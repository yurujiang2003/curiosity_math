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
    # Remove whitespace and convert to lowercase
    answer = answer.strip().lower()
    
    # Remove LaTeX formatting
    answer = answer.replace('\\', '')
    answer = answer.replace('boxed{', '')
    answer = answer.replace('}', '')
    
    # Normalize fractions
    answer = answer.replace('\\frac', '')
    
    # Normalize square roots
    answer = answer.replace('\\sqrt', 'sqrt')
    
    # Remove extra spaces
    answer = ' '.join(answer.split())
    
    return answer

def normalize_spacing(text):
    """
    标准化文本中的空格和格式
    """
    try:
        # 移除所有空白字符（空格、制表符、换行符等）
        text = ''.join(text.split())
        
        # 标准化常见的分隔符
        separators = {
            '，': ',',  # 中文逗号转英文逗号
            '；': ';',  # 中文分号转英文分号
            '：': ':',  # 中文冒号转英文冒号
            '（': '(',  # 中文括号转英文括号
            '）': ')',
            '［': '[',  # 中文方括号转英文方括号
            '］': ']',
            '｛': '{',  # 中文花括号转英文花括号
            '｝': '}',
            '　': '',   # 中文空格删除
            ' ': '',    # 英文空格删除
            '\t': '',   # 制表符删除
            '\n': '',   # 换行符删除
            '\r': '',   # 回车符删除
        }
        
        for old, new in separators.items():
            text = text.replace(old, new)
        
        return text
    except Exception as e:
        print(f"Error in normalize_spacing: {e}")
        return text

def check_mathematical_equivalence(expr1, expr2):
    """
    检查两个数学表达式是否等价
    """
    try:
        # 移除所有空格
        expr1 = expr1.replace(' ', '')
        expr2 = expr2.replace(' ', '')
        
        # 如果字符串完全相同，直接返回True
        if expr1 == expr2:
            return True
            
        # 处理分数
        def convert_fraction(expr):
            # 将分数转换为小数
            if 'over' in expr:
                try:
                    num, den = expr.split('over')
                    num = num.replace('negative', '-')
                    return float(num) / float(den)
                except:
                    return None
            # 处理带分数，如 "1 1/2" 转换为 1.5
            parts = expr.split()
            if len(parts) == 2 and '/' in parts[1]:
                try:
                    whole = float(parts[0])
                    num, den = parts[1].split('/')
                    return whole + float(num) / float(den)
                except:
                    return None
            # 处理普通分数 "1/2"
            if '/' in expr:
                try:
                    num, den = expr.split('/')
                    return float(num) / float(den)
                except:
                    return None
            return None
            
        # 处理百分数
        def convert_percentage(expr):
            if expr.endswith('%'):
                try:
                    return float(expr[:-1]) / 100
                except:
                    return None
            return None
            
        # 处理科学记数法
        def convert_scientific(expr):
            if 'e' in expr.lower():
                try:
                    return float(expr)
                except:
                    return None
            return None
            
        # 处理根号
        def convert_sqrt(expr):
            if 'sqrt' in expr:
                try:
                    # 提取根号内的数字
                    num = expr.replace('sqrt', '').strip('()')
                    return float(num) ** 0.5
                except:
                    return None
            return None
            
        # 尝试将表达式转换为数值并比较
        def try_numeric_conversion(expr):
            # 尝试各种转换方法
            methods = [
                float,  # 普通数字
                convert_fraction,  # 分数
                convert_percentage,  # 百分数
                convert_scientific,  # 科学记数法
                convert_sqrt  # 根号
            ]
            
            for method in methods:
                try:
                    result = method(expr)
                    if result is not None:
                        return result
                except:
                    continue
            return None
            
        # 尝试数值比较
        val1 = try_numeric_conversion(expr1)
        val2 = try_numeric_conversion(expr2)
        
        if val1 is not None and val2 is not None:
            # 使用相对误差进行比较
            rel_tol = 1e-9  # 相对误差容限
            abs_tol = 1e-9  # 绝对误差容限
            return abs(val1 - val2) <= max(rel_tol * max(abs(val1), abs(val2)), abs_tol)
            
        # 处理集合等价性
        def normalize_set(expr):
            if expr.startswith('{') and expr.endswith('}'):
                elements = expr[1:-1].split(',')
                return sorted(elem.strip() for elem in elements)
            return None
            
        # 检查集合等价性
        set1 = normalize_set(expr1)
        set2 = normalize_set(expr2)
        if set1 is not None and set2 is not None:
            return set1 == set2
            
        # 处理区间等价性
        def normalize_interval(expr):
            if (expr.startswith('[') or expr.startswith('(')) and (expr.endswith(']') or expr.endswith(')')):
                bounds = expr[1:-1].split(',')
                if len(bounds) == 2:
                    return (expr[0], [float(b.strip()) for b in bounds], expr[-1])
            return None
            
        # 检查区间等价性
        interval1 = normalize_interval(expr1)
        interval2 = normalize_interval(expr2)
        if interval1 is not None and interval2 is not None:
            return interval1 == interval2
        
        return False
        
    except Exception as e:
        print(f"Error in check_mathematical_equivalence: {e}")
        return False

