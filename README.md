# Ecommerce GenAI Apps

## Project Structure
```
ecommerce-genai-apps/
├── src/
│   ├── __init__.py
│   ├── features/
│   │   ├── __init__.py
│   │   ├── product_price_recommender/
│   │   │   ├── __init__.py
│   │   │   ├── price_analyzer.py
│   │   │   └── price_recommender.py
│   │   └── product_title_recommender/
│   │       ├── __init__.py
│   │       ├── title_analyzer.py
│   │       └── title_recommender.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── llm_integrations.py
│   ├── common/
│   │   ├── __init__.py
│   │   └── utils.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── tests/
│   ├── __init__.py
│   ├── test_price_recommender.py
│   └── test_title_recommender.py
├── notebooks/
│   ├── price_recommender_examples.ipynb
│   └── title_recommender_examples.ipynb
├── data/
│   └── sample_products.json
├── .env.example
├── requirements.txt
├── setup.py
└── README.md
```

## Setting Up the Project

### Step 1: Create a Virtual Environment
1. Open a terminal and navigate to the project directory:
   ```bash
   cd /Users/veranky/Documents/Personal/STTI/python_projects/ecommerce-genai-apps
   ```
2. Create a virtual environment named `stti-venv`:
   ```bash
   python3 -m venv stti-venv
   ```
3. Activate the virtual environment:
   - On macOS/Linux (using zsh):
     ```bash
     source stti-venv/bin/activate
     ```
   - On Windows:
     ```bash
     stti-venv\Scripts\activate
     ```

### Step 2: Install Required Libraries
1. Install the necessary libraries by creating a `requirements.txt` file with the following content:
   ```
   langchain
   openai
   llama-index
   python-dotenv
   ```
2. Install the libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Set Up API Keys Securely
1. Copy the `.env.example` file to create your own `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Open the `.env` file in your preferred text editor:
   ```bash
   nano .env   # or use any text editor
   ```
3. Add your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```
4. Save and close the file.

**Important Security Note:**
- The `.env` file is automatically excluded from Git via the `.gitignore` file
- Never commit API keys or other sensitive information directly to your repository
- Always use environment variables for sensitive information

## Pushing the Project to GitHub

### Step 1: Initialize a Git Repository
1. Navigate to the project directory:
   ```bash
   cd /Users/veranky/Documents/Personal/STTI/python_projects/ecommerce-genai-apps
   ```
2. Initialize a Git repository:
   ```bash
   git init
   ```

### Step 2: Add Files and Commit
1. Add all files to the repository:
   ```bash
   git add .
   ```
2. Commit the changes:
   ```bash
   git commit -m "Initial commit"
   ```

### Step 3: Create a New Repository on GitHub
1. Go to [GitHub](https://github.com) and log in to your account.
2. Click the **New** button to create a new repository.
3. Name the repository `ecommerce-genai-apps` and click **Create Repository**.

### Step 4: Push the Project to GitHub
1. Add the remote repository:
   ```bash
   git remote add origin https://github.com/<your-username>/ecommerce-genai-apps.git
   ```
2. Push the project to GitHub:
   ```bash
   git branch -M main
   git push -u origin main
   ```

Your project is now set up and pushed to GitHub!