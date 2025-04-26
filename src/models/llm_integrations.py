"""
LLM Integration Module for connecting to various language models.
"""
import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LLMFactory:
    """Factory class for creating LLM instances"""
    
    @staticmethod
    def get_openai(model_name="gpt-4", temperature=0.0):
        """
        Get an instance of OpenAI model
        
        Args:
            model_name (str): The name of the OpenAI model to use
            temperature (float): The temperature parameter for the model
            
        Returns:
            ChatOpenAI: An instance of the ChatOpenAI model
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
            
        return ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            api_key=api_key
        )
    
    @staticmethod
    def get_llama(model_path=None):
        """
        Placeholder for Llama model integration
        To be implemented in future versions
        """
        raise NotImplementedError("Llama integration not yet implemented")
    
    @staticmethod
    def get_model(model_type="openai", **kwargs):
        """
        Get an LLM model based on the model type
        
        Args:
            model_type (str): The type of model to use ('openai', 'llama', etc.)
            **kwargs: Additional arguments to pass to the model constructor
            
        Returns:
            LLM: An instance of the specified LLM
        """
        if model_type.lower() == "openai":
            return LLMFactory.get_openai(**kwargs)
        elif model_type.lower() == "llama":
            return LLMFactory.get_llama(**kwargs)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")