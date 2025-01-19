import os
import json
from typing import List, Dict
import logging
from pathlib import Path
from util import run_chatopenai
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import re

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_code_prompt(solution_type: str, problem: str, solution: str) -> str:
    return f"""
Convert this {solution_type} solution of the math problem to executable SymPy code.

Problem: {problem}

Solution: {solution}

Please write Python code that:
1. Uses SymPy library to implement this {solution_type} solution approach
2. Start with imports (from sympy import ...)
3. Includes necessary variable definitions
4. return the final answer
5. Don't include any comments before the imports

Return ONLY the code, no explanations.
"""

def clean_code_response(code_response: str) -> str:
    """清理和格式化API返回的代码"""
    # 移除可能的markdown代码块标记
    code = code_response.replace("```python", "").replace("```", "").strip()
    
    # 使用正则表达式找到第一个import语句
    import_match = re.search(r'^from\s+sympy\s+import|^import\s+sympy', code, re.MULTILINE)
    if not import_match:
        return code  # 如果没有找到import语句，返回原始代码
    
    # 只保留从import开始的代码
    code = code[import_match.start():]
    
    # 移除代码中的Note、Example等注释
    code = re.sub(r'^Note:.*$\n?', '', code, flags=re.MULTILINE)
    code = re.sub(r'^Example:.*$\n?', '', code, flags=re.MULTILINE)
    
    # 移除多余的空行，但保留最多两个连续的空行
    code = re.sub(r'\n\s*\n\s*\n', '\n\n', code)
    
    # 移除行首和行尾的空白字符
    code = '\n'.join(line.rstrip() for line in code.splitlines())
    
    # 确保代码以换行结束
    if not code.endswith('\n'):
        code += '\n'
    
    return code

def verify_code(code: str) -> bool:
    """验证生成的代码是否符合要求"""
    # 检查是否以sympy导入开始
    if not code.strip().startswith(('from sympy', 'import sympy')):
        return False
    
    # 检查是否包含问题描述或注释
    if '# Problem:' in code or 'Note:' in code:
        return False
    
    # 检查是否只包含有效的Python代码
    try:
        compile(code, '<string>', 'exec')
        return True
    except SyntaxError:
        return False

class Math2CodeConverter:
    def __init__(self, response_path: str = "response", code_path: str = "code"):
        self.response_path = Path(response_path)
        self.code_path = Path(code_path)
        self.categories = [
            "algebra",
            "counting_and_probability",
            "geometry",
            "intermediate_algebra",
            "number_theory",
            "prealgebra",
            "precalculus"
        ]

    def read_response(self, file_path: Path) -> Dict:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"读取文件 {file_path} 时出错: {str(e)}")
            return None

    def process_single_problem(self, args):
        """将单个问题转换为代码，分别保存常规和创新解法"""
        problem_data, category, save_path, filename = args
        try:
            # 获取常规解法的代码
            common_code = run_chatopenai(
                system_prompt="You are a Python programmer expert in using SymPy for mathematical computations.",
                user_prompt=get_code_prompt("common", problem_data['problem'], problem_data['common_answer']),
                temperature=0.3
            )
            
            # 获取创新解法的代码
            novel_code = run_chatopenai(
                system_prompt="You are a Python programmer expert in using SymPy for mathematical computations.",
                user_prompt=get_code_prompt("novel", problem_data['problem'], problem_data['novel_answer']),
                temperature=0.3
            )
            
            # 清理和验证代码
            common_code = clean_code_response(common_code)
            novel_code = clean_code_response(novel_code)
            
            if not verify_code(common_code) or not verify_code(novel_code):
                logger.error(f"生成的代码验证失败: {filename}")
                return None
            
            # 分别保存两种解法
            base_filename = filename.replace('.json', '.py')
            
            # 保存常规解法
            common_path = os.path.join(save_path, 'common')
            os.makedirs(common_path, exist_ok=True)
            with open(os.path.join(common_path, base_filename), 'w', encoding='utf-8') as f:
                f.write(f"{common_code}")
            
            # 保存创新解法
            novel_path = os.path.join(save_path, 'novel')
            os.makedirs(novel_path, exist_ok=True)
            with open(os.path.join(novel_path, base_filename), 'w', encoding='utf-8') as f:
                f.write(f"{novel_code}")
            
            logger.info(f"完成转换 {category}/{filename}")
            return True
        except Exception as e:
            logger.error(f"处理问题时出错: {str(e)}")
            return None

    def process_category(self, category: str):
        """处理单个类别的所有问题"""
        response_category_path = self.response_path / category
        
        if not response_category_path.exists():
            logger.error(f"类别路径不存在: {response_category_path}")
            return []

        # 收集所有问题
        tasks = []
        for file_name in response_category_path.glob("*.json"):
            problem_data = self.read_response(file_name)
            if problem_data:
                save_path = self.code_path / category
                tasks.append((problem_data, category, save_path, file_name.name))

        # 使用进程池并行处理
        num_processes = min(multiprocessing.cpu_count(), len(tasks))
        logger.info(f"启动 {num_processes} 个进程处理 {category} 类别的问题...")
        
        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            results = list(executor.map(self.process_single_problem, tasks))
            
        return [r for r in results if r is not None]

    def process_all_categories(self):
        """处理所有类别的问题"""
        for category in self.categories:
            logger.info(f"开始处理类别: {category}")
            results = self.process_category(category)
            logger.info(f"完成类别 {category} 的处理，共处理 {len(results)} 个问题")

def main():
    converter = Math2CodeConverter()
    converter.process_all_categories()

if __name__ == "__main__":
    main()
