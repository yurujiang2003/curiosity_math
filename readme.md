# CuriosityMath

## Motivation
How to trigger LLMs' curiosity to solve math problems in a much more novel way? We use incontext learning to create a prompt that can trigger LLMs' curiosity. 

### Prolog
Convert the response of the LLM to a prolog format. to verify the correctness of the solution, and could be easily standardized those responses.
Cleaned solution is used to sft model.

### Sft model:
1. label the solution correct or not (we wish the final model can be novel and correct)
2. no label (we wish the final model can be novel)

Compare the common solution and the novel solution in the prolog format, to show the difference in the complexity of the solutions.

### Novel or not?
If a novel solution is correct, and which is a outlier in the distribution of the common solutions, then we can say it is a novel solution.

## Pipeline

base_model download and save
    Qwen2.5-Math-7B
    Qwen2.5-Math-72B
    NuminaMath-7B-TIR

dataset download and save:
    FrontierMath: https://arxiv.org/pdf/2411.04872(extremely challenging)
    OlympiadBench: https://arxiv.org/html/2402.14008
    OmniMath: https://arxiv.org/pdf/2410.07985
    MATH Level 5 & MetaMath

## Simple statics results

### 1. Basic Prompt
![alt text](readme_src/f1490774a61fecb99e116a36b8f851e.png)

### 2. Incontext Learning
![alt text](readme_src/0d8d253577f0f95721871b183edceae.png)

### 3. Eazy Prompt
![alt text](readme_src/e95a33b7211b9ae5175715226a41b11.png)
