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
