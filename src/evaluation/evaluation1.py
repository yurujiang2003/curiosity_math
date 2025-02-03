import json
import os
import argparse
from tqdm import tqdm
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import random
import numpy as np
from datetime import datetime

def set_seed(seed):
    """Set random seed for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, required=True, help="Path to local model")
    parser.add_argument("--data_path", type=str, required=True, help="Path to organized MATH dataset")
    parser.add_argument("--output_dir", type=str, default="./outputs", help="Output directory")
    parser.add_argument("--max_new_tokens", type=int, default=512)
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--cot", action="store_true", help="Use CoT")
    parser.add_argument("--device", type=str, default="cuda", help="Device to use (cuda/cpu)")
    parser.add_argument("--gpu_ids", type=str, default="0", help="Comma-separated list of GPU IDs to use")
    parser.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature")
    parser.add_argument("--top_p", type=float, default=1.0, help="Top-p sampling")
    parser.add_argument("--num_beams", type=int, default=1, help="Number of beams for beam search")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--save_incorrect_only", action="store_true", help="Only save incorrect predictions")
    parser.add_argument("--trust_remote_code", action="store_true", help="Trust remote code when loading models")
    return parser.parse_args()

def set_gpu_device(args):
    """Set GPU device and return device string."""
    if args.device == "cuda" and torch.cuda.is_available():
        # Set visible GPU devices
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu_ids
        # Get the actual device string (e.g., "cuda:0")
        device = f"cuda:{0}"  # Always use first visible GPU after setting CUDA_VISIBLE_DEVICES
        print(f"Using GPU(s): {args.gpu_ids}")
    else:
        device = "cpu"
        print("Using CPU")
    return device

def load_model_and_tokenizer(args):
    """Load model and tokenizer with error handling."""
    print(f"Loading model from {args.model_path}")
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            args.model_path,
            trust_remote_code=args.trust_remote_code
        )
        # Set padding side to left for decoder-only models
        tokenizer.padding_side = 'left'
        
        model = AutoModelForCausalLM.from_pretrained(
            args.model_path,
            torch_dtype=torch.float16,
            device_map={"": args.device},  # Map model to specified device
            trust_remote_code=args.trust_remote_code
        )
        return model, tokenizer
    except Exception as e:
        raise RuntimeError(f"Error loading model and tokenizer: {e}")

def construct_prompt_cot(problem):
    return f"""Question: {problem['problem']}

Let's solve this step by step and provide the answer in the format of \boxed{...}:"""

def construct_prompt_no_cot(problem):
    return f"""Question: {problem['problem']}

Please solve the problem and provide the answer in the format of \boxed{...}:"""

def normalize_answer(answer):
    """Normalize answer string for comparison."""
    try:
        # 预处理：移除多余空白并转小写
        answer = answer.strip().lower()
        
        # 定义替换规则字典
        replacements = {
            # LaTeX命令和格式
            '\\boxed{': '', '\\boxed': '', '{': '', '}': '',
            '\\left': '', '\\right': '', '\\big': '', '\\Big': '',
            '\\;': '', '\\,': '', '\\:': '', '\\!': '', '\\space': '',
            
            # 分数
            '\\frac': '', '\\dfrac': '',
            
            # 数学运算符
            '\\times': '*', '\\cdot': '*', '\\div': '/',
            
            # 特殊数学符号
            '\\sqrt': 'sqrt',
            '\\pi': 'pi',
            '\\infty': 'infinity', '\\infinity': 'infinity',
            
            # 数字格式
            '-': 'negative',
            ',': '',
            '.': 'point',
        }
        
        # 应用所有替换规则
        for old, new in replacements.items():
            answer = answer.replace(old, new)
        
        # 移除所有剩余的反斜杠和命令
        answer = answer.replace('\\', '')
        
        # 标准化空白
        answer = ' '.join(answer.split())
        
        # 移除前后的空白字符
        answer = answer.strip()
        
        return answer
    except Exception as e:
        print(f"Error in normalize_answer: {e}")
        return answer

