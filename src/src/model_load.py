from transformers import AutoTokenizer, AutoModelForCausalLM
import os

def download_and_save_model(model_name="Qwen/Qwen2.5-Math-7B", save_path="./models/qwen2.5"):
    os.makedirs(save_path, exist_ok=True)

    print("Downloading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.save_pretrained(save_path)
    print(f"Tokenizer saved to: {save_path}")

    print("Downloading model...")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        trust_remote_code=True
    )
    model.save_pretrained(save_path)
    print(f"Model saved to: {save_path}")
    
    return save_path

def load_local_model(model_path):

    print("Loading model from local...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto",
        trust_remote_code=True
    )
    return model, tokenizer

if __name__ == "__main__":

    local_path = download_and_save_model()
    model, tokenizer = load_local_model(local_path)