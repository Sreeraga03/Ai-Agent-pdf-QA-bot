# Ai-Agent-pdf-QA-bot
 PDF Question Answering App that allows users to upload a PDF document and input a list of questions. The app uses a large language model to extract answers from the content of the PDF document. The answers are then displayed in a structured JSON format.

# Features
Upload a PDF document.
Input a list of questions.
Extract answers from the PDF content using a large language model.
Display the answers in a structured JSON format.

# Requirements
Python 3.8 or higher
Streamlit
PyPDF2
Langchain
OpenAI

# Installation

1.Clone the repository:
git clone https://github.com/Sreeraga03/Ai-Agent-pdf-QA-bot.git
cd Ai-Agent-pdf-QA-bot

2.Set up a virtual environment:
conda create -p llmproject python==3.9 -y
conda activate llmproject

3.Install the required packages:
pip install -r requirements.txt

# Configuration
1.Set up OpenAI API key:
Replace "your_openai_api_key" in main.py with your actual OpenAI API key(The current API will not work as i exchange the characters).

# Usage
1.Run the Streamlit app:
streamlit run main.py

2.Upload a PDF file:
Choose a PDF file to upload.

3.Enter questions:
Enter your questions in the provided text area (one per line).

4.Submit:
Click the "Submit" button to process the PDF and questions.

5.View Answers:
The answers will be displayed in a structured JSON format.

# File Structure

pdf-question-answering-app/
main.py                   # Main application code
requirements.txt          # List of required packages
README.md                 # Project documentation

# Contributing
1.Fork the repository.
2.Create a new branch (git checkout -b feature/your-feature-name).
3.Commit your changes (git commit -am 'Add some feature').
4.Push to the branch (git push origin feature/your-feature-name).
5.Create a new Pull Request.

# Acknowledgments

[OpenAI](https://openai.com/) for their powerful language model.
[Streamlit](https://streamlit.io/) for their easy-to-use web app framework.
[Langchain](https://langchain.com/) for their embeddings and vector store functionalities.


