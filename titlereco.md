# Product Title Recommender Feature Documentation

## Original User Prompts

### Initial Project Setup Prompt
```
I want to build a project in Python that will make calls to LLMs using langchain to do a few specific tasks like a) evaluating the titles of products in an online store across the top 3 LLMs (GPT, Lllama etc) to see if they will attract buyers to view the product and suggest alternate titles if the current titles are not well suited b) Ask price suggestions for a product from the top 3 LLMs. These are just a couple of examples of the types of feature I want to build. Here's some additional information
a) I have an OpenAI account with a paid secret key
b) I have a github account and would like to push this project to a new repo in github. You will need to suggest steps on how to do that.
c) I have Python3.10 and would like you to give me instructions on how to setup a virtual env and what libraries to download to make this project work.
d) I want you to create a project structure suitable for this project and add a readme.md and append the instructions on how to create the project, how to setup venv, how to push to github to this readme. I will ask you to add more details to it later.
```

### Title Recommendation Feature Prompt
```
Ok now we are ready to start adding code. Lets start with the product title recommender use case first. We will have a set of sample products with ids and titles and the goal is to call an LLM to evaluate the title to see if it is good or bad. IT should also suggest additional attributes it would like for me to provide to improve the title for the ones which it classifies as bad. Which LLM do you recommend we start with to test this? Here's a sample list of product titles to begin with:
Lacoste Elite Active 224 2 SMA
6 ' Fiberglass Step Ladder Folding
BRAND NEW GUCCI Ophidia Black Suede Leather Dome Cross Body Shoulder Bag Purse
Bose QuietComfort Ultra Noise Cancelling Headphones, Certified Refurbished
NWT Loft Red Blouse Floral Lace Trim Mixed Media Small Tunic Top Twee Spring
```

## User Requirements

The user requested to build a project in Python that uses LangChain to integrate with LLMs for performing specific e-commerce related tasks:

1. **Title Evaluation Feature**: Evaluating product titles across top LLMs (like GPT, Llama) to assess their effectiveness in attracting buyers and suggesting improvements when needed.
2. **Price Recommendation Feature**: Getting price suggestions for products from top LLMs.

Specific requirements included:
- Using an existing OpenAI account with a paid secret key
- Setting up a project that can be pushed to GitHub
- Using Python 3.10 with a virtual environment
- Creating an appropriate project structure

## Project Structure

The project was set up with the following structure:
```
ecommerce-genai-apps/
├── src/
│   ├── __init__.py
│   ├── features/
│   │   ├── __init__.py
│   │   ├── product_price_recommender/
│   │   │   ├── __init__.py
│   │   ├── product_title_recommender/
│   │   │   ├── __init__.py
│   │   │   ├── title_analyzer.py
│   │   │   ├── title_recommender.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── llm_integrations.py
│   ├── common/
│   │   ├── __init__.py
│   │   ├── utils.py
│   ├── config/
│   │   ├── __init__.py
│   ├── main.py
├── tests/
│   ├── __init__.py
├── notebooks/
│   ├── price_recommender_examples.ipynb
│   ├── title_recommender_examples.ipynb
├── data/
│   ├── sample_products.json
├── .env.example
├── requirements.txt
├── setup.py
├── README.md
```

## Implementation Summary

