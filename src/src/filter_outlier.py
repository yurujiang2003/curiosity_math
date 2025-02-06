import torch
import json
from transformers import AutoTokenizer, AutoModel
from typing import List, Dict, Tuple
from tqdm import tqdm
import numpy as np
from scipy import stats
from torch.nn.parallel import DataParallel

class ResponseFilter:
    def __init__(self, model_name: str = "BAAI/bge-large-en-v1.5", outlier_ratio: float = 0.2, 
                 min_responses: int = 5, batch_size: int = 32, min_length: int = 20):
        """
        初始化过滤器
        
        Args:
            model_name: 用于生成embedding的模型名称
            outlier_ratio: 要选取的离群值比例（0-1之间）
            min_responses: 最小回答数量
            batch_size: 批处理大小
            min_length: 最小回答长度（字符数）
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        if torch.cuda.device_count() > 1:
            self.model = DataParallel(self.model)
        self.model.eval()
        self.outlier_ratio = outlier_ratio
        self.min_responses = min_responses
        self.batch_size = batch_size
        self.min_length = min_length

    def filter_short_responses(self, responses: List[str]) -> Tuple[List[str], List[int]]:
        """
        过滤掉过短的回答
        
        Args:
            responses: 原始回答列表
            
        Returns:
            Tuple[List[str], List[int]]: 过滤后的回答列表和对应的原始索引
        """
        filtered = [(i, resp) for i, resp in enumerate(responses) if len(resp) >= self.min_length]
        if not filtered:
            return [], []
        indices, valid_responses = zip(*filtered)
        return list(valid_responses), list(indices)

    def get_embeddings_batch(self, texts: List[str]) -> torch.Tensor:
        """批量获取文本的embeddings"""
        all_embeddings = []
        
        for i in range(0, len(texts), self.batch_size):
            batch_texts = texts[i:i + self.batch_size]
            with torch.no_grad(), torch.cuda.amp.autocast():
                inputs = self.tokenizer(
                    batch_texts, 
                    padding=True, 
                    truncation=True, 
                    max_length=512, 
                    return_tensors="pt"
                ).to(self.device)
                
                outputs = self.model(**inputs)
                embeddings = outputs.last_hidden_state.mean(dim=1)
                embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)
                all_embeddings.append(embeddings)
        
        return torch.cat(all_embeddings, dim=0)

    def compute_similarities(self, embeddings: torch.Tensor, mean_embedding: torch.Tensor) -> torch.Tensor:
        """计算所有embeddings与平均embedding的余弦相似度"""
        return torch.nn.functional.cosine_similarity(embeddings, mean_embedding.expand(embeddings.size(0), -1), dim=1)

    def find_outliers(self, responses: List[str]) -> Tuple[List[str], List[int], List[float]]:
        """
        找出离群回答
        
        Args:
            responses: 回答列表
            
        Returns:
            Tuple[List[str], List[int], List[float]]: 离群回答、对应的索引和Z-score值
        """
        # 先过滤掉过短的回答
        valid_responses, valid_indices = self.filter_short_responses(responses)
        
        if len(valid_responses) < self.min_responses:
            return [], [], []

        # 批量获取embeddings
        embeddings = self.get_embeddings_batch(valid_responses)
        
        # 计算平均embedding
        mean_embedding = embeddings.mean(dim=0, keepdim=True)
        
        # 批量计算相似度
        similarities = self.compute_similarities(embeddings, mean_embedding)
        
        # 转移到CPU进行后续处理
        similarities = similarities.cpu().numpy()
        
        # 计算Z-scores并排序
        z_scores = stats.zscore(similarities)
        # 按Z-score绝对值从大到小排序
        sorted_indices = np.argsort(np.abs(z_scores))[::-1]
        
        # 选择前N个作为outliers，N由outlier_ratio决定
        num_outliers = max(1, int(len(valid_responses) * self.outlier_ratio))
        outlier_local_indices = sorted_indices[:num_outliers].tolist()
        
        # 将局部索引转换为原始索引
        outlier_global_indices = [valid_indices[i] for i in outlier_local_indices]
        outlier_responses = [responses[i] for i in outlier_global_indices]
        outlier_z_scores = [float(z_scores[i]) for i in outlier_local_indices]
        
        return outlier_responses, outlier_global_indices, outlier_z_scores

def main():
    # 清理GPU内存
    torch.cuda.empty_cache()
    
    input_file = "/home/shangbin/curiosity_math/many_times_results/merged_responses.json"
    output_file = "/home/shangbin/curiosity_math/many_times_results/merged_responses_filtered.json"
    
    # 配置参数
    model_name = "BAAI/bge-large-en-v1.5"
    batch_size = 32
    outlier_ratio = 0.2  # 取前20%作为outliers
    min_responses = 5    # 至少需要5个回答才进行处理
    min_length = 50     # 最小回答长度
    
    print(f"Using {torch.cuda.device_count()} GPUs")
    print(f"Reading from: {input_file}")
    
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    filter = ResponseFilter(
        model_name=model_name, 
        outlier_ratio=outlier_ratio,
        min_responses=min_responses,
        batch_size=batch_size,
        min_length=min_length
    )
    results = []
    
    # 处理每个问题
    for result in tqdm(data["results"], desc="Finding outliers"):
        responses = result["responses"]
        outlier_responses, outlier_indices, outlier_z_scores = filter.find_outliers(responses)
        
        results.append({
            "question": result["question"],
            "outliers": [
                {
                    "response": resp,
                    "index": idx,
                    "z_score": z_score
                }
                for resp, idx, z_score in zip(outlier_responses, outlier_indices, outlier_z_scores)
            ],
            "original_count": len(responses),
            "outlier_count": len(outlier_responses),
            "type": result.get("type", ""),
            "level": result.get("level", "")
        })
    
    # 保存结果
    print(f"Writing to: {output_file}")
    with open(output_file, 'w') as f:
        json.dump({
            "metadata": {
                **data["metadata"],
                "outlier_ratio": outlier_ratio,
                "min_responses": min_responses,
                "min_length": min_length
            },
            "results": results
        }, f, indent=2)
    
    # 打印统计信息
    total_responses = sum(r["original_count"] for r in results)
    total_outliers = sum(r["outlier_count"] for r in results)
    print(f"Total responses: {total_responses}")
    print(f"Total outliers: {total_outliers}")
    print(f"Outlier rate: {total_outliers/total_responses*100:.2f}%")

if __name__ == "__main__":
    main()