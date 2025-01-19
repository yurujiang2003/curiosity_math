import requests
from typing import Optional

def run_chatopenai(
    model_name: str = "gpt-4o-mini",
    system_prompt: Optional[str] = None,
    user_prompt: str = "",
    temperature: float = 0,
    **chat_kwargs,
) -> str:
    chat_params = {
        "model": model_name,
        "messages": [{"role": "system", "content": system_prompt}, 
                    {"role": "user", "content": user_prompt}] if system_prompt 
                    else [{"role": "user", "content": user_prompt}],
        "max_tokens": 1000,
        "temperature": temperature,
        "tool_use": "not_allowed",
    } | chat_kwargs

    headers = {
        'Authorization': 'Bearer sk-9XJQZhobjuc8coK8ITRqvbecRRnEvLrGZ6FDBzkJn11PyfnW',
        'Content-Type': 'application/json',
    }
    
    response = requests.post(
        "https://api.claudeshop.top/v1/chat/completions", 
        headers=headers, 
        json=chat_params
    )
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    model_name = "gpt-4o-mini"
    system_prompt = "You are a helpful assistant."
    user_prompt = "What is the capital of France?"
    print(run_chatopenai(model_name, system_prompt, user_prompt))