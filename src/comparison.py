import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import List, Dict, Union
import json
from scipy.stats import entropy
from collections import Counter
import math
import re
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from textstat import textstat
import os

class ResponseAnalyzer:
    def __init__(self):
        """Initialize the analyzer"""
        try:
            nltk.download('punkt', quiet=True)
            nltk.download('punkt_tab', quiet=True)
        except:
            print("Warning: NLTK data download failed")
    
    def analyze_responses(self, common: str, novel: str) -> Dict:
        """Analyze the responses"""
        return {
            "entropy": self._compute_entropy(common, novel),
            "complexity": self._analyze_complexity(common, novel),
            "diversity": self._analyze_diversity(common, novel),
            "math_features": self._analyze_math_features(common, novel)
        }

    def _compute_entropy(self, text1: str, text2: str) -> Dict:
        """Calculate entropy"""
        def get_entropy(text: str, unit: str = 'char') -> float:
            if unit == 'char':
                tokens = list(text.lower())
            else:  # word
                tokens = word_tokenize(text.lower())
            counter = Counter(tokens)
            probs = np.array([count/len(tokens) for count in counter.values()])
            return float(entropy(probs))
        
        return {
            "char_entropy": {
                "common": get_entropy(text1, 'char'),
                "novel": get_entropy(text2, 'char')
            },
            "word_entropy": {
                "common": get_entropy(text1, 'word'),
                "novel": get_entropy(text2, 'word')
            }
        }

    def _analyze_complexity(self, text1: str, text2: str) -> Dict:
        """Analyze text complexity"""
        def get_complexity(text: str) -> Dict:
            return {
                "readability": {
                    "flesch_reading_ease": textstat.flesch_reading_ease(text),
                    "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text)
                },
                "sentence_length": {
                    "mean": np.mean([len(s.split()) for s in sent_tokenize(text)]),
                    "std": np.std([len(s.split()) for s in sent_tokenize(text)])
                }
            }
        
        return {
            "common": get_complexity(text1),
            "novel": get_complexity(text2)
        }

    def _analyze_diversity(self, text1: str, text2: str) -> Dict:
        """Analyze vocabulary diversity"""
        def get_diversity(text: str) -> Dict:
            words = word_tokenize(text.lower())
            unique_words = set(words)
            return {
                "type_token_ratio": len(unique_words) / len(words) if words else 0,
                "unique_words": len(unique_words)
            }
        
        return {
            "common": get_diversity(text1),
            "novel": get_diversity(text2)
        }

    def _analyze_math_features(self, text1: str, text2: str) -> Dict:
        """Analyze mathematical features"""
        def get_math_features(text: str) -> Dict:
            math_symbols = r'[+\-*/=<>≤≥≠∈∉∪∩∀∃∄∑∏∫√π]'
            formulas = r'\$.*?\$'
            return {
                "symbol_density": len(re.findall(math_symbols, text)) / len(text),
                "formula_count": len(re.findall(formulas, text))
            }
        
        return {
            "common": get_math_features(text1),
            "novel": get_math_features(text2)
        }

def process_data_for_visualization(data: Union[str, List[Dict]]) -> Dict:
    """Process either file path or results list into visualization data"""
    metrics = {
        'char_entropy': {'common': [], 'novel': []},
        'word_entropy': {'common': [], 'novel': []},
        'readability_flesch': {'common': [], 'novel': []},
        'type_token_ratio': {'common': [], 'novel': []},
        'math_symbol_density': {'common': [], 'novel': []}
    }
    
    if isinstance(data, str):
        with open(data, 'r') as f:
            results = [json.loads(line) for line in f]
    else:
        results = data
        
    for result in results:
        if isinstance(result, dict) and 'analysis' in result:
            analysis = result['analysis']
            
            # Extract specific numerical values from the nested structure
            metrics['char_entropy']['common'].append(analysis['entropy']['char_entropy']['common'])
            metrics['char_entropy']['novel'].append(analysis['entropy']['char_entropy']['novel'])
            
            metrics['word_entropy']['common'].append(analysis['entropy']['word_entropy']['common'])
            metrics['word_entropy']['novel'].append(analysis['entropy']['word_entropy']['novel'])
            
            metrics['readability_flesch']['common'].append(analysis['complexity']['common']['readability']['flesch_reading_ease'])
            metrics['readability_flesch']['novel'].append(analysis['complexity']['novel']['readability']['flesch_reading_ease'])
            
            metrics['type_token_ratio']['common'].append(analysis['diversity']['common']['type_token_ratio'])
            metrics['type_token_ratio']['novel'].append(analysis['diversity']['novel']['type_token_ratio'])
            
            metrics['math_symbol_density']['common'].append(analysis['math_features']['common']['symbol_density'])
            metrics['math_symbol_density']['novel'].append(analysis['math_features']['novel']['symbol_density'])
    
    return metrics

def visualize_metrics(metrics: Dict, output_dir: str):
    """Create visualizations for the metrics"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Define metric names in English
    metric_names = {
        'char_entropy': 'Character Entropy',
        'word_entropy': 'Word Entropy',
        'readability_flesch': 'Flesch Reading Ease',
        'type_token_ratio': 'Type-Token Ratio',
        'math_symbol_density': 'Math Symbol Density'
    }
    
    # Create subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()
    
    for idx, (metric, name) in enumerate(metric_names.items()):
        if idx >= len(axes):
            break
            
        ax = axes[idx]
        data = [metrics[metric]['common'], metrics[metric]['novel']]
        
        # Create violin plot
        parts = ax.violinplot(data, showmeans=True)
        
        # Add box plot
        bp = ax.boxplot(data, positions=[1, 2], widths=0.2)
        
        # Set style
        for pc in parts['bodies']:
            pc.set_alpha(0.3)
        parts['cmeans'].set_color('red')
        
        # Set labels
        ax.set_title(name)
        ax.set_xticks([1, 2])
        ax.set_xticklabels(['Common', 'Novel'])
        
        # Add grid
        ax.grid(True, linestyle='--', alpha=0.7)
        
    # Remove extra subplots
    for idx in range(len(metric_names), len(axes)):
        fig.delaxes(axes[idx])
    
    # Adjust layout
    plt.tight_layout()
    
    # Save figure
    plt.savefig(os.path.join(output_dir, 'metrics_comparison.png'), dpi=300, bbox_inches='tight')
    plt.close()

def batch_analyze_responses(input_file: str, output_file: str):
    """Analyze responses from input file and save results
    
    Args:
        input_file: Path to input JSON file
        output_file: Path to save analysis results
    """
    analyzer = ResponseAnalyzer()
    results = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            analysis = analyzer.analyze_responses(
                data['common_response'],
                data.get('novel_response', '')  # Handle missing novel responses
            )
            results.append({
                "problem": data['problem'],
                "analysis": analysis
            })
    
    # Save detailed results
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # Generate analysis report
    output_dir = output_file.replace('.json', '_analysis')
    metrics = process_data_for_visualization(results)
    visualize_metrics(metrics, output_dir)

if __name__ == "__main__":
    input_file = "/home/shangbin/curiosity_math/qwen_2.5b_math_responses_medium_ICL.json"
    output_file = "/home/shangbin/curiosity_math/qwen_2.5b_math_responses_medium_ICL_analysis.json"
    batch_analyze_responses(input_file, output_file)