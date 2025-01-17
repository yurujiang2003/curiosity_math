import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_results(file_path):
    """加载JSON结果文件"""
    with open(file_path, 'r') as f:
        return json.load(f)

def create_comparison_plot(results_dict, output_path):
    """创建对比可视化图"""
    # 设置样式
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # 创建图形
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # 准备数据
    difficulties = list(results_dict.keys())
    metrics = {
        'Accuracy': {
            'Common': [d['common_accuracy'] for d in results_dict.values()],
            'Novel': [d['novel_accuracy'] for d in results_dict.values()]
        },
        'Similarity': {
            'Common String': [d['avg_common_similarity'] for d in results_dict.values()],
            'Novel String': [d['avg_novel_similarity'] for d in results_dict.values()],
            'Common Embedding': [d['avg_common_embedding_similarity'] for d in results_dict.values()],
            'Novel Embedding': [d['avg_novel_embedding_similarity'] for d in results_dict.values()]
        }
    }
    
    # 绘制准确率对比
    x = np.arange(len(difficulties))
    width = 0.35
    
    ax1.bar(x - width/2, metrics['Accuracy']['Common'], width, label='Common Response')
    ax1.bar(x + width/2, metrics['Accuracy']['Novel'], width, label='Novel Response')
    
    ax1.set_ylabel('Accuracy')
    ax1.set_title('Accuracy Comparison Across Difficulties')
    ax1.set_xticks(x)
    ax1.set_xticklabels(difficulties)
    ax1.legend()
    
    # 在柱状图上添加具体数值
    for i, v in enumerate(metrics['Accuracy']['Common']):
        ax1.text(i - width/2, v, f'{v:.2%}', ha='center', va='bottom')
    for i, v in enumerate(metrics['Accuracy']['Novel']):
        ax1.text(i + width/2, v, f'{v:.2%}', ha='center', va='bottom')
    
    # 绘制相似度对比
    markers = ['o', 's', '^', 'D']
    for (label, values), marker in zip(metrics['Similarity'].items(), markers):
        ax2.plot(difficulties, values, marker=marker, label=label, linewidth=2, markersize=8)
    
    ax2.set_ylabel('Similarity Score')
    ax2.set_title('Similarity Scores Comparison Across Difficulties')
    ax2.legend()
    ax2.grid(True)
    
    # 在线上添加具体数值
    for label, values in metrics['Similarity'].items():
        for i, v in enumerate(values):
            ax2.text(i, v, f'{v:.3f}', ha='center', va='bottom')
    
    # 调整布局
    plt.tight_layout()
    
    # 保存图片
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # 加载三个难度的结果
    results = {
        'Easy': load_results('curiosity_math/evaluation/gt/Qwen2.5-7B-Instruct_responses_easy_ICL_gt_match.json'),
        'Medium': load_results('curiosity_math/evaluation/gt/Qwen2.5-7B-Instruct_responses_medium_ICL_gt_match.json'),
        'Hard': load_results('curiosity_math/evaluation/gt/Qwen2.5-7B-Instruct_responses_hard_ICL_gt_match.json')
    }
    
    # 创建可视化
    create_comparison_plot(results, 'curiosity_math/evaluation/gt/comparison_plot.png')
    
    # 打印详细数据表格
    print("\nDetailed Results:")
    print("-" * 80)
    print(f"{'Difficulty':<10} {'Common Acc':>12} {'Novel Acc':>12} {'Common Sim':>12} {'Novel Sim':>12} {'Common Emb':>12} {'Novel Emb':>12}")
    print("-" * 80)
    
    for diff, data in results.items():
        print(f"{diff:<10} {data['common_accuracy']:>11.2%} {data['novel_accuracy']:>11.2%} "
              f"{data['avg_common_similarity']:>11.3f} {data['avg_novel_similarity']:>11.3f} "
              f"{data['avg_common_embedding_similarity']:>11.3f} {data['avg_novel_embedding_similarity']:>11.3f}")