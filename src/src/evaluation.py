import json
from pathlib import Path
from typing import Dict, List, Tuple
from inference import Inference
import torch

def load_responses(file_path: str) -> List[Dict]:
    """
    load question and response from json file
    
    Args:
        file_path: JSON file path
    
    Returns:
       include the dict of question and response
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        responses = []
        for line in f:
            try:
                response = json.loads(line.strip())
                if all(k in response for k in ['problem', 'common_response', 'novel_response']):
                    responses.append(response)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse line: {line[:100]}...")
                continue
    return responses

def extract_qa_pairs(responses: List[Dict]) -> List[Tuple[str, str, str]]:
    """
    extract question and response from the dict
    
    Args:
        responses: the dict of question and response
    
    Returns:
        the tuple of question, common_response and novel_response
    """
    qa_pairs = []
    for response in responses:
        problem = response['problem']
        solution = response['solution']
        common_response = response['common_response']
        novel_response = response['novel_response']
        qa_pairs.append((problem, solution, common_response, novel_response))
    return qa_pairs

def evaluate_responses_batch(inference: Inference, qa_pairs: List[Tuple[str, str, str]], batch_size: int = 10) -> List[Tuple[bool, bool]]:
    """
    批量评估问题-答案对
    
    Args:
        inference: LLM推理实例
        qa_pairs: 问题和两种回答的元组列表
        batch_size: 批处理大小
    
    Returns:
        每对回答的正确性评估结果列表
    """
    # 准备评估提示
    evaluation_prompts = []
    for problem, solution, common, novel in qa_pairs:
        # 为common response创建提示
        common_prompt = f"""Please evaluate if the following response correctly solves the math problem. 
Answer with only 'Correct' or 'Incorrect'.

Problem:
{problem}

And the ground truth is:
{solution}

Response:
{common}

Is this response correct?"""
        
        # 为novel response创建提示
        novel_prompt = f"""Please evaluate if the following response correctly solves the math problem. 
Answer with only 'Correct' or 'Incorrect'.

Problem:
{problem}

And the ground truth is:
{solution}

Response:
{novel}

Is this response correct?"""
        
        evaluation_prompts.extend([common_prompt, novel_prompt])
    
    # 批量生成评估结果
    print("Generating evaluations...")
    evaluation_results = inference.batch_generate_responses(
        evaluation_prompts,
        batch_size=batch_size,
        max_new_tokens=128,  # 对于简单的正确/错误回答，可以使用较小的token数
        temperature=0.1,     # 降低随机性
        top_p=0.9
    )
    
    # 解析结果
    results = []
    for i in range(0, len(evaluation_results), 2):
        common_result = "correct" in evaluation_results[i].lower()
        novel_result = "correct" in evaluation_results[i+1].lower()
        results.append((common_result, novel_result))
        
        # 打印进度
        pair_index = i // 2
        print(f"\nPair {pair_index + 1}/{len(qa_pairs)}:")
        print(f"Common response: {'Correct' if common_result else 'Incorrect'}")
        print(f"Novel response: {'Correct' if novel_result else 'Incorrect'}")
    
    return results

def main():

    file_paths = [
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_easy_ICL_iter1.json",
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_easy_ICL_iter2.json",
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_easy_iter1.json",
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_easy_iter2.json",
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_easy_iter3.json",
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_medium_ICL.json",
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_medium_iter1.json",
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_medium_iter2.json",
        "/home/shangbin/curiosity_math/prompt_ICL/qwen_2.5b_math_responses_medium_iter3.json"
    ]

    try:
        for file_path in file_paths:
            inference = Inference(
                model_name="deepseek-ai/deepseek-math-7b-instruct",
                gpu_id=15,
                model_path="/home/shangbin/models/deepseek-math-7b-instruct",
                local_files_only=True
            )
            # 从文件路径获取文件名（不含扩展名）
            file_stem = Path(file_path).stem
            
            # 加载和提取QA对
            responses = load_responses(file_path)
            qa_pairs = extract_qa_pairs(responses)
            print(f"\nProcessing {file_stem}")
            print(f"Loaded {len(qa_pairs)} question-answer pairs")

            # 批量评估
            evaluation_results = evaluate_responses_batch(inference, qa_pairs, batch_size=10)
            
            # 统计结果
            total_pairs = len(evaluation_results)
            common_correct = sum(r[0] for r in evaluation_results)
            novel_correct = sum(r[1] for r in evaluation_results)
            
            print("\nEvaluation Summary:")
            print(f"Total pairs evaluated: {total_pairs}")
            print(f"Common responses correct: {common_correct} ({common_correct/total_pairs*100:.1f}%)")
            print(f"Novel responses correct: {novel_correct} ({novel_correct/total_pairs*100:.1f}%)")
            
            # 保存结果到以原文件名为基础的新文件
            results_data = {
                "file_name": file_stem,
                "total_pairs": total_pairs,
                "common_correct": common_correct,
                "novel_correct": novel_correct,
                "common_accuracy": common_correct/total_pairs*100,
                "novel_accuracy": novel_correct/total_pairs*100,
                "detailed_results": [
                    {
                        "problem": qa_pairs[i][0][:200],  # 只保存前200个字符
                        "common_correct": evaluation_results[i][0],
                        "novel_correct": evaluation_results[i][1]
                    }
                    for i in range(total_pairs)
                ]
            }
            
            # Create the evaluation_results directory if it doesn't exist
            output_dir = Path(file_path).parent / "evaluation_results"
            output_dir.mkdir(exist_ok=True)
            
            output_path = output_dir / f"deepseek_evaluation_results_{file_stem}.json"
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(results_data, f, indent=2, ensure_ascii=False)
            print(f"Results saved to {output_path}")

            del inference
            torch.cuda.empty_cache()

    finally:
        torch.cuda.empty_cache()

if __name__ == "__main__":
    main()