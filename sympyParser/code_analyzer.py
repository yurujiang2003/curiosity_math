import os
import ast
import time
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import re
import signal
from contextlib import contextmanager

class TimeoutException(Exception):
    pass

@contextmanager
def time_limit(seconds):
    """超时控制的上下文管理器"""
    def signal_handler(signum, frame):
        raise TimeoutException("代码执行超时")
    
    # 设置信号处理器
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    
    try:
        yield
    finally:
        # 重置信号处理器
        signal.alarm(0)

class CodeAnalyzer:
    def __init__(self, code_path: str = "code"):
        self.code_path = Path(code_path)
        self.results = []
        # 设置matplotlib的警告阈值
        plt.rcParams['figure.max_open_warning'] = 50  # 增加警告阈值
        
    def count_sympy_imports(self, code: str) -> int:
        """统计sympy导入的模块数量"""
        tree = ast.parse(code)
        count = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == 'sympy':
                count += len(node.names)
            elif isinstance(node, ast.Import):
                for name in node.names:
                    if 'sympy' in name.name:
                        count += 1
        return count
    
    def count_complexity(self, code: str) -> Dict[str, int]:
        """分析代码复杂度"""
        tree = ast.parse(code)
        loops = len([node for node in ast.walk(tree) 
                    if isinstance(node, (ast.For, ast.While))])
        conditions = len([node for node in ast.walk(tree) 
                        if isinstance(node, ast.If)])
        variables = len([node for node in ast.walk(tree) 
                        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store)])
        
        return {
            'loops': loops,
            'conditions': conditions,
            'variables': variables
        }
    
    def measure_execution_time(self, code: str, timeout: int = 5) -> float:
        """测量代码执行时间，设置超时限制"""
        try:
            # 创建一个包含必要导入的执行环境
            setup_code = """
from sympy import *
from sympy.abc import *
import sympy
"""
            # 准备执行环境
            exec_globals = {}
            exec(setup_code, exec_globals)
            
            # 使用超时控制执行代码
            start_time = time.time()
            try:
                with time_limit(timeout):
                    exec(code, exec_globals)
                execution_time = time.time() - start_time
                return execution_time
            except TimeoutException:
                print(f"执行超时 ({timeout}s) {self.current_file}")
                return -1
            
        except Exception as e:
            print(f"执行错误 {self.current_file}: {str(e)}")
            return -1
    
    def analyze_file_pair(self, common_file: Path, novel_file: Path) -> Dict:
        """分析一对文件的差异"""
        # 保存完整的文件路径
        self.current_file = str(common_file.absolute())
        with open(common_file, 'r') as f:
            common_code = f.read()
        
        self.current_file = str(novel_file.absolute())
        with open(novel_file, 'r') as f:
            novel_code = f.read()
            
        common_metrics = {
            'type': 'common',
            'file': common_file.name,
            'code_length': len(common_code),
            'sympy_imports': self.count_sympy_imports(common_code),
            'execution_time': self.measure_execution_time(common_code),
            **self.count_complexity(common_code)
        }
        
        novel_metrics = {
            'type': 'novel',
            'file': novel_file.name,
            'code_length': len(novel_code),
            'sympy_imports': self.count_sympy_imports(novel_code),
            'execution_time': self.measure_execution_time(novel_code),
            **self.count_complexity(novel_code)
        }
        
        return {'common': common_metrics, 'novel': novel_metrics}
    
    def plot_comparison(self, metrics: List[Dict], save_path: str):
        """生成对比图表"""
        df = pd.DataFrame(metrics)
        
        # 使用默认样式而不是seaborn
        plt.style.use('default')
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Common vs Novel Solution Comparison', fontsize=16)
        
        # 绘制各项指标的对比图
        metrics_to_plot = [
            ('code_length', 'Code Length'),
            ('sympy_imports', 'SymPy Imports'),
            ('execution_time', 'Execution Time (s)'),
            ('loops', 'Loop Count'),
            ('conditions', 'Condition Count'),
            ('variables', 'Variable Count')
        ]
        
        for (metric, title), ax in zip(metrics_to_plot, axes.flat):
            # 使用普通的柱状图而不是seaborn
            ax.bar(df['type'], df[metric])
            ax.set_title(title)
            ax.set_xlabel('')
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
    
    def aggregate_statistics(self):
        """聚合所有结果的统计数据"""
        all_metrics = []
        for result in self.results:
            all_metrics.extend([result['common'], result['novel']])
        
        df = pd.DataFrame(all_metrics)
        # 添加类别和难度级别列
        df['category'] = df['file'].apply(lambda x: x.split('_')[0])
        df['level'] = df['file'].apply(lambda x: int(x.split('_')[1]))
        return df

    def plot_overall_comparison(self, df: pd.DataFrame, save_path: str):
        """绘制整体对比图"""
        metrics = ['code_length', 'sympy_imports', 'execution_time', 'loops', 'conditions', 'variables']
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Overall Common vs Novel Solution Comparison', fontsize=16)
        
        for metric, ax in zip(metrics, axes.flat):
            means = df.groupby('type')[metric].mean()
            errors = df.groupby('type')[metric].std()
            ax.bar(means.index, means.values, yerr=errors.values, capsize=5)
            ax.set_title(f'Average {metric.replace("_", " ").title()}')
            ax.set_ylabel('Value')
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def plot_category_comparison(self, df: pd.DataFrame, save_path: str):
        """绘制不同类别的对比图"""
        metrics = ['code_length', 'sympy_imports', 'execution_time', 'loops', 'conditions', 'variables']
        
        for metric in metrics:
            plt.figure(figsize=(12, 6))
            means = df.groupby(['category', 'type'])[metric].mean().unstack()
            means.plot(kind='bar', yerr=df.groupby(['category', 'type'])[metric].std().unstack(), capsize=5)
            plt.title(f'{metric.replace("_", " ").title()} by Category')
            plt.xlabel('Category')
            plt.ylabel('Value')
            plt.xticks(rotation=45)
            plt.legend(title='Solution Type')
            plt.tight_layout()
            plt.savefig(f"{save_path}/category_{metric}.png")
            plt.close('all')  # 关闭所有图表

    def plot_level_comparison(self, df: pd.DataFrame, save_path: str):
        """绘制不同难度级别的对比图"""
        metrics = ['code_length', 'sympy_imports', 'execution_time', 'loops', 'conditions', 'variables']
        
        for metric in metrics:
            plt.figure(figsize=(12, 6))
            means = df.groupby(['level', 'type'])[metric].mean().unstack()
            means.plot(kind='bar', yerr=df.groupby(['level', 'type'])[metric].std().unstack(), capsize=5)
            plt.title(f'{metric.replace("_", " ").title()} by Difficulty Level')
            plt.xlabel('Level')
            plt.ylabel('Value')
            plt.legend(title='Solution Type')
            plt.tight_layout()
            plt.savefig(f"{save_path}/level_{metric}.png")
            plt.close()

    def plot_category_level_comparison(self, df: pd.DataFrame, save_path: str):
        """绘制类别和难度级别的详细对比图"""
        metrics = ['code_length', 'sympy_imports', 'execution_time', 'loops', 'conditions', 'variables']
        
        for category in df['category'].unique():
            category_df = df[df['category'] == category]
            
            for metric in metrics:
                plt.figure(figsize=(12, 6))
                means = category_df.groupby(['level', 'type'])[metric].mean().unstack()
                means.plot(kind='bar', 
                          yerr=category_df.groupby(['level', 'type'])[metric].std().unstack(), 
                          capsize=5)
                plt.title(f'{category} - {metric.replace("_", " ").title()} by Level')
                plt.xlabel('Level')
                plt.ylabel('Value')
                plt.legend(title='Solution Type')
                plt.tight_layout()
                plt.savefig(f"{save_path}/{category}_level_{metric}.png")
                plt.close()

    def analyze_all(self):
        """分析所有配对的文件并生成统计图表"""
        for category in os.listdir(self.code_path):
            category_path = self.code_path / category
            if not category_path.is_dir():
                continue
                
            common_path = category_path / 'common'
            novel_path = category_path / 'novel'
            
            if not (common_path.exists() and novel_path.exists()):
                continue
                
            for common_file in common_path.glob('*.py'):
                novel_file = novel_path / common_file.name
                if novel_file.exists():
                    metrics = self.analyze_file_pair(common_file, novel_file)
                    self.results.append(metrics)
                    
                    # 为每对文件生成单独的对比图
                    plot_path = self.code_path / 'analysis' / category / f'{common_file.stem}_comparison.png'
                    plot_path.parent.mkdir(parents=True, exist_ok=True)
                    self.plot_comparison([metrics['common'], metrics['novel']], str(plot_path))

        # 生成统计数据
        df = self.aggregate_statistics()
        
        # 创建分析结果目录
        analysis_path = self.code_path / 'analysis'
        analysis_path.mkdir(parents=True, exist_ok=True)
        
        # 生成不同层次的对比图
        self.plot_overall_comparison(df, str(analysis_path / 'overall_comparison.png'))
        self.plot_category_comparison(df, str(analysis_path))
        self.plot_level_comparison(df, str(analysis_path))
        self.plot_category_level_comparison(df, str(analysis_path))
        
        # 生成统计报告
        self.generate_statistics_report(df, analysis_path / 'statistics_report.txt')

    def generate_statistics_report(self, df: pd.DataFrame, save_path: str):
        """生成详细的统计报告"""
        with open(save_path, 'w') as f:
            # 整体统计
            f.write("Overall Statistics:\n")
            f.write("=" * 50 + "\n")
            f.write(df.groupby('type').describe().to_string())
            f.write("\n\n")
            
            # 按类别统计
            f.write("Statistics by Category:\n")
            f.write("=" * 50 + "\n")
            f.write(df.groupby(['category', 'type']).describe().to_string())
            f.write("\n\n")
            
            # 按难度级别统计
            f.write("Statistics by Level:\n")
            f.write("=" * 50 + "\n")
            f.write(df.groupby(['level', 'type']).describe().to_string())

def main():
    analyzer = CodeAnalyzer()
    analyzer.analyze_all()

if __name__ == "__main__":
    main() 