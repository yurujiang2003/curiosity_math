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

def ICL_prompt() -> str:
    return """
Here are some examples of problems with both novel (correct) and common (incorrect) solutions:

Problem 1: Frog in a Well
A frog is at the bottom of a 30-foot well. Each day, it climbs up 3 feet but slips back 2 feet at night. How many days will it take for the frog to get out?

Common Wrong Solution:
- Net progress per day = 3 - 2 = 1 foot
- Total distance = 30 feet
- Days needed = 30/1 = 30 days
(Wrong because it ignores that on the last day, the frog doesn't slip back)

Novel Correct Solution:
- After day 1: 3-2 = 1 foot
- After day 2: 1+(3-2) = 2 feet
- This continues until day 28: 28 feet
- On day 29: 28+3 = 31 feet (reaches top)
Answer: 29 days (not 30)

Problem 2: Birthday Paradox
In a room of 23 people, what's the probability that at least two people share the same birthday?

Common Wrong Solution:
- Probability = 23/365 ≈ 6.3%
(Wrong because it only considers one pair)

Novel Correct Solution:
- Calculate probability of NO matches first
- P(no match) = (365/365) × (364/365) × (363/365) × ... × (343/365)
- P(no match) ≈ 0.492703...
- P(at least one match) = 1 - 0.492703... ≈ 50.7%
Answer: About 50.7% (surprisingly high!)

Problem 3: Infinite Hotel
An infinite hotel is fully booked. Can you accommodate one more guest? What about infinitely many new guests?

Common Wrong Solution:
- No rooms available, so no more guests possible
(Wrong because it applies finite thinking to infinite scenarios)

Novel Correct Solution:
For one guest:
- Move guest in room n to room n+1
- Room 1 becomes available
For infinitely many guests:
- Move guest in room n to room 2n
- All odd numbers become available
Answer: Yes to both! Infinite sets have counterintuitive properties.

Problem 4: Blue-Eyed Islanders
On an island, 100 people have blue eyes. Each person can see others' eye colors but not their own. If anyone figures out their eye color, they must leave the next day. Everyone knows there's at least one blue-eyed person. One day, an outsider announces that at least one person has blue eyes. What happens?

Common Wrong Solution:
- Nothing changes since everyone already knew there were blue-eyed people
(Wrong because it misses the common knowledge aspect)

Novel Correct Solution:
- If 1 person had blue eyes: They'd leave on day 1
- If 2 people: They'd leave on day 2
- If 3 people: They'd leave on day 3
- With 100 people: All leave on day 100
The announcement creates common knowledge that triggers a logical chain reaction.

Please solve the following problem with both:
1. A novel, out-of-the-box solution that is mathematically correct
2. A common but incorrect solution that many people might try first

Remember to explain why the common solution is wrong and why the novel solution works.
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
        problem for problem in problems
    ]
    novel_instructions = [
        f""" {ICL_prompt()} 
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
    data_dir = ""
    model_name = "Qwen/Qwen2.5-Math-7B"
    model_path = model_name
    gpu_id = 14
    batch_size = 4
    num_problems = 100

    output_files = {
        "easy": "",
        "medium": "",
        "hard": ""
    }

    print("Collecting problems...")

    problems = {
        "medium": collect_problems_from_json(data_dir, level="Level 3", limit=num_problems),
        "hard": collect_problems_from_json(data_dir, level="Level 5", limit=num_problems)
    }
    
    for difficulty, problem_set in problems.items():
        print(f"Found {len(problem_set)} {difficulty} problems")
        print(f"Processing {difficulty} problems...")
        
        # 对每个难度级别只运行1次
        print(f"Running iteration for {difficulty} problems")
        responses = batch_process_problems(
            problem_set,
            model_name,
            model_path,
            gpu_id,
            batch_size
        )

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
        
        # 清理GPU内存
        torch.cuda.empty_cache()
        
        print(f"Completed processing {difficulty} problems")

if __name__ == "__main__":
    main()