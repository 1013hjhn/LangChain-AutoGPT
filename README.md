# 🦜🔗 Jaehee's Learning GPT

## Executive Summary

This AutoGPT is an interactive web application built with Streamlit and powered by OpenAI's langauge model. This allows users to input promts and receive AI-generated concept explanations and FAQ list with answers. It leverages LangChain framework for an efficient prompt management and integrates Wikipidea research to enhance the quality of responses. It is built with a purpose of assisting a wide range of users with learning procedure in academic subject, by providing a detailed explanation of concepts and related questions with answers. 

Key features:
- AI-generated concept explanations
- Automated FAQ generation based on user prompts
- Integration with Wikipedia for additional context
- Conversation history tracking for concepts and questions
- User-friendly interface powered by Streamlit

## 🛠 Installation
### Prerequisites

- Python 3.7 or higher

### Install required Python packages:
```sh
pip install --user streamlit langchain openai wikipedia-api chromadb tiktoken
 ```
### Set up your OpenAI API key:
   ```sh
apikey = "your-openai-api-key-here"
