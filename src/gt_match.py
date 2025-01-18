from typing import List, Dict
import re
import json
from difflib import SequenceMatcher
from sentence_transformers import SentenceTransformer
import torch
import numpy as np

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

def flexible_match(text1: str, text2: str) -> bool:
    """
    Perform a flexible match between two texts.
    """
    # Clean and tokenize the texts
    tokens1 = set(clean_math_text(text1).lower().split())
    tokens2 = set(clean_math_text(text2).lower().split())
    
    # Calculate the intersection of tokens
    intersection = tokens1.intersection(tokens2)
    
    # Define a threshold for flexible matching
    threshold = 0.5  # 50% of the tokens should match
    
    # Calculate the match ratio
    match_ratio = len(intersection) / max(len(tokens1), len(tokens2))
    
    return match_ratio >= threshold

def calculate_embedding_similarity(text1: str, text2: str, model_name: str = "all-MiniLM-L6-v2", gpu_id: int = 0) -> float:
    """
    使用文本嵌入计算两个文本的相似度
    
    Args:
        text1: 第一个文本
        text2: 第二个文本
        model_name: sentence-transformer模型名称
        gpu_id: GPU设备ID
    
    Returns:
        float: 相似度分数 (0-1)
    """
    try:
        device = torch.device(f"cuda:{gpu_id}" if torch.cuda.is_available() else "cpu")
        
        # 加载模型（第一次调用时会下载模型）
        model = SentenceTransformer(model_name)
        model = model.to(device)
        
        # 获取文本嵌入
        embedding1 = model.encode(
            [clean_math_text(text1)], 
            convert_to_tensor=True,
            device=device
        )
        embedding2 = model.encode(
            [clean_math_text(text2)], 
            convert_to_tensor=True,
            device=device
        )
        
        # 计算余弦相似度
        cosine_similarity = torch.nn.functional.cosine_similarity(embedding1, embedding2)
        
        return float(cosine_similarity[0])  # 转换为Python float
        
    except Exception as e:
        print(f"Error calculating embedding similarity: {e}")
        return 0.0

def evaluate_responses(data: Dict, gpu_id: int = 0) -> Dict:
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
    
    # 计算字符串相似度
    common_similarity = calculate_similarity(solution_answer, common_answer)
    novel_similarity = calculate_similarity(solution_answer, novel_answer)
    
    # 计算embedding相似度
    common_embedding_similarity = calculate_embedding_similarity(
        solution_answer, 
        common_answer,
        gpu_id=gpu_id
    )
    novel_embedding_similarity = calculate_embedding_similarity(
        solution_answer, 
        novel_answer,
        gpu_id=gpu_id
    )
    
    # Perform flexible match
    common_flexible_match = flexible_match(solution_answer, common_answer)
    novel_flexible_match = flexible_match(solution_answer, novel_answer)
    
    return {
        'problem': data['problem'],
        'solution_answer': solution_answer,
        'common_answer': common_answer,
        'novel_answer': novel_answer,
        'common_similarity': common_similarity,
        'novel_similarity': novel_similarity,
        'common_embedding_similarity': common_embedding_similarity,
        'novel_embedding_similarity': novel_embedding_similarity,
        'common_flexible_match': common_flexible_match,
        'novel_flexible_match': novel_flexible_match
    }

def process_file(input_file: str, gpu_id: int = 0) -> Dict:
    """
    处理整个文件并计算统计数据
    """
    total_problems = 0
    common_matches = 0
    novel_matches = 0
    
    # 添加相似度累计变量
    total_common_similarity = 0.0
    total_novel_similarity = 0.0
    total_common_embedding_similarity = 0.0
    total_novel_embedding_similarity = 0.0
    
    results = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                result = evaluate_responses(data, gpu_id=gpu_id)
                results.append(result)
                
                total_problems += 1
                if result['common_similarity'] > 0.8:  # 设置相似度阈值
                    common_matches += 1
                if result['novel_similarity'] > 0.8:
                    novel_matches += 1
                
                # 累加相似度
                total_common_similarity += result['common_similarity']
                total_novel_similarity += result['novel_similarity']
                total_common_embedding_similarity += result['common_embedding_similarity']
                total_novel_embedding_similarity += result['novel_embedding_similarity']
                    
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON line: {e}")
    
    # 计算平均相似度
    avg_common_similarity = total_common_similarity / total_problems if total_problems > 0 else 0
    avg_novel_similarity = total_novel_similarity / total_problems if total_problems > 0 else 0
    avg_common_embedding_similarity = total_common_embedding_similarity / total_problems if total_problems > 0 else 0
    avg_novel_embedding_similarity = total_novel_embedding_similarity / total_problems if total_problems > 0 else 0
    
    stats = {
        'total_problems': total_problems,
        'common_accuracy': common_matches / total_problems if total_problems > 0 else 0,
        'novel_accuracy': novel_matches / total_problems if total_problems > 0 else 0,
        'avg_common_similarity': avg_common_similarity,
        'avg_novel_similarity': avg_novel_similarity,
        'avg_common_embedding_similarity': avg_common_embedding_similarity,
        'avg_novel_embedding_similarity': avg_novel_embedding_similarity,
        'detailed_results': results
    }
    
    return stats

# 使用示例
if __name__ == "__main__":
    input_file = "curiosity_math/Qwen2.5-7B-Instruct_responses_easy_ICL_ground_truth.json"
    gpu_id = 0  # 使用第一个GPU
    
    stats = process_file(input_file, gpu_id=gpu_id)
    
    print(f"Total problems processed: {stats['total_problems']}")
    print(f"Common response accuracy: {stats['common_accuracy']:.2%}")
    print(f"Novel response accuracy: {stats['novel_accuracy']:.2%}")
    print(f"Average common similarity: {stats['avg_common_similarity']:.4f}")
    print(f"Average novel similarity: {stats['avg_novel_similarity']:.4f}")
    print(f"Average common embedding similarity: {stats['avg_common_embedding_similarity']:.4f}")
    print(f"Average novel embedding similarity: {stats['avg_novel_embedding_similarity']:.4f}")
    
    # 保存详细结果
    output_file = "curiosity_math/evaluation/gt/Qwen2.5-7B-Instruct_responses_easy_ICL_gt_match.json"
    
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)