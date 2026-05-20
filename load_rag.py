print("STARTING LOAD_RAG")

from rag.document_loader import (
    DocumentLoader
)

print("IMPORT SUCCESS")

loader = DocumentLoader()

print("LOADER CREATED")

loader.load_documents()

print("DOCUMENTS LOADED")