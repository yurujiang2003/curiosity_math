# CuriosityMath

## Motivation
How to trigger LLMs' curiosity to solve math problems in a much more novel way? We use incontext learning to create a prompt that can trigger LLMs' curiosity. 

### SymPy code language
Convert the response of the LLM to a SymPy code language. to verify the correctness of the solution, and could be easily standardized those responses.
Cleaned solution is used to sft model.

### Sft model:
1. label the solution correct or not (we wish the final model can be novel and correct)
2. no label (we wish the final model can be novel)

Compare the common solution and the novel solution in the prolog format, to show the difference in the complexity of the solutions.

### Novel or not?
If a novel solution is correct, and which is a outlier in the distribution of the common solutions, then we can say it is a novel solution.

### Evaluation

| Model | Common | Novel | GT | Likelihood | gsm8k | minerva_math | svamp | asdiv | mawps | tabmwp | mathqa | mmlu_stem | sat_math | avg  |
|-------|---------|--------|-----|------------|-------|--------------|-------|-------|-------|--------|--------|-----------|----------|------|
| Qwen-Math-7B | | | | | 84.6 | 56.4 | 87.4 | 91.2 | 95.9 | 65.9 | 36.4 | 69.0 | 93.8 | 75.6 |
| Qwen-Math-7B | ✓ | | | | 84.8 | 55.6 | 87.5 | 91.4 | 95.9 | 65.9 | 32.2 | 68.8 | 93.8 | 75.1 |
| Qwen-Math-7B | | ✓ | | | 84.5 | 55.8 | 87.6 | 91.3 | 95.9 | 65.7 | 29.2 | 68.9 | 93.8 | 74.7 |
| Qwen-Math-7B | | | ✓ | | 84.4 | 56.2 | 87.7 | 91.4 | 95.9 | 65.9 | 26.6 | 68.8 | 93.8 | 74.5 |
| Qwen-Math-7B | ✓ | | | ✓ | 84.6 | 56.0 | 87.5 | 91.4 | 95.8 | 65.9 | 28.7 | 68.8 | 93.8 | 74.7 |
| Qwen-Math-7B | | ✓ | | ✓ | 84.2 | 55.2 | 87.4 | 91.2 | 95.9 | 66.0 | 33.8 | 68.9 | 93.8 | 75.2 |

### Explaination
以下是两种方法的数学表达式说明：

### 一、基于嵌入相似度的离群检测 (Embedding Similarity)
1. **嵌入向量计算**：
   - 输入文本序列：T = [t₁, t₂, ..., tₙ]
   - 通过Transformer模型获得上下文嵌入：
     $$
     \mathbf{E} = \text{Transformer}(T) \in \mathbb{R}^{n \times d}
     $$
   - 池化操作（平均池化）：
     $$
     \mathbf{\bar{e}} = \frac{1}{n}\sum_{i=1}^{n}\mathbf{E}_i \in \mathbb{R}^d
     $$

2. **相似度计算**：
   - 计算平均嵌入向量：
     $$
     \mathbf{\mu} = \frac{1}{N}\sum_{j=1}^{N}\mathbf{\bar{e}}_j \in \mathbb{R}^d
     $$
   - 余弦相似度计算：
     $$
     \text{sim}_j = \frac{\mathbf{\bar{e}}_j \cdot \mathbf{\mu}}{\|\mathbf{\bar{e}}_j\| \cdot \|\mathbf{\mu}\|}
     $$

3. **离群检测**：
   - 计算Z-score标准化：
     $$
     z_j = \frac{\text{sim}_j - \mu_{\text{sim}}}{\sigma_{\text{sim}}}
     $$
   - 选择绝对值最大的Z-score作为离群值

### 二、基于似然度的离群检测 (Likelihood Filtering)
1. **对数似然计算**：
   - 输入文本序列：T = [w₁, w₂, ..., wₙ]
   - 语言模型输出每个token的概率分布：
     $$
     P(w_i|w_{<i}) = \text{softmax}(\mathbf{h}_i)
     $$
   - 平均对数似然计算：
     $$
     \mathcal{L}(T) = \frac{1}{n}\sum_{i=1}^{n}\log P(w_i|w_{<i})
     $$

2. **离群检测**：
   - 收集所有响应对数似然值：
     $$
     \mathbf{L} = [\mathcal{L}(T_1), \mathcal{L}(T_2), ..., \mathcal{L}(T_N)]
     $$
   - 计算Z-score标准化：
     $$
     z_j = \frac{\mathcal{L}(T_j) - \mu_{\mathbf{L}}}{\sigma_{\mathbf{L}}}
     $$
   - 选择Z-score最低的作为离群值，最高的作为典型样本

### 符号说明
| 符号 | 含义 |
|------|------|
| T    | 输入文本序列 |
| d    | 嵌入维度 |
| N    | 响应数量 |
| n    | 序列长度 |
| μ    | 均值向量/标量 |
| σ    | 标准差 |

两种方法的本质差异：
- 嵌入方法：基于语义空间的几何分布特征
- 似然方法：基于生成模型的概率分布特征