def extract_answer(response):
    """Extract and normalize answer from response."""
    try:
        if "\\boxed" in response:
            # 找到最后一个boxed（通常是最终答案）
            last_boxed = response.rindex("\\boxed")
            remaining = response[last_boxed:]
            
            # 使用栈来处理嵌套的括号
            stack = []
            start = remaining.index("{") + 1
            end = start
            
            for i in range(start, len(remaining)):
                if remaining[i] == "{":
                    stack.append("{")
                elif remaining[i] == "}":
                    stack.pop()
                    if not stack:  # 找到匹配的最外层括号
                        end = i
                        break
            
            if start < end:  # 确保提取到了有效内容
                answer = remaining[start:end]
                return normalize_answer(answer)
            
        # 如果没有找到boxed答案或提取失败，尝试其他提取方法
        # 1. 尝试提取"The answer is..."后面的内容
        if "the answer is" in response.lower():
            answer_start = response.lower().index("the answer is") + len("the answer is")
            answer = response[answer_start:].strip()
            return normalize_answer(answer)
            
        # 2. 尝试提取最后一个句子作为答案
        sentences = response.split('.')
        if sentences:
            return normalize_answer(sentences[-1])
            
        # 如果所有方法都失败，标准化整个响应
        return normalize_answer(response)
        
    except Exception as e:
        print(f"Error in extract_answer: {e}")
        return normalize_answer(response)

def are_answers_equivalent(pred, target):
    """Check if predicted answer is equivalent to target answer."""
    try:
        # 标准化两个答案
        pred = normalize_answer(pred)
        target = normalize_answer(target)
        
        # 基本相等性检查
        if pred == target:
            return True
        
        # 移除所有空格进行比较
        if pred.replace(' ', '') == target.replace(' ', ''):
            return True
            
        # 尝试数值比较
        try:
            # 处理分数
            def parse_fraction(s):
                if 'over' in s:
                    num, denom = s.split('over')
                    return float(num.strip()) / float(denom.strip())
                return float(s.replace('point', '.').replace('negative', '-'))
            
            # 转换为数值并比较
            pred_val = parse_fraction(pred)
            target_val = parse_fraction(target)
            
            # 使用相对误差进行比较
            rel_tol = 1e-9  # 相对误差容限
            abs_tol = 1e-9  # 绝对误差容限
            if abs(pred_val - target_val) <= max(rel_tol * max(abs(pred_val), abs(target_val)), abs_tol):
                return True
        except:
            pass
        
        # 处理多项选择题答案
        def is_multiple_choice(ans):
            return all(c in 'abcde' for c in ans.replace(' ', '').lower())
        
        if is_multiple_choice(pred) and is_multiple_choice(target):
            pred_choices = ''.join(sorted(pred.replace(' ', '').lower()))
            target_choices = ''.join(sorted(target.replace(' ', '').lower()))
            return pred_choices == target_choices
        
        # 处理集合答案
        def parse_set(s):
            # 移除集合符号和空格
            s = s.replace('{', '').replace('}', '').replace(' ', '')
            # 分割元素并排序
            elements = sorted(s.split(','))
            return elements
        
        if ('{' in pred and '}' in pred) or ('{' in target and '}' in target):
            try:
                pred_set = parse_set(pred)
                target_set = parse_set(target)
                return pred_set == target_set
            except:
                pass
        
        # 处理区间表示
        def parse_interval(s):
            # 移除区间符号和空格
            s = s.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace(' ', '')
            # 分割并转换为数值
            start, end = s.split(',')
            return float(start.replace('point', '.').replace('negative', '-')), \
                   float(end.replace('point', '.').replace('negative', '-'))
        
        if ('[' in pred and ']' in pred) or ('(' in pred and ')' in pred):
            try:
                pred_interval = parse_interval(pred)
                target_interval = parse_interval(target)
                return pred_interval == target_interval
            except:
                pass
        
        # 处理向量/坐标
        def parse_vector(s):
            # 移除向量符号和空格
            s = s.replace('<', '').replace('>', '').replace('(', '').replace(')', '').replace(' ', '')
            # 分割并转换为数值
            components = [float(x.replace('point', '.').replace('negative', '-')) 
                        for x in s.split(',')]
            return components
        
        if ('<' in pred and '>' in pred) or ('(' in pred and ')' in pred):
            try:
                pred_vector = parse_vector(pred)
                target_vector = parse_vector(target)
                return pred_vector == target_vector
            except:
                pass
        
        return False
        
    except Exception as e:
        print(f"Error in are_answers_equivalent: {e}")
        return False

