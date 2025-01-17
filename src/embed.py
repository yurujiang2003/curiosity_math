import torch
import json
from transformers import AutoTokenizer, AutoModel
from torch.nn.functional import kl_div
import numpy as np
from typing import List, Dict, Tuple
from tqdm import tqdm

class ResponseAnalyzer:
    def __init__(self, model_name: str = "BAAI/bge-large-en-v1.5"):
        """
        初始化分析器
        
        Args:
            model_name: 用于生成embedding的模型名称
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.model.eval()

    def get_embedding(self, text: str) -> torch.Tensor:
        """
        获取文本的embedding
        
        Args:
            text: 输入文本
        
        Returns:
            torch.Tensor: 文本的embedding向量
        """
        with torch.no_grad():
            inputs = self.tokenizer(
                text, 
                padding=True, 
                truncation=True, 
                max_length=512, 
                return_tensors="pt"
            ).to(self.device)
            
            outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1)  # [1, hidden_size]
            # 归一化
            embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)
            
            return embeddings.cpu()

    def calculate_kl_divergence(
        self, 
        p_dist: torch.Tensor, 
        q_dist: torch.Tensor
    ) -> float:
        """
        计算两个分布的KL散度
        
        Args:
            p_dist: 第一个分布
            q_dist: 第二个分布
            
        Returns:
            float: KL散度值
        """
        # 确保输入是概率分布
        p_dist = torch.softmax(p_dist, dim=-1)
        q_dist = torch.softmax(q_dist, dim=-1)
        
        return kl_div(
            q_dist.log(), 
            p_dist, 
            reduction='batchmean'
        ).item()

    def analyze_responses(
        self,
        responses: Dict[str, Dict[int, Dict[str, str]]],
        response_type: str = "common_response"
    ) -> Dict[str, Dict[str, float]]:
        """
        分析每个问题的所有回答
        
        Args:
            responses: 按问题和重复次数组织的回答
            response_type: 分析哪种类型的回答 ("common_response" 或 "novel_response")
            
        Returns:
            Dict: 每个问题的分析结果
        """
        results = {}
        
        for problem, repeats in tqdm(responses.items(), desc="Analyzing problems"):
            # 收集这个问题的所有回答
            problem_responses = [
                repeat[response_type] 
                for repeat in repeats.values()
            ]
            
            # 获取所有回答的embeddings
            embeddings = torch.cat([
                self.get_embedding(response) 
                for response in problem_responses
            ])
            
            # 计算平均embedding
            mean_embedding = embeddings.mean(dim=0, keepdim=True)
            
            # 计算每个回答与平均值的KL散度
            kl_divergences = [
                self.calculate_kl_divergence(emb.unsqueeze(0), mean_embedding)
                for emb in embeddings
            ]
            
            # 计算统计信息
            results[problem] = {
                "mean_kl": float(np.mean(kl_divergences)),
                "std_kl": float(np.std(kl_divergences)),
                "min_kl": float(np.min(kl_divergences)),
                "max_kl": float(np.max(kl_divergences)),
                "num_responses": len(problem_responses)
            }
            
        return results

def main():
    # 加载数据
    output_dir = "/home/shangbin/curiosity_math/many_times_results"
    analyzer = ResponseAnalyzer()
    
    for difficulty in ["easy", "medium", "hard"]:
        print(f"\nAnalyzing {difficulty} problems...")
        
        try:
            # 加载响应数据
            with open(f"{output_dir}/{difficulty}/responses.json", 'r') as f:
                data = json.load(f)
            
            responses = data["responses"]
            
            # 分析common和novel响应
            for response_type in ["common_response", "novel_response"]:
                print(f"\nAnalyzing {response_type}...")
                results = analyzer.analyze_responses(responses, response_type)
                
                # 保存结果
                output_file = f"{output_dir}/{difficulty}/kl_divergence_{response_type}.json"
                with open(output_file, 'w') as f:
                    json.dump({
                        "metadata": {
                            "difficulty": difficulty,
                            "response_type": response_type,
                            "model_name": data["metadata"]["model_name"],
                            "num_problems": data["metadata"]["num_problems"],
                            "num_repeats": data["metadata"]["num_repeats"]
                        },
                        "results": results
                    }, f, indent=2)
                
                # 打印汇总统计
                kl_values = [r["mean_kl"] for r in results.values()]
                print(f"Average KL divergence: {np.mean(kl_values):.4f}")
                print(f"Std KL divergence: {np.std(kl_values):.4f}")
                
        except Exception as e:
            print(f"Error processing {difficulty}: {e}")
            continue

if __name__ == "__main__":
    main()