def are_answers_equivalent(pred, target):
    """Check if predicted answer is equivalent to target answer."""
    try:
        # 标准化两个答案
        pred = normalize_answer(pred)
        target = normalize_answer(target)
        
        # 基本相等性检查
        if pred == target:
            return True
            
        # 检查数学等价性
        if check_mathematical_equivalence(pred, target):
            return True
            
        return False
        
    except Exception as e:
        print(f"Error in are_answers_equivalent: {e}")
        return False

def extract_answer(response):
    """Extract and normalize answer from response."""
    if "\\boxed" in response:
        try:
            start = response.index("\\boxed{") + 7
            end = response.index("}", start)
            return normalize_answer(response[start:end])
        except:
            pass
    return normalize_answer(response)

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

def extract_all_boxed_answers(response):
    """Extract all boxed answers from the response."""
    answers = []
    try:
        # 找到所有 \boxed{...} 的位置
        current_pos = 0
        while True:
            # 查找下一个 \boxed
            boxed_start = response.find("\\boxed", current_pos)
            if boxed_start == -1:
                break
                
            # 找到左花括号
            brace_start = response.find("{", boxed_start)
            if brace_start == -1:
                break
                
            # 计算嵌套的花括号
            count = 1
            pos = brace_start + 1
            while count > 0 and pos < len(response):
                if response[pos] == "{":
                    count += 1
                elif response[pos] == "}":
                    count -= 1
                pos += 1
                
            if count == 0:
                # 提取并标准化答案
                answer = response[brace_start + 1:pos - 1]
                normalized_answer = normalize_answer(answer)
                if normalized_answer:  # 只添加非空答案
                    answers.append(normalized_answer)
                    
            current_pos = pos
            
        # 如果没有找到任何 boxed 答案，将整个响应作为答案
        if not answers:
            normalized_response = normalize_answer(response)
            if normalized_response:
                answers.append(normalized_response)
                
    except Exception as e:
        print(f"Error extracting boxed answers: {e}")
        # 发生错误时，尝试将整个响应作为答案
        try:
            normalized_response = normalize_answer(response)
            if normalized_response:
                answers.append(normalized_response)
        except:
            pass
            
    return answers

def are_any_answers_equivalent(pred_answers, target_answer):
    """Check if any of the predicted answers matches the target answer."""
    for pred in pred_answers:
        if are_answers_equivalent(pred, target_answer):
            return True
    return False

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
        predicted_answers = extract_all_boxed_answers(model_response)
        ground_truth = extract_answer(problem['solution'])
        
        # 检查是否有任何一个预测答案与正确答案匹配
        is_correct = are_any_answers_equivalent(predicted_answers, ground_truth)
        correct += int(is_correct)
        
        if not args.save_incorrect_only or not is_correct:
            result = {
                "problem": problem['problem'],
                "ground_truth": problem['solution'],
                "ground_truth_answer": ground_truth,
                "model_response": model_response,
                "predicted_answers": predicted_answers,
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