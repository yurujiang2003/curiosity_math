from typing import List, Dict
import re
import json
from difflib import SequenceMatcher

def clean_math_text(text: str) -> str:
    """
    清理数学文本，移除LaTeX标记等
    """
    # 移除LaTeX标记
    text = re.sub(r'\$+', '', text)
    # 移除换行符和多余空格
    text = ' '.join(text.split())
    return text

def extract_final_answer(text: str) -> str:
    """
    提取最终答案（通常在boxed中或Answer:后面）
    """
    # 尝试找到boxed中的答案
    boxed_match = re.search(r'\\boxed{([^}]+)}', text)
    if boxed_match:
        return clean_math_text(boxed_match.group(1))
    
    # 尝试找到"Answer:"后面的内容
    answer_match = re.search(r'Answer:\s*([^\n]+)', text)
    if answer_match:
        return clean_math_text(answer_match.group(1))
    
    return clean_math_text(text)

def calculate_similarity(text1: str, text2: str) -> float:
    """
    计算两个文本的相似度
    """
    return SequenceMatcher(None, text1, text2).ratio()

def evaluate_responses(data: Dict) -> Dict:
    """
    评估common_response和novel_response与solution的匹配程度
    """
    solution = data.get('solution', '')
    common_response = data.get('common_response', '')
    novel_response = data.get('novel_response', '')
    
    # 提取答案
    solution_answer = extract_final_answer(solution)
    common_answer = extract_final_answer(common_response)
    novel_answer = extract_final_answer(novel_response)
    
    # 计算相似度
    common_similarity = calculate_similarity(solution_answer, common_answer)
    novel_similarity = calculate_similarity(solution_answer, novel_answer)
    
    return {
        'problem': data['problem'],
        'solution_answer': solution_answer,
        'common_answer': common_answer,
        'novel_answer': novel_answer,
        'common_similarity': common_similarity,
        'novel_similarity': novel_similarity
    }

def process_file(input_file: str) -> Dict:
    """
    处理整个文件并计算统计数据
    """
    total_problems = 0
    common_matches = 0
    novel_matches = 0
    results = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                result = evaluate_responses(data)
                results.append(result)
                
                total_problems += 1
                if result['common_similarity'] > 0.8:  # 设置相似度阈值
                    common_matches += 1
                if result['novel_similarity'] > 0.8:
                    novel_matches += 1
                    
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON line: {e}")
    
    stats = {
        'total_problems': total_problems,
        'common_accuracy': common_matches / total_problems if total_problems > 0 else 0,
        'novel_accuracy': novel_matches / total_problems if total_problems > 0 else 0,
        'detailed_results': results
    }
    
    return stats

# 使用示例
if __name__ == "__main__":
    input_file = "curiosity_math/prompt_ICL/qwen_2.5b_math_response_ICL_ground_truth.json"
    stats = process_file(input_file)
    
    print(f"Total problems processed: {stats['total_problems']}")
    print(f"Common response accuracy: {stats['common_accuracy']:.2%}")
    print(f"Novel response accuracy: {stats['novel_accuracy']:.2%}")    
    # 保存详细结果
    output_file = "curiosity_math/evaluation/gt/qwen_2.5b_math_response_ICL.json"
    
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)