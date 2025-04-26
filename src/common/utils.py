"""
Utility functions for the ecommerce-genai-apps project.
"""
import os
import json
import argparse

def ensure_directory_exists(file_path):
    """
    Ensure the directory for a file exists
    
    Args:
        file_path (str): Path to a file
    """
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def save_json(data, file_path):
    """
    Save data to a JSON file
    
    Args:
        data: Data to save
        file_path (str): Path to the output file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        ensure_directory_exists(file_path)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        print(f"Error saving data to file: {e}")
        return False

def load_json(file_path):
    """
    Load data from a JSON file
    
    Args:
        file_path (str): Path to the input file
        
    Returns:
        dict: The loaded data, or None if loading fails
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading data from file: {e}")
        return None

def setup_env_file():
    """
    Setup the .env file with required environment variables
    """
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            # Copy the example file content to create a new .env file
            try:
                with open('.env.example', 'r') as example_file:
                    example_content = example_file.read()
                
                with open('.env', 'w') as env_file:
                    env_file.write(example_content)
                
                print("Created .env file from .env.example.")
                print("SECURITY NOTE: Please edit the .env file and add your actual API keys.")
                print("This file will not be committed to version control.")
            except Exception as e:
                print(f"Error creating .env file: {e}")
                print("Please manually create a .env file with your API keys.")
        else:
            # Create a basic .env file if no example exists
            with open('.env', 'w') as f:
                f.write('# Add your API keys below\n')
                f.write('OPENAI_API_KEY=your_openai_api_key_here\n')
            print("Created .env file. Please add your OpenAI API key.")
            print("SECURITY NOTE: This file will not be committed to version control.")
    else:
        print(".env file already exists.")