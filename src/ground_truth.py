import os
import json
from pathlib import Path
from typing import Dict, List

def find_solution_by_problem(directory: str, target_problem: str) -> str:
    """
    在指定目录下搜索包含目标问题的JSON文件并提取其解决方案
    
    Args:
        directory (str): 要搜索的目录路径
        target_problem (str): 要查找的问题文本
    
    Returns:
        str: 找到的解决方案，如果没找到返回None
    """
    # 规范化问题文本，移除多余的空白字符
    target_problem = ' '.join(target_problem.split())
    
    # 递归搜索所有JSON文件
    for path in Path(directory).rglob('*.json'):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # 规范化文件中的问题文本
                if 'problem' in data:
                    file_problem = ' '.join(data['problem'].split())
                    
                    # 比较问题文本
                    if file_problem == target_problem:
                        return data.get('solution')
                        
        except Exception as e:
            print(f"Error processing {path}: {e}")
            continue
            
    return None


def process_questions_with_solutions(input_file: str, math_dir: str) -> List[Dict]:
    """
    处理包含多个问题的文件，为每个问题匹配解决方案
    
    Args:
        input_file (str): 输入文件路径，包含多个问题的JSON行
        math_dir (str): MATH数据集目录路径
    
    Returns:
        List[Dict]: 包含问题和解决方案的字典列表
    """
    results = []
    
    # 读取文件中的每一行
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                # 解析JSON行
                data = json.loads(line.strip())
                
                if 'problem' in data:
                    # 查找对应的解决方案
                    solution = find_solution_by_problem(math_dir, data['problem'])
                    
                    # 创建结果字典
                    result = {
                        'problem': data['problem'],
                        'solution': solution,
                        'common_response': data.get('common_response'),
                        'novel_response': data.get('novel_response')
                    }
                    
                    results.append(result)
                    
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON line: {e}")
            except Exception as e:
                print(f"Error processing line: {e}")
                
    return results

def save_results(results: List[Dict], output_file: str):
    """
    保存处理结果到文件
    
    Args:
        results (List[Dict]): 处理结果
        output_file (str): 输出文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for result in results:
            json.dump(result, f, ensure_ascii=False)
            f.write('\n')

# 使用示例
if __name__ == "__main__":

    input_files = ["curiosity_math/Qwen2.5-7B-Instruct_responses_easy_ICL.json",
                   "curiosity_math/Qwen2.5-7B-Instruct_responses_medium_ICL.json",
                   "curiosity_math/Qwen2.5-7B-Instruct_responses_hard_ICL.json"]
    math_dir = "curiosity_math/datasets/MATH"

    for input_file in input_files:
        output_file = input_file.replace(".json", "_ground_truth.json")
        
        # 处理问题并匹配解决方案
        results = process_questions_with_solutions(input_file, math_dir)
        
        # 保存结果
        save_results(results, output_file)
        
        print(f"Processed {len(results)} questions and saved results to {output_file}")