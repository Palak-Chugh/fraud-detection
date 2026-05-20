from rag.retriever import (
    FraudRetriever
)

print("STARTING")

retriever = (
    FraudRetriever()
)

result = retriever.retrieve(
    """
    High value transaction
    at night using new device
    """
)

print("RAG RESULT:")
print(result)