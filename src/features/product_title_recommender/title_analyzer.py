"""
Title Analyzer Module for evaluating product titles using LLMs.
"""
import json
# Updated imports to work with older langchain version
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from ...models.llm_integrations import LLMFactory

class TitleEvaluator:
    """Class for evaluating product titles using LLMs"""
    
    def __init__(self, model_type="openai", model_name="gpt-4"):
        """
        Initialize a TitleEvaluator instance
        
        Args:
            model_type (str): Type of LLM to use (e.g. 'openai', 'llama')
            model_name (str): Name of the specific model to use
        """
        self.llm = LLMFactory.get_model(model_type=model_type, model_name=model_name)
        self._init_prompts()
        
    def _init_prompts(self):
        """Initialize the prompts used for title evaluation"""
        self.evaluation_prompt = ChatPromptTemplate.from_template(
            """You are an e-commerce product listing expert. Your task is to evaluate the quality of a product title 
            and determine if it's effective at attracting buyers.
            
            For the following product title: "{title}"
            
            Please provide an evaluation with:
            1. A quality rating (Good/Needs Improvement)
            2. Detailed reasoning for your rating
            3. A list of suggested additional product attributes that would improve the title if added
            4. An example of an improved title if the original needs improvement
            
            Format your response as a JSON with the following structure:
            {{
                "rating": "Good or Needs Improvement",
                "reasoning": "Your detailed reasoning here",
                "suggested_attributes": ["attribute1", "attribute2"],
                "improved_title": "Your improved title here if applicable, otherwise null"
            }}
            
            Only respond with the JSON object, no other text.
            """
        )
        
        self.evaluation_chain = LLMChain(
            llm=self.llm,
            prompt=self.evaluation_prompt
        )
        
    def evaluate_title(self, title):
        """
        Evaluate a product title using the configured LLM
        
        Args:
            title (str): The product title to evaluate
            
        Returns:
            dict: A dictionary containing the evaluation results
        """
        try:
            result = self.evaluation_chain.run(title=title)
            # Parse the JSON response from the LLM
            return json.loads(result)
        except Exception as e:
            print(f"Error evaluating title: {e}")
            return {
                "rating": "Error",
                "reasoning": f"Failed to evaluate title: {str(e)}",
                "suggested_attributes": [],
                "improved_title": None
            }
    
    def batch_evaluate_titles(self, products):
        """
        Evaluate multiple product titles in batch
        
        Args:
            products (list): List of product dictionaries with 'id' and 'title' keys
            
        Returns:
            list: List of dictionaries with product IDs and evaluation results
        """
        results = []
        for product in products:
            product_id = product.get('id', 'unknown')
            title = product.get('title', '')
            
            evaluation = self.evaluate_title(title)
            results.append({
                'product_id': product_id,
                'original_title': title,
                'evaluation': evaluation
            })
            
        return results