import os
import json
import logging
from pathlib import Path
from typing import List, Dict, Any
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential
import re
from sympy import Basic, Matrix

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PySymExecutor:
    def __init__(self, api_key: str = None):
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
        
    def execute_pysym(self, pysym_code: str) -> Dict[str, Any]:
        """
        Execute the SymPy code and return the results
        Args:
            pysym_code: String containing Python SymPy code
        Returns:
            Dictionary containing execution results and any errors
        """
        try:
            # Create a new namespace for execution
            namespace = {
                'Basic': Basic,
                'Matrix': Matrix
            }
            
            # Add necessary imports to namespace
            exec('from sympy import *', namespace)
            
            # Execute the code
            exec(pysym_code, namespace)
            
            # Extract results
            results = {
                'success': True,
                'output': {},
                'error': None
            }
            
            # Find variables that are SymPy objects
            for var_name, value in namespace.items():
                if var_name.startswith('_'):  # Skip internal variables
                    continue
                    
                if isinstance(value, (Basic, Matrix)):  # SymPy types
                    try:
                        if hasattr(value, 'evalf'):
                            evalf_result = value.evalf()
                            # 检查是否可以安全地转换为数值
                            try:
                                if hasattr(evalf_result, 'is_real') and evalf_result.is_real:
                                    numeric_value = float(evalf_result)
                                else:
                                    numeric_value = None
                            except (TypeError, ValueError):
                                numeric_value = None
                        else:
                            numeric_value = None
                            
                        results['output'][var_name] = {
                            'symbolic': str(value),
                            'numeric': numeric_value
                        }
                    except Exception as e:
                        logger.warning(f"Could not process value for {var_name}: {e}")
                        results['output'][var_name] = {
                            'symbolic': str(value),
                            'numeric': None
                        }
            
            return results
            
        except Exception as e:
            logger.error(f"Error executing SymPy code: {e}")
            return {
                'success': False,
                'output': {},
                'error': str(e)
            }
    
    def format_output(self, results: Dict[str, Any]) -> str:
        """
        Format the execution results into a readable string
        """
        if not results['success']:
            return f"Execution Error: {results['error']}"
            
        output_lines = ["Execution Results:"]
        
        for var_name, value in results['output'].items():
            output_lines.append(f"\n{var_name}:")
            output_lines.append(f"  Symbolic: {value['symbolic']}")
            if value['numeric'] is not None:
                output_lines.append(f"  Numeric: {value['numeric']}")
                
        return '\n'.join(output_lines)
    
    def execute_and_format(self, pysym_code: str) -> str:
        """
        Execute the code and return formatted results
        """
        results = self.execute_pysym(pysym_code)
        return self.format_output(results)
    
    def validate_execution(self, pysym_code: str) -> bool:
        """
        Validate if the code can be executed safely
        """
        try:
            # Check for dangerous operations
            dangerous_ops = ['os', 'system', 'subprocess', 'eval', 'exec']
            for op in dangerous_ops:
                if op in pysym_code.lower():
                    logger.warning(f"Dangerous operation found: {op}")
                    return False
            
            # Try to compile the code
            compile(pysym_code, '<string>', 'exec')
            
            return True
            
        except Exception as e:
            logger.error(f"Code validation failed: {e}")
            return False
    
    def safe_execute(self, pysym_code: str) -> str:
        """
        Safely execute SymPy code with validation
        """
        if not self.validate_execution(pysym_code):
            return "Error: Code validation failed. Execution aborted."
            
        try:
            return self.execute_and_format(pysym_code)
        except Exception as e:
            logger.error(f"Safe execution failed: {e}")
            return f"Error during execution: {str(e)}"

        
# 创建执行器
executor = PySymExecutor()

# 示例代码
code = """
# Python SymPy Solution
from sympy import symbols, Rational
import sympy as sp
# Define the angle ABC as a symbol
angle_ABC = symbols('angle_ABC')
# Calculate the angles
angle_ABQ = Rational(2, 3) * angle_ABC
angle_MBQ = Rational(1, 6) * angle_ABC
# Calculate the ratio
ratio = angle_MBQ / angle_ABQ

ratio
"""

# 执行代码
result = executor.safe_execute(code)
print(result)