### Title Analyzer (`title_analyzer.py`)
The `TitleEvaluator` class evaluates product titles using LLMs (defaults to OpenAI's GPT-4). It:
- Takes a product title as input
- Sends a prompt to the LLM requesting evaluation of the title's quality
- Returns structured analysis including:
  - Rating (Good/Needs Improvement)
  - Reasoning behind the rating
  - Suggested attributes to add
  - Improved title suggestion if needed

### Title Recommender (`title_recommender.py`)
The `TitleRecommender` class leverages the `TitleEvaluator` to provide recommendations. It:
- Processes either individual titles or batches from JSON files
- Generates recommendations based on LLM evaluations
- Can save recommendations to a file for later reference

### LLM Integrations (`llm_integrations.py`)
The `LLMFactory` class provides a unified interface for connecting to different LLMs:
- Currently supports OpenAI models
- Has a placeholder for future Llama integration
- Uses environment variables for API keys

### Sample Data
Sample product titles were provided:
- "Lacoste Elite Active 224 2 SMA"
- "6 ' Fiberglass Step Ladder Folding"
- "BRAND NEW GUCCI Ophidia Black Suede Leather Dome Cross Body Shoulder Bag Purse"
- "Bose QuietComfort Ultra Noise Cancelling Headphones, Certified Refurbished"
- "NWT Loft Red Blouse Floral Lace Trim Mixed Media Small Tunic Top Twee Spring"

### Command-line Interface
A command-line interface was implemented in `main.py` allowing users to:
- Evaluate individual product titles
- Process batches of titles from a JSON file
- Save recommendations to a specified output file

## Usage Instructions

1. **Environment Setup**:
   ```bash
   # Create a .env file with your OpenAI API key
   OPENAI_API_KEY=your_actual_key_here
   ```

2. **Single Title Evaluation**:
   ```bash
   python -m src.main evaluate-title --title "Your product title here"
   ```

3. **Batch Title Evaluation**:
   ```bash
   python -m src.main evaluate-title --input-file data/sample_products.json --output-file data/title_recommendations.json
   ```

4. **Selecting Different Models**:
   ```bash
   python -m src.main evaluate-title --title "Your product title" --model-type openai --model-name gpt-4
   ```

## Next Steps

1. Implement the Price Recommender feature
2. Add additional LLM integrations (Llama, etc.)
3. Create a simple web UI for easier interaction with the tools
4. Implement a comparison functionality to see which LLM provides better recommendations

## Jupyter Notebook Implementation

To facilitate easy exploration and experimentation with the title recommender feature, a comprehensive Jupyter notebook was developed. The notebook, located at `notebooks/title_recommender_examples.ipynb`, provides an interactive interface for working with the title recommender.

### Notebook Structure and Features

1. **Setup and Configuration**
   - Imports necessary libraries
   - Configures the environment (including API key validation)
   - Sets up the path structure to access the project modules

2. **Data Loading**
   - Loads sample product data from the JSON file
   - Displays the data in a pandas DataFrame for easy inspection

3. **Title Recommender Instance Creation**
   - Creates an instance of the TitleRecommender with OpenAI's GPT-4
   - Shows how to configure different models (with GPT-3.5-turbo as an alternative example)

4. **Single Title Evaluation**
   - Demonstrates how to evaluate a single product title
   - Provides detailed output including rating, reasoning, and suggestions

5. **Batch Evaluation**
   - Shows how to process and evaluate all product titles in the sample data
   - Creates a summary DataFrame for quick overview of results

6. **Detailed Analysis**
   - Provides in-depth analysis of each title recommendation
   - Highlights the reasoning behind each evaluation

7. **Comparison Visualization**
   - Creates a side-by-side comparison of original and improved titles
   - Facilitates quick identification of titles needing improvement

8. **Result Persistence**
   - Demonstrates saving recommendations to a JSON file
   - Shows proper error handling for file operations

9. **Quality Analysis**
   - Includes statistical analysis of title quality
   - Features data visualization with matplotlib to show the proportion of good titles vs. those needing improvement

10. **Experimentation Section**
    - Provides a cell for testing custom product titles
    - Encourages hands-on experimentation with the model

### Benefits of the Notebook

1. **Interactive Learning**: Users can experiment with the title recommender in real-time and see immediate results.
2. **Visual Analysis**: Charts and formatted output make it easy to understand title quality distribution.
3. **Extensibility**: The notebook structure makes it easy to add new experiments or modify existing ones.
4. **Documentation**: Serves as both a tutorial and documentation for the title recommender feature.
5. **Reproducibility**: Enables consistent experimentation across different product datasets.

### Running the Notebook

To run the notebook:
1. Ensure your virtual environment is activated
2. Verify that your `.env` file contains a valid OpenAI API key
3. Navigate to the notebooks directory and start Jupyter:
   ```bash
   cd notebooks
   jupyter notebook
   ```
4. Open `title_recommender_examples.ipynb` and run the cells in sequence

The notebook provides a complete end-to-end demonstration of the title recommender, from setup to analysis, making it an ideal starting point for users new to the project.