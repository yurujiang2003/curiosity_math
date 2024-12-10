from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from tqdm import tqdm
from torch.utils.data import DataLoader, Dataset

class Inference:
    def __init__(self, model_name, gpu_id, model_path):
        self.model_name = model_name
        self.gpu_id = gpu_id
        self.model_path = model_path
        self.model = None
        self.tokenizer = None
        self.device = f"cuda:{self.gpu_id}" if torch.cuda.is_available() else "cpu"
        
    class PromptDataset(Dataset):
        def __init__(self, prompts, tokenizer, max_length=512):
            self.prompts = prompts
            self.tokenizer = tokenizer
            self.max_length = max_length
        
        def __len__(self):
            return len(self.prompts)
        
        def __getitem__(self, idx):
            return self.prompts[idx]
            
    def load_model(self):
        if self.model is None:
            print(f"Loading model {self.model_name} on device {self.device}")
            model_path = self.model_path
            
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                torch_dtype=torch.bfloat16,
                local_files_only=True,
                trust_remote_code=True,
                device_map={'': self.device}  
            )
            
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
    
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.eval()
    
    def generate_response(
        self,
        instruction,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        use_chat_template=True
    ):
        """Generate single response"""
        self.load_model()
        try:
            with torch.no_grad():
                if use_chat_template:
                    chat = [
                        {"role": "user", "content": instruction},
                    ]
                    prompt = self.tokenizer.apply_chat_template(
                        chat, 
                        tokenize=False, 
                        add_generation_prompt=True
                    )
                    inputs = self.tokenizer.encode(
                        prompt, 
                        add_special_tokens=False, 
                        return_tensors="pt"
                    ).to(f"cuda:{self.gpu_id}")
                else:
                    full_prompt = f"Instruction: {instruction}\nResponse:"
                    inputs = self.tokenizer(
                        full_prompt,
                        return_tensors="pt",
                        padding=True,
                        truncation=True,
                        max_length=512
                    ).input_ids.to(f"cuda:{self.gpu_id}")
                
                outputs = self.model.generate(
                    inputs,
                    max_new_tokens=max_new_tokens,
                    do_sample=do_sample,
                    temperature=temperature,
                    top_p=top_p,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id
                )
                
                if use_chat_template:
                    response = self.tokenizer.decode(
                        outputs[0][len(inputs[0]):], 
                        skip_special_tokens=True
                    ).strip()
                else:
                    full_output = self.tokenizer.decode(
                        outputs[0], 
                        skip_special_tokens=True
                    )
                    response = full_output.split("Response:")[-1].strip()
                    
                return response
                
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return f"Error generating response: {str(e)}"

    def batch_generate_responses(
        self, 
        instructions,
        batch_size=10, 
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        use_chat_template=True
    ):
        try:
            self.load_model()
            responses = []
            
            # 1. pre-calculate dynamic batch size to avoid OOM
            max_batch_size = min(
                batch_size,
                max(1, int(torch.cuda.get_device_properties(self.gpu_id).total_memory * 0.7 
                          / (self.model.config.max_position_embeddings * 2048)))
            )
            
            # 2. pre-process all prompts
            if use_chat_template:
                batch_prompts = [
                    self.tokenizer.apply_chat_template(
                        [{"role": "user", "content": instruction}],
                        tokenize=False,
                        add_generation_prompt=True
                    )
                    for instruction in instructions
                ]
            else:
                batch_prompts = [
                    f"Instruction: {instruction}\nResponse:"
                    for instruction in instructions
                ]

            # 3. use DataLoader to optimize data loading
            dataset = self.PromptDataset(batch_prompts, self.tokenizer)
            dataloader = DataLoader(
                dataset, 
                batch_size=max_batch_size, 
                shuffle=False, 
                num_workers=2,
                pin_memory=True
            )

            # 4. batch process
            for batch_prompts in tqdm(dataloader, desc="Processing batches"):
                # 5. use automatic mixed precision
                with torch.no_grad(), torch.cuda.amp.autocast():
                    # batch encode
                    inputs = self.tokenizer(
                        batch_prompts,
                        padding=True,
                        truncation=True,
                        max_length=512,
                        return_tensors="pt"
                    ).to(self.device)

                    # 6. optimize generate parameters
                    outputs = self.model.generate(
                        input_ids=inputs.input_ids,
                        attention_mask=inputs.attention_mask,
                        max_new_tokens=max_new_tokens,
                        do_sample=do_sample,
                        temperature=temperature,
                        top_p=top_p,
                        pad_token_id=self.tokenizer.pad_token_id,
                        eos_token_id=self.tokenizer.eos_token_id,
                        use_cache=True,
                        num_beams=1,
                        early_stopping=True,
                        return_dict_in_generate=False,
                        repetition_penalty=1.0,
                        length_penalty=1.0,
                        no_repeat_ngram_size=0
                    )

                    # 8. parallel decoding
                    if use_chat_template:
                        batch_responses = [
                            self.tokenizer.decode(
                                output[inputs.input_ids[j].ne(self.tokenizer.pad_token_id).sum():],
                                skip_special_tokens=True
                            ).strip()
                            for j, output in enumerate(outputs)
                        ]
                    else:
                        batch_responses = [
                            self.tokenizer.decode(output, skip_special_tokens=True).split("Response:")[-1].strip()
                            for output in outputs
                        ]

                    responses.extend(batch_responses)

                # 9. clean up memory
                del inputs, outputs
                torch.cuda.empty_cache()

            return responses
            
        finally:
            # 10. clean up
            if hasattr(self, 'model') and self.model is not None:
                self.model.to('cpu')
                del self.model
                del self.tokenizer
                self.model = None
                self.tokenizer = None
                torch.cuda.empty_cache()

