from rag.retriever import (
    FraudRetriever
)

retriever = (
    FraudRetriever()
)

query = """
High value transaction
at night using new device
"""

result = retriever.retrieve(
    query
)

print(result)