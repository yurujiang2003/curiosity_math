def get_base_prompt(problem: dict) -> str:
    return f"""
Here is the problem:

Problem: {problem['problem']}
"""

def get_common_prompt(problem: dict) -> str:
    base_prompt = get_base_prompt(problem)
    return """Please solve the problem commonly.
""" + base_prompt

def get_novel_prompt(problem: dict) -> str:
    base_prompt = get_base_prompt(problem)
    return """Here is an example of problems with both novel and common solutions(Your are not required to answer them):
**Problem**: There are 35 animals (chickens and rabbits) in a cage with 94 legs in total. How many chickens and rabbits are there?

**Common Solution**:  
Let \( x \) be the number of chickens and \( y \) be the number of rabbits. Set up the system of equations:
\[
\begin{cases}
x + y = 35 \\
2x + 4y = 94
\end{cases}
\]
Solve the system to find \( x = 23 \) (chickens) and \( y = 12 \) (rabbits).

**Novel Solution**:  
Assume all animals are chickens. Then the total number of legs would be \( 35 \times 2 = 70 \), which is 24 legs fewer than the actual count. Each time a chicken is replaced with a rabbit, the number of legs increases by 2. Therefore, \( 24 \div 2 = 12 \) replacements are needed, resulting in 12 rabbits and \( 35 - 12 = 23 \) chickens.

Note: Above is just an example teaching you to think out of box. You donot need to answer them. Your task is to answer the following problem.
""" + base_prompt

SYSTEM_PROMPT = "You are a math assistant who can solve problems well." 
