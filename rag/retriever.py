from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

import os

embedding_model = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

vector_db = FAISS.load_local(
    "vector_store",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

def retrieve_context(query):

    docs = retriever.invoke(query)

    return "\n".join([doc.page_content for doc in docs])