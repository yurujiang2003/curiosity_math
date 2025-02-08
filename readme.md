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
EmbeddingSimilarityFilter（基于嵌入相似度的过滤）
这种方法基于文本嵌入的余弦相似度和Z分数来识别异常值。其数学公式如下：
1) 首先计算所有响应的嵌入向量 $E_i$
2) 计算平均嵌入向量：
$\mu_E = \frac{1}{n}\sum_{i=1}^n E_i$
3) 计算每个响应与平均嵌入的余弦相似度：
$sim_i = \frac{E_i \cdot \mu_E}{||E_i|| \cdot ||\mu_E||}$
4) 计算相似度的Z分数：
$z_i = \frac{sim_i - \mu_{sim}}{\sigma_{sim}}$
其中 $\mu_{sim}$ 是所有相似度的平均值，$\sigma_{sim}$ 是标准差
5) 根据 |z| 值的大小排序，选择最大的 k 个作为异常值（k = n × outlier_ratio）
LikelihoodFilter（基于似然的过滤）
这种方法基于语言模型计算的对数似然来识别异常值。其数学公式如下：
1) 对于每个文本序列，计算其平均对数似然：
$L_i = \frac{1}{T}\sum_{t=1}^T \log P(x_t|x_{<t})$
其中：
T 是序列长度
$x_t$ 是第 t 个词元
$P(x_t|x_{<t})$ 是模型预测下一个词元的概率
2) 计算似然的Z分数：
$z_i = \frac{L_i - \mu_L}{\sigma_L}$
其中 $\mu_L$ 是所有似然的平均值，$\sigma_L$ 是标准差
3) 根据 z 值：
选择 z 值最小的 k 个作为异常值（低似然）
选择 z 值最大的 k 个作为常见响应（高似然）
其中 k = n × outlier_ratio
两种方法的主要区别：
EmbeddingSimilarityFilter 关注的是响应的语义相似度，找出与平均语义差异最大的响应
LikelihoodFilter 关注的是响应的生成概率，找出模型认为最不可能/最可能生成的响应
