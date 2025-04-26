"""
Main entry point for the ecommerce-genai-apps application.
"""
import os
import argparse
import json
from dotenv import load_dotenv
from features.product_title_recommender.title_recommender import TitleRecommender
from common.utils import setup_env_file, load_json, save_json

# Load environment variables
load_dotenv()

def evaluate_titles(args):
    """
    Evaluate product titles using the specified model
    
    Args:
        args: Command-line arguments
    """
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set it in the .env file.")
        setup_env_file()
        return
    
    # Create title recommender
    recommender = TitleRecommender(
        model_type=args.model_type, 
        model_name=args.model_name
    )
    
    # Process input
    if args.title:
        # Single title evaluation
        result = recommender.get_recommendation(args.title)
        print(json.dumps(result, indent=2))
    elif args.input_file:
        # Batch evaluation
        products_data = args.input_file
        recommendations = recommender.get_batch_recommendations(products_data)
        
        if args.output_file:
            save_json({'recommendations': recommendations}, args.output_file)
            print(f"Recommendations saved to {args.output_file}")
        else:
            print(json.dumps({'recommendations': recommendations}, indent=2))
    else:
        print("Error: You must provide either a title or an input file.")
        

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="ecommerce-genai-apps command line interface")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Title evaluation command
    title_parser = subparsers.add_parser("evaluate-title", help="Evaluate product titles")
    title_parser.add_argument("--title", help="Single product title to evaluate")
    title_parser.add_argument("--input-file", help="Path to JSON file containing product data")
    title_parser.add_argument("--output-file", help="Path to save evaluation results")
    title_parser.add_argument("--model-type", default="openai", help="Type of LLM to use (openai, llama)")
    title_parser.add_argument("--model-name", default="gpt-4", help="Name of the specific model")
    
    # Parse arguments
    args = parser.parse_args()
    
    if args.command == "evaluate-title":
        evaluate_titles(args)
    elif not args.command:
        parser.print_help()
    else:
        print(f"Unknown command: {args.command}")

if __name__ == "__main__":
    main()