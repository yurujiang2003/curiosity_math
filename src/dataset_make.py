import pandas as pd
import json
import random
from typing import List, Dict
import os

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

def main():
    # 定义输入输出文件路径
    base_dir = '/home/shangbin/curiosity_math/many_times_results'
    input_files = [
        os.path.join(base_dir, f'level{i}_responses_20_times_outliers.json')
        for i in range(1, 6)
    ]
    
    output_files = [
        os.path.join(base_dir, f'level{i}_responses_20_times_outliers_sft.jsonl')
        for i in range(1, 6)
    ]

    # 处理所有文件
    total_samples = 0
    for input_file, output_file in zip(input_files, output_files):
        try:
            processed_data = process_data(input_file, output_file)
            total_samples += len(processed_data)
        except Exception as e:
            print(f"Error processing {os.path.basename(input_file)}: {str(e)}")
            continue

    print(f"\nTotal processed samples: {total_samples}")

if __name__ == "__main__":
    main()