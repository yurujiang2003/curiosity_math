import logging
from typing import Dict, Any, Tuple
from sympy import simplify, expand, Symbol
from sympy.parsing.sympy_parser import parse_expr
import re

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SymPyComparator:
    def __init__(self):
        self.symbol_map = {}
        self.reverse_map = {}
        self.symbol_counter = 0
    
    def _normalize_variables(self, expr_str: str) -> str:
        """
        Standardize the variable names in the expression, so that different variable names can be compared
        """
        # Find all variable names (alphabetic identifiers starting with a letter)
        variables = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', expr_str)
        
        for var in variables:
            if var not in ['sin', 'cos', 'tan', 'exp', 'log', 'sqrt']:  # Skip math function names
                if var not in self.symbol_map:
                    self.symbol_map[var] = f'x_{self.symbol_counter}'
                    self.reverse_map[f'x_{self.symbol_counter}'] = var
                    self.symbol_counter += 1
                expr_str = re.sub(r'\b' + var + r'\b', self.symbol_map[var], expr_str)
                
        return expr_str
    
    def _extract_expressions(self, code: str) -> Dict[str, str]:
        """
        Extract all assignment expressions from the code
        """
        expressions = {}
        lines = code.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                try:
                    var_name, expr = line.split('=', 1)
                    var_name = var_name.strip()
                    expr = expr.strip()
                    if expr:
                        expressions[var_name] = self._normalize_variables(expr)
                except Exception as e:
                    logger.warning(f"Could not parse line: {line}, Error: {e}")
                    
        return expressions
    
    def compare_expressions(self, expr1: str, expr2: str) -> float:
        """
        比较两个表达式的相似度
        """
        try:
            # 首先标准化变量名
            expr1 = self._normalize_variables(expr1)
            expr2 = self._normalize_variables(expr2)
            
            # 解析标准化后的表达式
            parsed1 = parse_expr(expr1)
            parsed2 = parse_expr(expr2)
            
            # 展开并化简
            expanded1 = expand(parsed1)
            expanded2 = expand(parsed2)
            
            # 如果完全相等（考虑到变量已标准化，这应该能捕获等价表达式）
            if expanded1 == expanded2:
                return 1.0
                
            # 计算差异
            diff = simplify(expanded1 - expanded2)
            if diff == 0:
                return 1.0
                
            # 如果结构相同但可能有常数差异
            if str(expanded1.free_symbols) == str(expanded2.free_symbols):
                return 0.9
                
            # 如果基本结构相似（操作符数量相同）
            if str(expanded1).count('+') == str(expanded2).count('+') and \
               str(expanded1).count('*') == str(expanded2).count('*'):
                return 0.7
                
            return 0.0
                
        except Exception as e:
            logger.error(f"Error comparing expressions: {e}")
            return 0.0
    
    def compare_codes(self, code1: str, code2: str) -> Tuple[float, Dict[str, float]]:
        """
        比较两段代码的相似度
        """
        try:
            # 重置映射
            self.symbol_map = {}
            self.symbol_counter = 0
            
            # 提取表达式
            expr1 = self._extract_expressions(code1)
            expr2 = self._extract_expressions(code2)
            
            # 计算每个表达式的相似度
            similarities = {}
            total_similarity = 0.0
            matched_pairs = 0
            
            # 为每个表达式找到最佳匹配
            for var1, exp1 in expr1.items():
                best_similarity = 0.0
                best_match = None
                
                for var2, exp2 in expr2.items():
                    similarity = self.compare_expressions(exp1, exp2)
                    if similarity > best_similarity:
                        best_similarity = similarity
                        best_match = var2
                
                if best_match:
                    similarities[f"{var1} vs {best_match}"] = best_similarity
                    total_similarity += best_similarity
                    matched_pairs += 1
            
            # 计算平均相似度
            average_similarity = total_similarity / matched_pairs if matched_pairs > 0 else 0.0
            
            return average_similarity, similarities
            
        except Exception as e:
            logger.error(f"Error comparing codes: {e}")
            return 0.0, {}
    
    def get_detailed_comparison(self, code1: str, code2: str) -> Dict[str, Any]:
        """
        Get detailed comparison results
        """
        overall_similarity, detailed_similarities = self.compare_codes(code1, code2)
        
        return {
            "overall_similarity": overall_similarity,
            "detailed_similarities": detailed_similarities,
            "variable_mappings": self.symbol_map,
            "original_variables": self.reverse_map
        }

def main():
    # 测试代码
    code1 = """
    from sympy import symbols
    x = symbols('x')
    result = x**2 + 2*x + 1
    """
    
    code2 = """
    from sympy import symbols
    y = symbols('y')
    output = y**2 + 2*y + 1
    """
    
    comparator = SymPyComparator()
    result = comparator.get_detailed_comparison(code1, code2)
    
    print("Overall Similarity:", result["overall_similarity"])
    print("\nDetailed Similarities:")
    for expr_pair, similarity in result["detailed_similarities"].items():
        print(f"{expr_pair}: {similarity}")
        
    print("\nVariable Mappings:")
    for original, normalized in result["variable_mappings"].items():
        print(f"{original} -> {normalized}")

if __name__ == "__main__":
    main()