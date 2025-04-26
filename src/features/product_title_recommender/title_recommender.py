"""
Title Recommender Module for suggesting improved product titles based on LLM evaluations.
"""
import json
from .title_analyzer import TitleEvaluator

class TitleRecommender:
    """Class for suggesting improved product titles based on LLM evaluations"""
    
    def __init__(self, model_type="openai", model_name="gpt-4"):
        """
        Initialize a TitleRecommender instance
        
        Args:
            model_type (str): Type of LLM to use (e.g. 'openai', 'llama')
            model_name (str): Name of the specific model to use
        """
        self.evaluator = TitleEvaluator(model_type=model_type, model_name=model_name)
    
    def get_recommendation(self, title):
        """
        Get a recommendation for a single product title
        
        Args:
            title (str): The product title to get recommendations for
            
        Returns:
            dict: A dictionary containing the evaluation and recommendation
        """
        evaluation = self.evaluator.evaluate_title(title)
        
        recommendation = {
            'original_title': title,
            'evaluation': evaluation,
            'needs_improvement': evaluation['rating'] == 'Needs Improvement',
            'suggested_attributes': evaluation['suggested_attributes'],
            'improved_title': evaluation['improved_title']
        }
        
        return recommendation
    
    def get_batch_recommendations(self, products_data):
        """
        Get recommendations for multiple products
        
        Args:
            products_data (list or str): Either a list of product dictionaries or a path to a JSON file
            
        Returns:
            list: List of dictionaries with evaluation and recommendation data
        """
        # Load products data if a file path is provided
        if isinstance(products_data, str):
            try:
                with open(products_data, 'r') as file:
                    data = json.load(file)
                    products = data.get('products', [])
            except Exception as e:
                print(f"Error loading products data from file: {e}")
                return []
        else:
            products = products_data
        
        # Get evaluations for all products
        evaluations = self.evaluator.batch_evaluate_titles(products)
        
        # Transform evaluations into recommendations
        recommendations = []
        for eval_result in evaluations:
            product_id = eval_result.get('product_id', 'unknown')
            title = eval_result.get('original_title', '')
            evaluation = eval_result.get('evaluation', {})
            
            recommendations.append({
                'product_id': product_id,
                'original_title': title,
                'evaluation': evaluation,
                'needs_improvement': evaluation.get('rating', '') == 'Needs Improvement',
                'suggested_attributes': evaluation.get('suggested_attributes', []),
                'improved_title': evaluation.get('improved_title', None)
            })
        
        return recommendations
    
    def save_recommendations(self, recommendations, output_file):
        """
        Save recommendations to a JSON file
        
        Args:
            recommendations (list): List of recommendation dictionaries
            output_file (str): Path to the output file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(output_file, 'w') as file:
                json.dump({'recommendations': recommendations}, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving recommendations to file: {e}")
            return False