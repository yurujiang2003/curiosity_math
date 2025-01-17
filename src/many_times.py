import json
import os
from inference import Inference
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

def perform_inference_multiple_times(question: str, model_name: str, model_path: str, num_repeats: int, gpu_id: int):
    """
    Perform inference on a question multiple times.
    
    Args:
        question: The question to infer.
        model_name: Name of the model to use.
        model_path: Path to the model.
        num_repeats: Number of times to repeat the inference.
        gpu_id: The GPU ID to use for inference.
        
    Returns:
        dict: Question metadata and responses
    """
    # Initialize the inference object
    inferencer = Inference(model_name, gpu_id, model_path)
    questions = [question] * num_repeats  # Repeat the question

    try:
        responses = inferencer.batch_generate_responses(
            instructions=questions,
            batch_size=16,  # Adjust as needed
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            use_chat_template=True
        )

        # Return the responses and metadata
        return {
            "question": question,
            "responses": responses
        }

    except Exception as e:
        print(f"Error during inference: {e}")
        raise e

def extract_questions_from_json(json_file: str) -> list:
    """
    Extract questions from json file
    
    Args:
        json_file: the path of the json file
    
    Returns:
        questions: the list of questions
    """
    questions = []
    with open(json_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                questions.append(data['problem'])
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON line: {e}")
                continue
    return questions

if __name__ == "__main__":
    # Configuration
    json_file = "curiosity_math/Qwen2.5-7B-Instruct_responses_medium_ICL_ground_truth.json"
    model_name = "Qwen/Qwen2.5-Math-7B"
    model_path = model_name
    num_repeats = 100  # Number of times to repeat the inference
    gpu_id = 15  # GPU ID to use
    output_dir = "./many_times_results"
    
    try:
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Create output file path
        output_file = os.path.join(output_dir, f"all_responses_{num_repeats}_times.json")
        
        # Extract all questions
        questions = extract_questions_from_json(json_file)
        if not questions:
            raise ValueError("No questions found in the JSON file")
        
        # Initialize results dictionary
        results = {
            "metadata": {
                "model_name": model_name,
                "num_repeats": num_repeats,
                "temperature": 0.7,
                "top_p": 0.9,
                "total_questions": len(questions)
            },
            "results": []
        }
        
        # Process each question
        for idx, question in enumerate(questions):
            print(f"Processing question {idx + 1}/{len(questions)}: {question[:100]}...")  # Print first 100 chars
            
            try:
                # Perform inference
                question_results = perform_inference_multiple_times(
                    question=question,
                    model_name=model_name,
                    model_path=model_path,
                    num_repeats=num_repeats,
                    gpu_id=gpu_id
                )
                
                # Add results to the main dictionary
                results["results"].append(question_results)
                
                # Save the updated results after each question (in case of interruption)
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                
                print(f"Completed question {idx + 1}")
                
            except Exception as e:
                print(f"Error processing question {idx + 1}: {e}")
                continue
            
            # Clean up GPU memory after each question
            torch.cuda.empty_cache()
            torch.cuda.synchronize()
            
        print(f"All questions processed successfully! Results saved to {output_file}")

    except Exception as e:
        print(f"Error in main process: {e}")
    finally:
        # Final cleanup
        torch.cuda.empty_cache()
        torch.cuda.synchronize()