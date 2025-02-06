from dataclasses import dataclass
from typing import List, Optional
from transformers import AutoTokenizer, TrainingArguments
from datasets import Dataset
import json
import torch
from unsloth import FastLanguageModel
import wandb
from trl import SFTTrainer

#### accept config from yaml: 
#### accelerate launch --config_file=/path/to/config.yaml --num_processes 4 /path/to/sft.py

@dataclass
class TrainingConfig:
    """Configuration for training"""
    per_device_train_batch_size: int = 4
    gradient_accumulation_steps: int = 8
    num_train_epochs: int = 5
    learning_rate: float = 2e-4
    bf16: bool = True
    logging_steps: int = 10
    max_seq_length: int = 512
    save_strategy: str = "steps"
    save_steps: int = 100
    logging_dir: str = "./logs"
    gradient_checkpointing: bool = True

@dataclass
class LoRAConfig:
    """Config for LoRA"""
    r: int = 32
    lora_alpha: int = 8
    target_modules: List[str] = None
    lora_dropout: float = 0.1
    bias: str = "none"

    def __post_init__(self):
        if self.target_modules is None:
            self.target_modules = ["q_proj", "v_proj", "k_proj", "o_proj"]

class QwenTrainer:
    def __init__(
        self,
        model_name: str,
        output_dir: str,
        dataset_path: str,
        training_config: Optional[TrainingConfig] = None,
        lora_config: Optional[LoRAConfig] = None,
    ):
        self.model_name = model_name
        self.output_dir = output_dir
        self.dataset_path = dataset_path
        self.training_config = training_config or TrainingConfig()
        self.lora_config = lora_config or LoRAConfig()
        
        wandb.init(
            project="qwen-math-sft",
            name=f"qwen-math-sft-{wandb.util.generate_id()}",
            config={
                "model_name": model_name,
                "training_config": self.training_config.__dict__,
                "lora_config": self.lora_config.__dict__
            }
        )

    def load_dataset(self):
        """Load and format dataset"""
        print("Loading dataset...")
        with open(self.dataset_path, 'r') as f:
            data = [json.loads(line) for line in f]
        
        # Initialize tokenizer here since we need it for formatting
        tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            trust_remote_code=True
        )
        
        formatted_data = []
        for item in data:
            messages = item["message"]
            # 使用tokenizer的chat template
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False
            )
            # Tokenize the text
            encoded = tokenizer(
                text,
                truncation=True,
                padding="max_length",
                max_length=self.training_config.max_seq_length,
                return_tensors=None  # Return list instead of tensors
            )
            formatted_data.append(encoded)
        
        self.dataset = Dataset.from_list(formatted_data)
        print(f"Loaded {len(self.dataset)} examples")
        return self.dataset

    def train(self):
        """Train the model"""
        print("Loading model and tokenizer...")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=self.model_name,
            max_seq_length=self.training_config.max_seq_length,
            dtype=torch.bfloat16 if self.training_config.bf16 else torch.float32,
            load_in_4bit=True,
            trust_remote_code=True
        )
        
        print("Applying LoRA...")
        model = FastLanguageModel.get_peft_model(
            model,
            r=self.lora_config.r,
            target_modules=self.lora_config.target_modules,
            lora_alpha=self.lora_config.lora_alpha,
            lora_dropout=self.lora_config.lora_dropout,
            bias=self.lora_config.bias,
            use_gradient_checkpointing=self.training_config.gradient_checkpointing,
        )
        
        print("Setting up training arguments...")
        training_args = TrainingArguments(
            output_dir=self.output_dir,
            num_train_epochs=self.training_config.num_train_epochs,
            per_device_train_batch_size=self.training_config.per_device_train_batch_size,
            gradient_accumulation_steps=self.training_config.gradient_accumulation_steps,
            learning_rate=self.training_config.learning_rate,
            logging_steps=self.training_config.logging_steps,
            save_steps=self.training_config.save_steps,
            save_strategy=self.training_config.save_strategy,
            bf16=self.training_config.bf16,
            report_to="wandb",
            remove_unused_columns=False,
            gradient_checkpointing=self.training_config.gradient_checkpointing
        )
        
        print("Starting training...")
        trainer = SFTTrainer(
            model=model,
            tokenizer=tokenizer,
            args=training_args,
            train_dataset=self.dataset,
            max_seq_length=self.training_config.max_seq_length,
        )
        
        trainer.train()
        print(f"Training completed. Model saved to {self.output_dir}")
        
        # Save final model
        trainer.save_model(self.output_dir)
        wandb.finish()

def main():
    training_config = TrainingConfig(
        per_device_train_batch_size=4,
        gradient_accumulation_steps=8,
        num_train_epochs=5,
        learning_rate=1e-5,
        gradient_checkpointing=True,
        bf16=True
    )
    
    lora_config = LoRAConfig(
        r=32,
        lora_alpha=8,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"]
    )
    
    trainer = QwenTrainer(
        model_name="Qwen/Qwen2.5-Math-7B",
        output_dir="/home/shangbin/curiosity_math/models/qwen-math-sft-outlier",
        dataset_path="/home/shangbin/curiosity_math/datasets/math_outliers_dataset.jsonl",
        training_config=training_config,
        lora_config=lora_config
    )
    
    trainer.load_dataset()
    trainer.train()

if __name__ == "__main__":
    main()