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

| Model | gsm8k | minerva_math | svamp | asdiv | mawps | tabmwp | mathqa | mmlu_stem | sat_math | avg |
|---------|-------|--------------|-------|-------|-------|---------|---------|-----------|-----------|-----|
| Qwen-Math-7B (base) | 84.6 | 56.4 | 87.4 | 91.2 | 95.9 | 65.9 | 36.4 | 69.0 | 93.8 | 75.6 |
| Qwen-Math-7B (100) | 84.6 | 56.2 | 87.5 | 91.2 | 95.8 | 65.8 | 33.5 | 68.9 | 93.8 | 75.3 |
| Qwen-Math-7B (215) | 84.5 | 55.8 | 87.6 | 91.3 | 95.9 | 65.7 | 29.2 | 68.9 | 93.8 | 74.7 |
| Qwen-Math-7B (215 gt) | 84.4 | 56.2 | 87.7 | 91.4 | 95.9 | 65.9 | 26.6 | 68.8 | 93.8 | 74.5 |