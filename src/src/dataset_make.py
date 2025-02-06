import pandas as pd
import json
import random
from typing import List, Dict
import os
from collections import defaultdict

def process_data(input_file: str, output_file: str) -> List[Dict]:
    """convert raw json to jsonl for supervides fine-tuning
    
    Args:
        input_file: path to the raw json file
        output_file: path to the output jsonl file
        
    Returns:
        processed data list
    """
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # 处理数据
    processed_data = []
    for item in data['results']:
        response = random.choice(item['responses'])
        message = [
            {"role": "user", "content": item['question']},
            {"role": "assistant", "content": response}
        ]
        processed_data.append({"message": message})

    # save as jsonl
    processed_df = pd.DataFrame(processed_data)
    processed_df.to_json(output_file, orient='records', lines=True, force_ascii=False)
    
    print(f"Processed {len(processed_data)} samples from {os.path.basename(input_file)}")
    return processed_data

class GroundTruthDatasetMaker:
    def __init__(self, base_dir: str):
        """Initialize dataset maker
        
        Args:
            base_dir: base directory containing Level_X folders
        """
        self.base_dir = base_dir
        self.types = ["Algebra", "Counting & Probability", "Geometry", "Intermediate Algebra", 
                     "Number Theory", "Prealgebra", "Precalculus"]
        self.levels = [f"Level_{i}" for i in range(1, 6)]
        
        # Create input and output file paths
        self.input_files = []
        for level in self.levels:
            for type_ in self.types:
                self.input_files.append(
                    os.path.join(self.base_dir, level, f"{type_}.json")
                )
                
        # Create output file path (single output file)
        self.output_file = os.path.join(self.base_dir, "math_dataset_sft.jsonl")
        
    def process_data_with_balance(self, input_file: str, samples_per_type: int = 20) -> List[Dict]:
        """Process data ensuring equal samples per type
        
        Args:
            input_file: path to the input json file
            samples_per_type: number of samples to select for each type
            
        Returns:
            List of processed samples
        """
        with open(input_file, 'r') as f:
            data = json.load(f)
            
        # Group problems by type
        type_questions = defaultdict(list)
        for problem in data['problems']:
            type_questions[problem['type']].append(problem)
            
        # Process data with balanced sampling
        processed_data = []
        for type_name, questions in type_questions.items():
            # Sample questions if we have more than needed
            if len(questions) > samples_per_type:
                selected_questions = random.sample(questions, samples_per_type)
            else:
                selected_questions = questions
                print(f"Warning: Only {len(questions)} samples available for {type_name}")
                
            # Process selected questions
            for item in selected_questions:
                message = [
                    {"role": "user", "content": item['problem']},
                    {"role": "assistant", "content": item['solution']}
                ]
                processed_data.append({
                    "message": message,
                    "type": item['type'],
                    "level": item['level']
                })
                
        return processed_data
        
    def make_dataset(self, samples_per_type: int = 20) -> None:
        """Process all level files and create corresponding jsonl files with balanced samples"""
        total_samples = 0
        all_processed_data = []
        
        # Process each level and type combination
        for input_file in self.input_files:
            if not os.path.exists(input_file):
                print(f"Warning: {input_file} does not exist")
                continue
                
            try:
                processed_data = self.process_data_with_balance(
                    input_file, 
                    samples_per_type=samples_per_type
                )
                all_processed_data.extend(processed_data)
                total_samples += len(processed_data)
                
                # Print statistics for this file
                print(f"Processed {len(processed_data)} samples from {os.path.basename(input_file)}")
                    
            except Exception as e:
                print(f"Error processing {os.path.basename(input_file)}: {str(e)}")
                continue
        
        # Save all processed data to single output file
        if all_processed_data:
            processed_df = pd.DataFrame(all_processed_data)
            processed_df.to_json(self.output_file, orient='records', lines=True, force_ascii=False)
            print(f"\nSaved {len(all_processed_data)} total samples to {self.output_file}")
                
        print(f"\nTotal processed samples: {total_samples}")
        
        # Print overall statistics
        level_counts = defaultdict(int)
        type_counts = defaultdict(int)
        for item in all_processed_data:
            level_counts[item['level']] += 1
            type_counts[item['type']] += 1
            
        print("\nOverall samples per level:")
        for level, count in level_counts.items():
            print(f"{level}: {count}")
            
        print("\nOverall samples per type:")
        for type_name, count in type_counts.items():
            print(f"{type_name}: {count}")

class OutlierFilter(GroundTruthDatasetMaker):
    def __init__(self, base_dir: str, output_dir: str, outlier_ratio: float = 0.2, min_responses: int = 5, batch_size: int = 32, min_length: int = 20):
        """Initialize outlier filter
        
        Args:
            base_dir: 输入文件目录
            output_dir: 输出文件目录
            outlier_ratio: outlier比例
            min_responses: 最小回答数
            batch_size: 批处理大小
            min_length: 最小回答长度
        """
        super().__init__(base_dir)
        self.outlier_ratio = outlier_ratio
        self.min_responses = min_responses
        self.batch_size = batch_size
        self.min_length = min_length
        # 覆盖基类的输出文件路径
        self.output_file = os.path.join(output_dir, "math_outliers_dataset.jsonl")
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        # 更新输入文件路径
        self.input_files = [os.path.join(base_dir, "merged_responses_filtered.json")]
        
    def process_data_with_balance(self, input_file: str, samples_per_type: int = 20) -> List[Dict]:
        """处理所有outlier QA对，每个问题随机选择一个outlier response
        
        Args:
            input_file: 输入的outlier json文件路径
            samples_per_type: 未使用，保持与基类接口一致
            
        Returns:
            List[Dict]: 处理后的数据列表
        """
        with open(input_file, 'r') as f:
            data = json.load(f)
            
        processed_data = []
        
        # 处理每个问题
        for result in data['results']:
            if not result.get("outliers"):  # 跳过没有outliers的问题
                continue
                
            # 随机选择一个outlier
            outlier = random.choice(result["outliers"])
            message = [
                {"role": "user", "content": result["question"]},
                {"role": "assistant", "content": outlier["response"]}
            ]
            
            processed_data.append({
                "message": message
            })
        
        return processed_data

    def make_dataset(self, samples_per_type: int = 20) -> None:
        """Process outlier files and create jsonl files"""
        total_samples = 0
        all_processed_data = []
        
        # Process each input file
        for input_file in self.input_files:
            if not os.path.exists(input_file):
                print(f"Warning: {input_file} does not exist")
                continue
                
            try:
                processed_data = self.process_data_with_balance(
                    input_file, 
                    samples_per_type=samples_per_type
                )
                all_processed_data.extend(processed_data)
                total_samples += len(processed_data)
                
                # Print statistics for this file
                print(f"Processed {len(processed_data)} samples from {os.path.basename(input_file)}")
                    
            except Exception as e:
                print(f"Error processing {os.path.basename(input_file)}: {str(e)}")
                continue
        
        # Save all processed data to single output file
        if all_processed_data:
            processed_df = pd.DataFrame(all_processed_data)
            processed_df.to_json(self.output_file, orient='records', lines=True, force_ascii=False)
            print(f"\nSaved {len(all_processed_data)} total samples to {self.output_file}")
                
        print(f"\nTotal processed samples: {total_samples}")

def main():
    input_dir = "/home/shangbin/curiosity_math/many_times_results"
    output_dir = "/home/shangbin/curiosity_math/datasets"
    
    filter = OutlierFilter(
        base_dir=input_dir,
        output_dir=output_dir
    )
    filter.make_dataset()

if __name__ == "__main__":
    main()