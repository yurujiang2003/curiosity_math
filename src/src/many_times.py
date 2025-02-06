import json
import os
from inference import Inference
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm
import gc
from multiprocessing import Process

def get_instruction_template(question: str) -> str:
    """Generate instruction template with example and question
    
    Args:
        question: The math question to be answered
        
    Returns:
        Formatted instruction with example and question
    """
    return f"""Here is an example of problems with both novel and common solutions (You are not required to answer this example):

**Problem**: There are 35 animals (chickens and rabbits) in a cage with 94 legs in total. How many chickens and rabbits are there?

**Common Solution**:  
Let $x$ be the number of chickens and $y$ be the number of rabbits. Set up the system of equations:
\\[
\\begin{{cases}}
x + y = 35 \\\\
2x + 4y = 94
\\end{{cases}}
\\]
Solve the system to find $x = 23$ (chickens) and $y = 12$ (rabbits).

**Novel Solution**:  
Assume all animals are chickens. Then the total number of legs would be $35 \\times 2 = 70$, which is 24 legs fewer than the actual count. Each time a chicken is replaced with a rabbit, the number of legs increases by 2. Therefore, $24 \\div 2 = 12$ replacements are needed, resulting in 12 rabbits and $35 - 12 = 23$ chickens.

Note: Above is just an example teaching you to think out of box. You do not need to answer it. 
Your task is to solve the following problem:

{question}"""

class BatchInferencer:
    def __init__(self, model_name: str, gpu_id: int, model_path: str):
        """Initialize the inferencer with model"""
        self.inferencer = Inference(model_name, gpu_id, model_path)
        
    def process_all_questions(self, questions: list, num_repeats: int, output_file: str) -> dict:
        """Process all questions and save results"""
        results = {
            "metadata": {
                "model_name": self.inferencer.model_name,
                "num_repeats": num_repeats,
                "temperature": 1.0,
                "top_p": 0.9,
                "total_questions": len(questions)
            },
            "results": []
        }
        
        for question_data in tqdm(questions, desc="Processing questions"):
            question = question_data['question']
            instruction = get_instruction_template(question)
            question_instructions = [instruction] * num_repeats
            
            try:
                responses = self.inferencer.batch_generate_responses(
                    instructions=question_instructions,
                    batch_size=20,
                    max_new_tokens=512,
                    do_sample=True,
                    temperature=1.0,
                    top_p=0.9,
                    use_chat_template=True
                )
                
                result = {
                    "question": question,
                    "responses": responses,
                    "type": question_data['type'],
                    "level": question_data['level']
                }
                results["results"].append(result)
                
                # Save intermediate results periodically
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                
            except Exception as e:
                print(f"\nError processing question: {question[:100]}...")
                print(f"Error: {e}")
                continue
            
        return results

def extract_questions_from_sft(jsonl_file: str) -> list:
    """Extract questions from sft jsonl file
    
    Args:
        jsonl_file: path to the sft jsonl file
        
    Returns:
        list of questions with their metadata
    """
    questions = []
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            for msg in data['message']:
                if msg['role'] == 'user':
                    questions.append({
                        'question': msg['content'],
                        'type': data['type'],
                        'level': data['level']
                    })
                    break
    return questions

