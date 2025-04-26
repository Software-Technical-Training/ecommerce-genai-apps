from setuptools import setup, find_packages

setup(
    name='ecommerce-genai-apps',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'langchain',
        'openai',
        'llama-index',
        'python-dotenv'
    ],
    description='Ecommerce GenAI Apps for product title and price recommendations',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/<your-username>/ecommerce-genai-apps',
)