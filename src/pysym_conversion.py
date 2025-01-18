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

class ExtractResponse:
    def __init__(self, file_path: str, novel_or_not: bool):
        self.file_path = Path(file_path)
        self.novel_or_not = novel_or_not
        
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

    def extract_response(self) -> List[Dict[str, str]]:
        """
        Extract the response from the JSON file
        """
        responses = []
        response_type = "novel_response" if self.novel_or_not else "common_response"
        
        logger.info(f"Starting extraction from {self.file_path}")
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line_num, line in enumerate(file, 1):
                    try:
                        data = json.loads(line)
                        if response_type in data:
                            response = {
                                "problem": data.get("problem", ""),
                                "solution": data.get("solution", ""),
                                "response": data[response_type]
                            }
                            responses.append(response)
                    except json.JSONDecodeError as e:
                        logger.error(f"Error parsing JSON at line {line_num}: {e}")
                        continue
        except Exception as e:
            logger.error(f"Error reading file: {e}")
            raise
            
        logger.info(f"Extracted {len(responses)} responses")
        return responses

class PysymConverter:
    def __init__(self, api_key: str = None):
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
        
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def convert_to_pysym(self, text: str) -> str:
        """
        Convert the text to Python sympy code
        """
        try:
            completion = self.client.chat.completions.create(
                messages=[{
                    "role": "system",
                    "content": "You are a Python SymPy code generator. Convert mathematical problems into Python code using the SymPy library for symbolic mathematics. Always include necessary imports and ensure the code is executable."
                }, {
                    "role": "user",
                    "content": f"Do not change the original mathematical logic. Convert this mathematical problem into Python SymPy code: {text}. Return only the code, no explanations."
                }],
                model="gpt-4",
                temperature=0.1
            )
            return completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error in API call: {e}")
            raise

    def validate_pysym(self, pysym_code: str) -> bool:
        """
        Validate if the generated Python SymPy code is syntactically correct
        by checking syntax and imports
        """
        try:

            compile(pysym_code, '<string>', 'exec')

            required_imports = ['sympy', 'symbols', 'Rational']
            code_lines = pysym_code.lower().split('\n')
            import_lines = [line for line in code_lines if 'import' in line]

            for req_import in required_imports:
                if not any(req_import.lower() in line for line in import_lines):
                    logger.warning(f"Missing required import: {req_import}")
                    return False

            if 'symbols(' not in pysym_code:
                logger.warning("No symbol definition found in code")
                return False
            
            return True
            
        except SyntaxError as e:
            logger.error(f"Syntax error in code: {e}")
            return False
        except Exception as e:
            logger.error(f"Error validating code: {e}")
            return False
            
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def optimize_pysym(self, pysym_code: str) -> str:
        """
        Optimize the Python SymPy code for better performance and readability
        """
        try:
            completion = self.client.chat.completions.create(
                messages=[{
                    "role": "system",
                    "content": "You are a Python code optimizer specializing in SymPy code. The only thing you should do is to ensure the code is syntactically correct and includes all necessary imports. Do not change the code logic."
                }, {
                    "role": "user",
                    "content": f"Check if the code is syntactically correct and includes all necessary imports. Do not change the code logic. {pysym_code}"
                }],
                model="gpt-4",
                temperature=0.1
            )
            return completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error in optimization API call: {e}")
            raise
            
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def extract_pysym_block(self, text: str) -> str:
        """
        Extract Python SymPy code block from text using regex patterns
        Args:
            text: The text containing Python SymPy code
        Returns:
            str: Extracted Python SymPy code
        """
        try:
            # Pattern for code blocks with markdown
            markdown_pattern = r'```(?:python)?\s*(.*?)\s*```'
            # Pattern for imports
            import_pattern = r'(?:from\s+sympy|import\s+sympy)'
            
            # First try to find code blocks with markdown formatting
            code_blocks = re.findall(markdown_pattern, text, re.DOTALL)
            
            if code_blocks:
                # Filter blocks that contain SymPy imports or usage
                sympy_blocks = [block for block in code_blocks 
                              if re.search(import_pattern, block, re.IGNORECASE) 
                              or 'sympy' in block.lower()]
                
                if sympy_blocks:
                    # Return the first valid SymPy code block
                    return self._clean_code_block(sympy_blocks[0])
            
            # If no markdown blocks found, try to find Python code directly
            lines = text.split('\n')
            code_lines = []
            in_code_block = False
            
            for line in lines:
                # Check for code indicators
                if any(indicator in line.lower() for indicator in 
                      ['import sympy', 'from sympy', 'symbols(', 'sp.']):
                    in_code_block = True
                
                if in_code_block:
                    # Stop collecting at clearly non-code lines
                    if any(end_indicator in line.lower() for end_indicator in 
                          ['therefore', 'thus', 'hence', 'solution:']):
                        break
                    code_lines.append(line)
            
            if code_lines:
                return self._clean_code_block('\n'.join(code_lines))
            
            # If no code found, return original text
            return text
            
        except Exception as e:
            logger.error(f"Error in code extraction: {e}")
            return text

    def _clean_code_block(self, code: str) -> str:
        """
        Clean and format the extracted code block
        """
        try:
            # Remove markdown formatting
            code = re.sub(r'```python|```', '', code)
            
            # Remove output sections
            code = re.sub(r'```output.*?```', '', code, flags=re.DOTALL)
            
            # Clean up empty lines and whitespace
            lines = [line.rstrip() for line in code.split('\n')]
            lines = [line for line in lines if line.strip()]
            
            # Ensure proper imports
            has_sympy_import = any('sympy' in line for line in lines)
            if has_sympy_import and not any('from sympy import' in line for line in lines):
                # Add basic imports if needed
                lines.insert(0, 'from sympy import symbols, Rational')
            
            # Join lines and ensure proper spacing
            cleaned_code = '\n'.join(lines)
            
            # Validate the cleaned code
            if self.validate_pysym(cleaned_code):
                return cleaned_code
            else:
                logger.warning("Extracted code failed validation")
                return code
            
        except Exception as e:
            logger.error(f"Error in code cleaning: {e}")
            return code

    def process_text(self, text: str, validate: bool = True, optimize: bool = True) -> str:
        """
        Process text and return the final Python SymPy code block
        """
        try:
            # Convert to Python SymPy
            raw_output = self.convert_to_pysym(text)
            
            # Extract Python SymPy code from the output
            pysym_code = self.extract_pysym_block(raw_output)
            
            # Validate if requested
            if validate:
                is_valid = self.validate_pysym(pysym_code)
                
                # Only optimize if code is valid and optimization is requested
                if is_valid and optimize:
                    optimized_output = self.optimize_pysym(pysym_code)
                    pysym_code = self.extract_pysym_block(optimized_output)
                    
            # Format the code block
            formatted_code = f"""# Python SymPy Solution
{pysym_code}
"""
            return formatted_code
            
        except Exception as e:
            logger.error(f"Error in processing pipeline: {e}")
            return f"# Error: {str(e)}"

    def batch_process(self, texts: List[str], validate: bool = True, optimize: bool = True) -> List[Dict[str, Any]]:
        """
        Process multiple texts in batch
        """
        results = []
        total = len(texts)
        
        for i, text in enumerate(texts, 1):
            logger.info(f"Processing text {i}/{total}")
            try:
                result = self.process_text(text, validate, optimize)
                results.append(result)
            except Exception as e:
                logger.error(f"Error processing text {i}: {e}")
                results.append({
                    "original_text": text,
                    "error": str(e)
                })
                
        return results


class PySymDealer:
    def __init__(self, api_key: str = None):
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
    
    def self_verifier(self):
        """
        self verifier
        """
        pass
 
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

            for var_name, value in namespace.items():
                if var_name.startswith('_'):  
                    continue
                    
                if isinstance(value, (Basic, Matrix)):  # SymPy types
                    try:
                        if hasattr(value, 'evalf'):
                            evalf_result = value.evalf()
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
    
def save_results(results: List[Dict[str, Any]], output_file: str):
    """
    save the results to a json file
    """
    output_path = Path(output_file)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        logger.info(f"Results saved to {output_path}")
    except Exception as e:
        logger.error(f"Error saving results: {e}")
        raise
