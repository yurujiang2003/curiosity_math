import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def compare_accuracies(json_file1, json_file2, output_dir):
    """
    比较两个JSON文件中的准确率并生成对比图
    
    Args:
        json_file1: 第一个JSON文件路径
        json_file2: 第二个JSON文件路径
        output_dir: 输出图片保存目录
    """
    # 读取JSON文件
    with open(json_file1, 'r') as f:
        data1 = json.load(f)
    with open(json_file2, 'r') as f:
        data2 = json.load(f)
    
    # 计算每个level和type的准确率
    def calculate_metrics(data):
        level_stats = {}
        type_stats = {}
        
        for item in data:
            level = item['level']
            prob_type = item['type']
            is_correct = int(item['is_correct'])
            
            # 统计level
            if level not in level_stats:
                level_stats[level] = {'correct': 0, 'total': 0}
            level_stats[level]['correct'] += is_correct
            level_stats[level]['total'] += 1
            
            # 统计type
            if prob_type not in type_stats:
                type_stats[prob_type] = {'correct': 0, 'total': 0}
            type_stats[prob_type]['correct'] += is_correct
            type_stats[prob_type]['total'] += 1
        
        # 计算准确率
        level_acc = {k: v['correct']/v['total'] for k, v in level_stats.items()}
        type_acc = {k: v['correct']/v['total'] for k, v in type_stats.items()}
        
        return level_acc, type_acc
    
    # 获取两个文件的统计数据
    level_acc1, type_acc1 = calculate_metrics(data1)
    level_acc2, type_acc2 = calculate_metrics(data2)
    
    # 创建对比图
    def plot_comparison(acc1, acc2, title, filename):
        # 准备数据
        categories = sorted(set(acc1.keys()) | set(acc2.keys()))
        df = pd.DataFrame({
            'Category': categories * 2,
            'Accuracy': [acc1.get(c, 0) for c in categories] + [acc2.get(c, 0) for c in categories],
            'Model': ['Base Qwen'] * len(categories) + ['Novel Qwen'] * len(categories)
        })
        
        # 设置图形样式
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Category', y='Accuracy', hue='Model', data=df)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # 保存图片
        plt.savefig(f"{output_dir}/{filename}.png")
        plt.close()
    
    # 生成level和type的对比图
    plot_comparison(level_acc1, level_acc2, 'Accuracy Comparison by Level', 'level_comparison')
    plot_comparison(type_acc1, type_acc2, 'Accuracy Comparison by Type', 'type_comparison')
    
    # 返回统计数据
    return {
        'level_accuracies': {
            'model1': level_acc1,
            'model2': level_acc2
        },
        'type_accuracies': {
            'model1': type_acc1,
            'model2': type_acc2
        }
    }

if __name__ == "__main__":
    compare_accuracies("/home/shangbin/outputs/20250203_090608/all_results.json", "/home/shangbin/outputs/20250203_090616/all_results.json", "/home/shangbin/curiosity_math")
