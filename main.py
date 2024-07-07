import os
import json
from PyPDF2 import PdfReader # Used to read PDF files
from langchain.embeddings.openai import OpenAIEmbeddings # components from the LangChain library to handle embeddings
from langchain.text_splitter import  CharacterTextSplitter # it will handle text splitting
from langchain.vectorstores import FAISS # used for vector storage
from langchain.chains.question_answering import load_qa_chain # question answering
# as default it use GPT-3 models like text-davinci-003 or text-davinci-002
from langchain.llms import OpenAI

import streamlit as st

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = "akp-proj-hgjASeo5vyumWzlPRmepT3BlbkFJ1wDNElVFqzfVQQBg6ntotoyis"

# Streamlit interface
st.title("PDF Question Answering App")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
questions = st.text_area("Enter your questions (one per line)")

# Function to process PDF and questions on submit
def process_pdf_and_questions():
    if uploaded_file is not None and questions:
        pdfreader = PdfReader(uploaded_file)

        # Read text from PDF
        # here it extract each page text and feed into raw_text variable
        raw_text = ''
        for i, page in enumerate(pdfreader.pages):
            content = page.extract_text()
            if content:
                raw_text += content

        # Split the text using Character Text Splitter
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)

        # Download embeddings from OpenAI
        embeddings = OpenAIEmbeddings()

        document_search = FAISS.from_texts(texts, embeddings)
        chain = load_qa_chain(OpenAI(), chain_type="stuff")

        # Process each question
        questions_list = questions.split('\n')
        answers = {}
        for query in questions_list:
            query = query.strip()
            if query:
                docs = document_search.similarity_search(query)
                answer = chain.run(input_documents=docs, question=query)
                if "Data Not Available" in answer or len(answer) == 0:
                    answer = "Data Not Available"
                answers[query] = answer

        # Display the answers as JSON
        st.write("Answers:")
        st.json(answers)

        # Save the answers to a JSON file
        output_file = "answers.json"
        with open(output_file, 'w') as f:
            json.dump(answers, f, indent=2)

        st.write(f"Answers have been saved to {output_file}")

# Submit button
if st.button("Submit"):
    process_pdf_and_questions()
