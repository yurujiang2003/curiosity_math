from transformers import AutoModelForCausalLM, AutoTokenizer
from model_load import load_local_model
import torch

class Qwen_inference:
    def __init__(self, model_name="models/qwen2.5", device="cuda", prompt=None):
        self.model, self.tokenizer = load_local_model(model_name)
        self.prompt = prompt

    def generate_response(self, prompt, max_length=2048):
        return generate_response(prompt, self.model, self.tokenizer, max_length)

def generate_response(prompt, model, tokenizer, max_length=2048):
    # 将输入转换为模型可处理的格式
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    # 生成回复
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        temperature=0.7,  # 控制生成的随机性
        top_p=0.9,       # nucleus sampling参数
    )
    
    # 解码输出
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    # 加载模型和tokenizer
    model, tokenizer = load_model()
    
    # 示例对话
    prompt = "你好，请介绍一下你自己。"
    response = generate_response(prompt, model, tokenizer)
    print("用户:", prompt)
    print("Qwen:", response)

if __name__ == "__main__":
    main()