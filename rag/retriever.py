# from sentence_transformers import (
#     SentenceTransformer
# )

# from rag.chroma_manager import (
#     ChromaManager
# )


# EMBEDDING_MODEL = (
#     SentenceTransformer(
#         "all-MiniLM-L6-v2"
#     )
# )


# class FraudRetriever:

#     def __init__(self):

#         self.chroma = (
#             ChromaManager()
#         )

#     def retrieve(
#         self,
#         query
#     ):

#         embedding = (
#             EMBEDDING_MODEL
#             .encode(query)
#             .tolist()
#         )

#         results = (
#             self.chroma.search(
#                 embedding
#             )
#         )

#         documents = (
#             results["documents"][0]
#         )

#         return "\n".join(
#             documents
#         )
class FraudRetriever:

    def retrieve(
        self,
        query
    ):

        return """
        Transactions above ₹50,000
        using a new device
        between 12 AM and 4 AM
        should be reviewed.

        Trusted devices reduce risk.
        """