from embed import ResponseAnalyzer
from data_load import load_data
import numpy as np
from typing import List, Tuple
from sklearn.metrics.pairwise import cosine_similarity

def get_average_embedding(question: str, responses: List[str], analyzer: ResponseAnalyzer) -> np.ndarray:
    """
    Get average embedding vector for all responses to a question
    
    Args:
        question (str): The question text
        responses (List[str]): List of response texts
        analyzer (ResponseAnalyzer): Embedding model instance
        
    Returns:
        np.ndarray: Average embedding vector
    """
    # Get embeddings for all responses
    embeddings = []
    for response in responses:
        embedding = analyzer.get_embedding(response)
        embeddings.append(embedding)
    
    # Convert to numpy array and calculate mean
    embeddings_array = np.array(embeddings)
    average_embedding = np.mean(embeddings_array, axis=0)
    
    return average_embedding

def process_qa_pairs(file_path: str, analyzer: ResponseAnalyzer) -> List[Tuple[str, np.ndarray]]:
    """
    Process all QA pairs in a file and get average embeddings
    
    Args:
        file_path (str): Path to the JSON file
        analyzer (ResponseAnalyzer): Embedding model instance
        
    Returns:
        List[Tuple[str, np.ndarray]]: List of (question, average_embedding) pairs
    """
    qa_pairs = load_data(file_path)
    results = []
    
    for question, responses in qa_pairs:
        avg_embedding = get_average_embedding(question, responses, analyzer)
        results.append((question, avg_embedding))
    
    return results

def compare_with_reference(question: str, 
                         new_response: str, 
                         reference_data: List[Tuple[str, np.ndarray]], 
                         analyzer: ResponseAnalyzer) -> float:
    """
    Compare a new response with the reference average embedding for the same question
    
    Args:
        question (str): The question text
        new_response (str): New response to compare
        reference_data: List of (question, avg_embedding) tuples from reference data
        analyzer (ResponseAnalyzer): Embedding model instance
        
    Returns:
        float: Cosine similarity score with the reference average embedding
    """
    new_embedding = analyzer.get_embedding(new_response)

    reference_embedding = None
    for ref_question, ref_embedding in reference_data:
        if ref_question == question:
            reference_embedding = ref_embedding
            break
    
    if reference_embedding is None:
        raise ValueError(f"Question not found in reference data: {question}")
    
    similarity = cosine_similarity(new_embedding, reference_embedding)
    return similarity

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors
    """
    dot_product = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    return dot_product / (norm1 * norm2)

def select_diverse_responses(question: str,
                           responses: List[str],
                           reference_data: List[Tuple[str, np.ndarray]],
                           analyzer: ResponseAnalyzer,
                           select_ratio: float = 0.2,
                           min_similarity_threshold: float = 0.1) -> List[str]:
    """
    Select responses that have larger differences from the reference average embedding
    
    Args:
        question (str): The question text
        responses (List[str]): List of responses to filter
        reference_data: List of (question, avg_embedding) tuples from reference data
        analyzer (ResponseAnalyzer): Embedding model instance
        select_ratio (float): Ratio of responses to select (0.0-1.0)
        min_similarity_threshold (float): Minimum similarity threshold to consider
        
    Returns:
        List[str]: Selected diverse responses
    """
    reference_embedding = None
    for ref_question, ref_embedding in reference_data:
        if ref_question == question:
            reference_embedding = ref_embedding
            break
    
    if reference_embedding is None:
        raise ValueError(f"Question not found in reference data: {question}")
    
    response_similarities = []
    for response in responses:
        response_embedding = analyzer.get_embedding(response)
        similarity = cosine_similarity(response_embedding, reference_embedding)
        response_similarities.append((response, similarity))
    
    response_similarities.sort(key=lambda x: x[1])
    
    filtered_responses = [
        (resp, sim) for resp, sim in response_similarities 
        if sim >= min_similarity_threshold
    ]
    
    num_to_select = max(1, int(len(filtered_responses) * select_ratio))
    selected_responses = [resp for resp, _ in filtered_responses[:num_to_select]]
    
    return selected_responses

def main():
    analyzer = ResponseAnalyzer()
    reference_file = "path/to/reference_results.json"
    reference_data = process_qa_pairs(reference_file, analyzer)
    
    question = "The measure of each exterior angle..."
    responses = [
        "Response 1...",
        "Response 2...",
        "Response 3...",
        # ... more responses
    ]
    
    try:
        diverse_responses = select_diverse_responses(
            question,
            responses,
            reference_data,
            analyzer,
            select_ratio=0.3,  # 选择30%的responses
            min_similarity_threshold=0.5  # 最小相似度阈值
        )
        
        print(f"Selected {len(diverse_responses)} diverse responses:")
        for i, response in enumerate(diverse_responses, 1):
            print(f"{i}. {response}\n")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()