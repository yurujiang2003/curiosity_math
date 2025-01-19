import os
import json
from typing import List, Dict
import logging
from pathlib import Path
import random
from util import run_chatopenai
from prompts import get_common_prompt, get_novel_prompt, SYSTEM_PROMPT
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MathPairSolver:
    def __init__(self, base_path: str = "datasets/MATH/test"):
        self.base_path = Path(base_path)
        self.categories = [
            "algebra",
            "counting_and_probability",
            "geometry",
            "intermediate_algebra",
            "number_theory",
            "prealgebra",
            "precalculus"
        ]

    def read_problem(self, file_path: Path) -> Dict:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"读取文件 {file_path} 时出错: {str(e)}")
            return None

    def process_single_problem(self, args):
        """处理单个问题的函数"""
        problem_data, category, save_path, index, level = args
        try:
            common_response = run_chatopenai(
                system_prompt=SYSTEM_PROMPT,
                user_prompt=get_common_prompt(problem_data),
                temperature=0.7
            )
            
            novel_response = run_chatopenai(
                system_prompt=SYSTEM_PROMPT,
                user_prompt=get_novel_prompt(problem_data),
                temperature=0.7
            )
            
            result = {
                "category": category,
                "problem_id": str(index),
                "problem": problem_data['problem'],
                "level": problem_data['level'],
                "type": problem_data['type'],
                "original_solution": problem_data['solution'],
                "common_answer": common_response,
                "novel_answer": novel_response
            }

            # 修改保存路径逻辑
            filename = f"{level.replace(' ', '_')}_{index}.json"
            save_file = os.path.join(save_path, filename)  # 移除category
            os.makedirs(os.path.dirname(save_file), exist_ok=True)
            
            with open(save_file, 'w') as f:
                json.dump(result, f, indent=4)
            
            logger.info(f"完成处理 {category}/{level} - Case {index}")
            return result
        except Exception as e:
            logger.error(f"处理问题时出错: {str(e)}")
            return None

    def process_category(self, category: str, save_path: str, casenumber: int) -> List[Dict]:
        """处理单个类别的所有问题"""
        category_path = self.base_path / category
        
        if not category_path.exists():
            logger.error(f"类别路径不存在: {category_path}")
            return []

        # 收集所有问题并按level分组
        problems_by_level = {f"Level {i}": [] for i in range(1, 6)}
        
        for file_name in category_path.glob("*.json"):
            problem_data = self.read_problem(file_name)
            if problem_data:
                problems_by_level[problem_data['level']].append(problem_data)

        # 准备并行处理的任务
        tasks = []
        for level, problems in problems_by_level.items():
            if not problems:
                continue
                
            selected_problems = random.sample(problems, min(casenumber, len(problems)))
            for i, problem in enumerate(selected_problems, 1):
                tasks.append((problem, category, save_path, i, level))

        # 使用进程池并行处理
        num_processes = min(multiprocessing.cpu_count(), len(tasks))
        logger.info(f"启动 {num_processes} 个进程处理 {category} 类别的问题...")
        
        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            results = list(executor.map(self.process_single_problem, tasks))
            
        return [r for r in results if r is not None]

    def process_all_categories(self, save_path: str, casenumber: int) -> Dict[str, List[Dict]]:
        """处理所有类别的问题"""
        all_results = {}
        
        for category in self.categories:
            logger.info(f"开始处理类别: {category}")
            results = self.process_category(category, os.path.join(save_path, category), casenumber)
            all_results[category] = results
            logger.info(f"完成类别 {category} 的处理，共处理 {len(results)} 个问题")

        return all_results

def main():
    casenumber = 10
    solver = MathPairSolver()
    results = solver.process_all_categories("response", casenumber)

if __name__ == "__main__":
    main()