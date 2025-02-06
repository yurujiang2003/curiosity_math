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

def common_prompt()->str:
    return """
Here are some examples of problems with solutions(Your are not required to answer them):

**Problem**: There are 35 animals (chickens and rabbits) in a cage with 94 legs in total. How many chickens and rabbits are there?

**Solution**:  
Let \( x \) be the number of chickens and \( y \) be the number of rabbits. Set up the system of equations:
\[
\begin{cases}
x + y = 35 \\
2x + 4y = 94
\end{cases}
\]
Solve the system to find \( x = 23 \) (chickens) and \( y = 12 \) (rabbits).

Note: Above is just some example teaching you to think out of box. You donot need to answer them. Your task is to answer the following problem.
    """

def ICL_prompt() -> str:
    return """
Here is an example of problems with both novel and common solutions(Your are not required to answer them):
**Problem**: There are 35 animals (chickens and rabbits) in a cage with 94 legs in total. How many chickens and rabbits are there?

**Common Solution**:  
Let \( x \) be the number of chickens and \( y \) be the number of rabbits. Set up the system of equations:
\[
\begin{cases}
x + y = 35 \\
2x + 4y = 94
\end{cases}
\]
Solve the system to find \( x = 23 \) (chickens) and \( y = 12 \) (rabbits).

**Novel Solution**:  
Assume all animals are chickens. Then the total number of legs would be \( 35 \times 2 = 70 \), which is 24 legs fewer than the actual count. Each time a chicken is replaced with a rabbit, the number of legs increases by 2. Therefore, \( 24 \div 2 = 12 \) replacements are needed, resulting in 12 rabbits and \( 35 - 12 = 23 \) chickens.

Note: Above is just an example teaching you to think out of box. You donot need to answer them. Your task is to answer the following problem.
"""

def batch_process_problems(
    problems: List[str],
    model_name: str,
    model_path: str,
    gpu_id: int = 0,
    batch_size: int = 8
) -> List[str]:

    inferencer = Inference(model_name, gpu_id, model_path)
    common_instructions = [

        f""" {common_prompt()}
        please solve the following problem.
        {problem}
        """ for problem in problems
    ]
    novel_instructions = [
        f""" {ICL_prompt()} 
        Your task is to solve the following problem out of the box, providing a novel solution.
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
    batch_size = 14
    num_problems = 100

    output_files = {
        "easy": "/home/shangbin/curiosity_math/Qwen2.5-7B-Instruct_responses_easy_ICL.json",
        "medium": "/home/shangbin/curiosity_math/Qwen2.5-7B-Instruct_responses_medium_ICL.json",
        "hard": "/home/shangbin/curiosity_math/Qwen2.5-7B-Instruct_responses_hard_ICL.json"
    }

    print("Collecting problems...")

    problems = {
        "easy": collect_problems_from_json(data_dir, level="Level 1", limit=num_problems),
        "medium": collect_problems_from_json(data_dir, level="Level 3", limit=num_problems),
        "hard": collect_problems_from_json(data_dir, level="Level 5", limit=num_problems)
    }
    
    try:
        for difficulty, problem_set in problems.items():
            print(f"Found {len(problem_set)} {difficulty} problems")
            print(f"Processing {difficulty} problems...")
            
            # Create a new inferencer for each difficulty level
            inferencer = Inference(model_name, gpu_id, model_path)
            
            try:
                # 准备指令
                common_instructions = [problem for problem in problem_set]
                novel_instructions = [
                    f""" {ICL_prompt()} 
                    please solve the following problem out of the box, providing a novel solution.
                    {problem}
                    """ for problem in problem_set
                ]
                
                # 生成响应
                print(f"Generating common responses for {difficulty}...")
                common_responses = inferencer.batch_generate_responses(
                    instructions=common_instructions,
                    batch_size=batch_size,
                    max_new_tokens=512,
                    temperature=0.7,
                    use_chat_template=True
                )
                
                # Reinitialize the model if needed
                if not hasattr(inferencer, 'model') or inferencer.model is None:
                    inferencer = Inference(model_name, gpu_id, model_path)
                
                print(f"Generating novel responses for {difficulty}...")
                novel_responses = inferencer.batch_generate_responses(
                    instructions=novel_instructions,
                    batch_size=batch_size,
                    max_new_tokens=512,
                    temperature=0.7,
                    use_chat_template=True
                )
                
                # 合并结果
                responses = [
                    {
                        "problem": problem,
                        "common_response": common_response,
                        "novel_response": novel_response
                    } for problem, common_response, novel_response in zip(problem_set, common_responses, novel_responses)
                ]

                # 保存结果
                output_file = output_files[difficulty]
                print(f"Saving {difficulty} results...")
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    for response in responses:
                        result = {
                            "problem": response["problem"],
                            "common_response": response["common_response"],
                            "novel_response": response["novel_response"],
                            "difficulty": difficulty
                        }
                        f.write(json.dumps(result, ensure_ascii=False) + '\n')
                
                print(f"Results saved to {output_file}")
                print(f"Completed processing {difficulty} problems")
                
            finally:
                # Clean up the inferencer after processing each difficulty level
                del inferencer
                torch.cuda.empty_cache()
    
    finally:
        torch.cuda.empty_cache()

if __name__ == "__main__":
    main()