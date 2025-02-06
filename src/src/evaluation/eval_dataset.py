import json
import os
from collections import defaultdict
from tqdm import tqdm

def load_math_data(data_dir):
    """Load MATH dataset and organize by level and type."""
    data_by_category = defaultdict(lambda: defaultdict(list))

    for root, _, files in os.walk(data_dir):
        for file in tqdm(files):
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    level = data.get('level', 'Unknown')
                    problem_type = data.get('type', 'Unknown')

                    data_by_category[level][problem_type].append(data)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return data_by_category

def save_organized_data(data_by_category, output_dir):
    """Save organized data into separate JSON files by level and type."""
    os.makedirs(output_dir, exist_ok=True)

    for level, type_dict in data_by_category.items():
        level_dir = os.path.join(output_dir, level.replace(" ", "_"))
        os.makedirs(level_dir, exist_ok=True)
        
        for problem_type, problems in type_dict.items():
            output_file = os.path.join(level_dir, f"{problem_type}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "level": level,
                    "type": problem_type,
                    "problems": problems
                }, f, indent=2, ensure_ascii=False)

def main():
    # Configure paths
    data_dir = "/home/shangbin/curiosity_math/datasets/MATH/train"
    output_dir = "/home/shangbin/curiosity_math/datasets/organized_math_train"
    
    # Load and organize data
    print("Loading and organizing MATH dataset...")
    data_by_category = load_math_data(data_dir)
    
    # Save organized data
    print("Saving organized data...")
    save_organized_data(data_by_category, output_dir)
    
    # Print statistics
    total_problems = sum(
        len(problems)
        for type_dict in data_by_category.values()
        for problems in type_dict.values()
    )
    print(f"\nTotal problems processed: {total_problems}")
    print("\nProblems by category:")
    for level, type_dict in data_by_category.items():
        print(f"\n{level}:")
        for problem_type, problems in type_dict.items():
            print(f"  {problem_type}: {len(problems)} problems")

if __name__ == "__main__":
    main()