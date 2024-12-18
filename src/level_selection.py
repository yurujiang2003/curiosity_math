import os
import json
import torch
from pathlib import Path
from typing import List, Dict
from inference import Inference

def collect_problems_from_json(
    directory: str, 
    level: str = None, 
    limit: int = 100
) -> List[str]:
    """
    collect problems from json files, and filter by level
    
    Args:
        directory (str): the directory of json files
        level (str): the level of problems, like "Level 1" to "Level 5", None means all levels
        limit (int): the number of problems to return
    
    Returns:
        List[str]: the list of problems
    """
    problems = []
    
    for path in Path(directory).rglob('*.json'):
        if limit is not None and len(problems) >= limit:
            break
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                if 'problem' in data and (level is None or data.get('level') == level):
                    problem_data = {
                        'problem': data['problem'],
                        'level': data.get('level', 'Unknown'),
                        'type': data.get('type', 'Unknown'),
                        'path': str(path)
                    }
                    problems.append(problem_data)
                    
        except Exception as e:
            print(f"Error processing {path}: {e}")
    
    # sort by level
    level_order = {
        'Level 1': 1,
        'Level 2': 2,
        'Level 3': 3,
        'Level 4': 4,
        'Level 5': 5,
        'Unknown': 6
    }
    problems.sort(key=lambda x: level_order.get(x['level'], 999))

    return [p['problem'] for p in problems]

def batch_process_problems(
    problems: List[str],
    model_name: str,
    model_path: str,
    gpu_id: int = 0,
    batch_size: int = 8
) -> List[str]:

    inferencer = Inference(model_name, gpu_id, model_path)
    common_instructions = [
        problem for problem in problems
    ]
    novel_instructions = [
        f""" 
        please solve the following problem out of the box, providing a novel solution.
        {problem}
        """ for problem in problems
    ]
    
    try:
        common_responses = inferencer.batch_generate_responses(
            instructions=common_instructions,
            batch_size=batch_size,
            max_new_tokens=512,
            temperature=0.7,
            use_chat_template=True
        )
        novel_responses = inferencer.batch_generate_responses(
            instructions=novel_instructions,
            batch_size=batch_size,
            max_new_tokens=512,
            temperature=0.7,
            use_chat_template=True
        )
        
        combined_responses = [
            {
                "problem": problem,
                "common_response": common_response,
                "novel_response": novel_response
            } for problem, common_response, novel_response in zip(problems, common_responses, novel_responses)
        ]
        return combined_responses
    finally:

        del inferencer

def main():
    data_dir = "/home/shangbin/curiosity_math/datasets/MATH"
    model_name = "Qwen/Qwen2.5-Math-7B"
    model_path = model_name
    gpu_id = 15
    batch_size = 4
    num_problems = 100

    output_files = {
        "easy": "/home/shangbin/curiosity_math/qwen_2.5b_math_responses_easy.json",
        "medium": "/home/shangbin/curiosity_math/qwen_2.5b_math_responses_medium.json",
        "hard": "/home/shangbin/curiosity_math/qwen_2.5b_math_responses_hard.json"
    }

    print("Collecting problems...")

    problems = {
        "easy": collect_problems_from_json(data_dir, level="Level 2", limit=num_problems),
        "medium": collect_problems_from_json(data_dir, level="Level 3", limit=num_problems),
        "hard": collect_problems_from_json(data_dir, level="Level 5", limit=num_problems)
    }
    
    for difficulty, problem_set in problems.items():
        print(f"Found {len(problem_set)} {difficulty} problems")
        print(f"Processing {difficulty} problems...")
        
        # 对每个难度级别运行3次
        for iteration in range(3):
            print(f"Running iteration {iteration + 1} for {difficulty} problems")
            responses = batch_process_problems(
                problem_set,
                model_name,
                model_path,
                gpu_id,
                batch_size
            )

            output_file = output_files[difficulty].replace('.json', f'_iter{iteration+1}.json')
            print(f"Saving {difficulty} results for iteration {iteration + 1}...")
            
            with open(output_file, 'w', encoding='utf-8') as f:
                for response in responses:
                    result = {
                        "problem": response["problem"],
                        "common_response": response["common_response"],
                        "novel_response": response["novel_response"],
                        "difficulty": difficulty,
                        "iteration": iteration + 1
                    }
                    f.write(json.dumps(result, ensure_ascii=False) + '\n')
            
            print(f"Results saved to {output_file}")
            
            # 清理GPU内存
            torch.cuda.empty_cache()
            
        print(f"Completed processing {difficulty} problems")

if __name__ == "__main__":
    main()