def generate_answer(model, tokenizer, prompts, args):
    """Batch process multiple prompts with enhanced error handling and memory management."""
    all_responses = []
    
    for i in tqdm(range(0, len(prompts), args.batch_size), desc="Generating answers"):
        batch_prompts = prompts[i:i + args.batch_size]
        
        try:
            inputs = tokenizer(
                batch_prompts,
                return_tensors="pt",
                padding=True,
                truncation=True
            ).to(args.device)
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=args.max_new_tokens,
                    do_sample=(args.temperature > 0),
                    temperature=args.temperature,
                    top_p=args.top_p,
                    num_beams=args.num_beams,
                    pad_token_id=tokenizer.eos_token_id
                )
            
            decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
            
            for prompt, response in zip(batch_prompts, decoded_outputs):
                response = response[len(prompt):].strip()
                all_responses.append(response)
                
        except Exception as e:
            print(f"Error processing batch {i}: {e}")
            all_responses.extend(["" for _ in range(len(batch_prompts))])
        
        # Clear cache after each batch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    
    return all_responses

def evaluate_file(model, tokenizer, data_file, args):
    """Evaluate a single file with enhanced error handling."""
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading file {data_file}: {e}")
        return []

    problems = data['problems']
    prompts = [construct_prompt_cot(problem) if args.cot else construct_prompt_no_cot(problem) 
              for problem in problems]

    responses = generate_answer(model, tokenizer, prompts, args)
    
    correct = 0
    results = []
    
    for problem, model_response in zip(problems, responses):
        predicted_answer = extract_answer(model_response)
        ground_truth = extract_answer(problem['solution'])
        
        is_correct = predicted_answer == ground_truth
        correct += int(is_correct)
        
        if not args.save_incorrect_only or not is_correct:
            result = {
                "problem": problem['problem'],
                "ground_truth": problem['solution'],
                "ground_truth_answer": ground_truth,
                "model_response": model_response,
                "predicted_answer": predicted_answer,
                "is_correct": is_correct,
                "level": problem['level'],
                "type": problem['type']
            }
            results.append(result)
    
    accuracy = correct / len(problems) if problems else 0
    print(f"Accuracy for {data_file}: {accuracy:.2%}")
    
    return results

def main():
    args = parse_args()
    set_seed(args.seed)
    
    # Set GPU device before loading model
    args.device = set_gpu_device(args)
    
    # Create output directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    args.output_dir = os.path.join(args.output_dir, timestamp)
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Save configuration
    with open(os.path.join(args.output_dir, "config.json"), 'w') as f:
        json.dump(vars(args), f, indent=2)
    
    model, tokenizer = load_model_and_tokenizer(args)
    
    all_results = []
    for root, _, files in os.walk(args.data_path):
        for file in tqdm(sorted(files), desc="Processing files"):
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                print(f"\nProcessing {file_path}")
                results = evaluate_file(model, tokenizer, file_path, args)
                all_results.extend(results)
                
                # Save intermediate results with level and type info
                level = results[0]['level'] if results else "unknown"
                problem_type = results[0]['type'] if results else "unknown"
                # 使用目录结构来组织不同level和type的结果
                level_dir = os.path.join(args.output_dir, level.replace(" ", "_"))
                os.makedirs(level_dir, exist_ok=True)
                
                output_file = os.path.join(level_dir, f"results_{problem_type}_{file}")
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Save all results
    with open(os.path.join(args.output_dir, "all_results.json"), 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    
    # Print summary statistics
    print("\nEvaluation Summary:")
    by_level = {}
    by_type = {}
    total_correct = 0
    total_problems = 0
    
    for result in all_results:
        level = result['level']
        problem_type = result['type']
        
        for stats_dict, key in [(by_level, level), (by_type, problem_type)]:
            if key not in stats_dict:
                stats_dict[key] = {'total': 0, 'correct': 0}
            stats_dict[key]['total'] += 1
            stats_dict[key]['correct'] += int(result['is_correct'])
        
        total_correct += int(result['is_correct'])
        total_problems += 1
    
    # Save and print statistics
    statistics = {
        "by_level": by_level,
        "by_type": by_type,
        "overall": {
            "total": total_problems,
            "correct": total_correct,
            "accuracy": total_correct/total_problems if total_problems else 0
        }
    }
    
    with open(os.path.join(args.output_dir, "statistics.json"), 'w') as f:
        json.dump(statistics, f, indent=2)
    
    print("\nBy Level:")
    for level, stats in sorted(by_level.items()):
        accuracy = stats['correct'] / stats['total']
        print(f"{level}: {stats['correct']}/{stats['total']} = {accuracy:.2%}")
    
    print("\nBy Type:")
    for type_, stats in sorted(by_type.items()):
        accuracy = stats['correct'] / stats['total']
        print(f"{type_}: {stats['correct']}/{stats['total']} = {accuracy:.2%}")
    
    print(f"\nOverall Accuracy: {total_correct}/{total_problems} = {total_correct/total_problems:.2%}")

if __name__ == "__main__":
    main()