def process_questions(questions: list, 
                     model_name: str,
                     model_path: str,
                     num_repeats: int,
                     gpu_id: int,
                     output_dir: str):
    """Process questions with batched inference
    
    Args:
        questions: list of questions with metadata
        model_name: name of the model
        model_path: path to the model
        num_repeats: number of times to repeat inference
        gpu_id: GPU ID to use
        output_dir: output directory for results
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "responses_20_times.json")
    
    # Initialize inferencer and process all questions
    print("\nInitializing model...")
    inferencer = BatchInferencer(model_name, gpu_id, model_path)
    
    try:
        # Process all questions at once
        results = inferencer.process_all_questions(questions, num_repeats, output_file)
            
    finally:
        # Cleanup only once at the end
        del inferencer.inferencer
        del inferencer
        gc.collect()
        torch.cuda.empty_cache()
    
    print(f"\nAll questions processed. Results saved to {output_file}")
    
    # Print statistics
    type_counts = {}
    level_counts = {}
    for result in results["results"]:
        type_counts[result['type']] = type_counts.get(result['type'], 0) + 1
        level_counts[result['level']] = level_counts.get(result['level'], 0) + 1
        
    print("\nProcessed questions by type:")
    for type_, count in type_counts.items():
        print(f"{type_}: {count}")
        
    print("\nProcessed questions by level:")
    for level, count in level_counts.items():
        print(f"{level}: {count}")

def split_questions(questions: list, num_gpus: int, gpu_id: int) -> list:
    """Split questions among GPUs
    
    Args:
        questions: List of all questions
        num_gpus: Total number of GPUs
        gpu_id: Current GPU ID
        
    Returns:
        List of questions assigned to this GPU
    """
    total_questions = len(questions)
    questions_per_gpu = total_questions // num_gpus
    start_idx = gpu_id * questions_per_gpu
    end_idx = start_idx + questions_per_gpu if gpu_id < num_gpus - 1 else total_questions
    return questions[start_idx:end_idx]

def run_gpu_process(gpu_id: int, questions: list, model_name: str, model_path: str, 
                   num_repeats: int, output_dir: str):
    """Run inference process on a specific GPU
    
    Args:
        gpu_id: GPU ID to use
        questions: Questions to process
        model_name: Name of the model
        model_path: Path to the model
        num_repeats: Number of times to repeat inference
        output_dir: Output directory for results
    """
    print(f"\nStarting process for GPU {gpu_id}")
    gpu_output_dir = os.path.join(output_dir, f"gpu_{gpu_id}")
    os.makedirs(gpu_output_dir, exist_ok=True)
    
    try:
        process_questions(
            questions=questions,
            model_name=model_name,
            model_path=model_path,
            num_repeats=num_repeats,
            gpu_id=gpu_id,
            output_dir=gpu_output_dir
        )
    except Exception as e:
        print(f"Error in GPU {gpu_id} process: {e}")

def main():
    # Configuration
    input_file = "/home/shangbin/curiosity_math/datasets/organized_math_train/math_dataset_sft.jsonl"
    model_name = "Qwen/Qwen2.5-Math-7B"
    model_path = model_name
    num_repeats = 20
    num_gpus = 5
    gpu_ids = [10, 11, 12, 13, 14]
    output_dir = "/home/shangbin/curiosity_math/many_times_results"
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract all questions
    print("Extracting questions from jsonl file...")
    all_questions = extract_questions_from_sft(input_file)
    print(f"Extracted {len(all_questions)} questions in total")
    
    # Create processes for each GPU
    processes = []
    for gpu_idx, gpu_id in enumerate(gpu_ids):
        # Get questions for this GPU
        gpu_questions = split_questions(all_questions, num_gpus, gpu_idx)
        print(f"Assigning {len(gpu_questions)} questions to GPU {gpu_id}")
        
        # Create and start process
        p = Process(target=run_gpu_process, args=(
            gpu_id, 
            gpu_questions, 
            model_name, 
            model_path, 
            num_repeats, 
            output_dir
        ))
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    print("\nAll GPU processes completed!")
    
    # Optional: Merge results
    print("\nMerging results from all GPUs...")
    merge_results(output_dir)

def merge_results(base_dir: str):
    """Merge results from all GPUs into a single file"""
    merged_results = {
        "metadata": {},
        "results": []
    }
    
    # Collect results from each GPU
    for gpu_dir in sorted(os.listdir(base_dir)):
        if not gpu_dir.startswith('gpu_'):
            continue
            
        result_file = os.path.join(base_dir, gpu_dir, 'responses_20_times.json')
        if not os.path.exists(result_file):
            print(f"Warning: Missing results from {gpu_dir}")
            continue
            
        with open(result_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not merged_results["metadata"]:
                merged_results["metadata"] = data["metadata"]
            merged_results["results"].extend(data["results"])
    
    # Update total questions count
    if merged_results["metadata"]:
        merged_results["metadata"]["total_questions"] = len(merged_results["results"])
    
    # Save merged results
    output_file = os.path.join(base_dir, "merged_responses.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_results, f, ensure_ascii=False, indent=2)
    
    print(f"Merged results saved to {output_file}")

if __name__ == "__main__":
    main()