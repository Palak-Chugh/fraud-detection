from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embedding_model = OpenAIEmbeddings(
    api_key=OPENAI_API_KEY
)

def build_vector_store(pdf_folder):

    documents = []

    for file in os.listdir(pdf_folder):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(
                os.path.join(pdf_folder, file)
            )

            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    split_docs = splitter.split_documents(documents)

    vector_db = FAISS.from_documents(
        split_docs,
        embedding_model
    )

    vector_db.save_local("vector_store")

    print("FAISS vector store created.")