import os
import json
from typing import List, Tuple


def load_data(file_path: str) -> List[Tuple[str, List[str]]]:
    """
    Load and parse evaluation data from JSON file
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        list: List of (question, responses) tuples
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    qa_pairs = []
    for item in data['results']:
        question = item['question']
        responses = item.get('responses', [])
        qa_pairs.append((question, responses))
        
    return qa_pairs

def get_metadata(file_path: str):
    """
    Get metadata from the evaluation file
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        dict: Metadata dictionary
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.get('metadata', {})

if __name__ == "__main__":
    file_path = "/Users/tintin/Desktop/curiosity_math/all_responses_100_times.json"
    qa_pairs = load_data(file_path)
    print(qa_pairs[0])
