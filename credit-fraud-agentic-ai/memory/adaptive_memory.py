import chromadb
from sentence_transformers import SentenceTransformer
import uuid


class AdaptiveMemory:

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="./memory/chroma_store"
        )

        self.collection = self.client.get_or_create_collection(
            name="fraud_memory"
        )

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def store_case(self, transaction, result):

        memory_text = f"""
        Transaction:
        {transaction}

        Fraud Analysis:
        {result}
        """

        embedding = self.embedding_model.encode(
            memory_text
        ).tolist()

        self.collection.add(
            ids=[str(uuid.uuid4())],
            documents=[memory_text],
            embeddings=[embedding]
        )

    def retrieve_similar_cases(
        self,
        transaction_text,
        top_k=3
    ):

        embedding = self.embedding_model.encode(
            transaction_text
        ).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        return results["documents"][0] \
            if results["documents"] else []