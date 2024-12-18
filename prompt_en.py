import os
import json
from pathlib import Path
from typing import List, Dict
from inference import Inference

def collect_problems_from_json(directory: str, limit: int = 100) -> List[str]:

    problems = []
    for path in Path(directory).rglob('*.json'):
        if limit is not None and len(problems) >= limit:
            break
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'problem' in data:
                    problems.append(data['problem'])
        except Exception as e:
            print(f"Error processing {path}: {e}")
    return problems

def batch_process_problems(
    problems: List[str],
    model_name: str,
    model_path: str,
    gpu_id: int = 0,
    batch_size: int = 8
) -> List[str]:

    inferencer = Inference(model_name, gpu_id, model_path)
    
    try:
        responses = inferencer.batch_generate_responses(
            instructions=problems,
            batch_size=batch_size,
            max_new_tokens=512,
            temperature=0.7,
            use_chat_template=True
        )
        return responses
    finally:

        del inferencer

def main():
    # 配置参数
    data_dir = "/home/shangbin/curiosity_math/datasets/MATH"
    model_name = "Qwen/Qwen2.5-Math-7B"
    model_path = model_name
    gpu_id = 15
    batch_size = 4
    output_file = "/home/shangbin/curiosity_math/qwen_2.5b_math_responses.jsonl"
    num_problems = 100

    print("Collecting problems...")
    problems = collect_problems_from_json(data_dir, limit=num_problems)
    print(f"Found {len(problems)} problems")

    print("Processing problems...")
    responses = batch_process_problems(
        problems,
        model_name,
        model_path,
        gpu_id,
        batch_size
    )

    # 保存结果
    print("Saving results...")
    with open(output_file, 'w', encoding='utf-8') as f:
        for problem, response in zip(problems, responses):
            result = {
                "problem": problem,
                "response": response
            }
            f.write(json.dumps(result, ensure_ascii=False) + '\n')

    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()