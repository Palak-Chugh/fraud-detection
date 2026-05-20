import chromadb


class ChromaManager:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./rag/vector_store"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="fraud_knowledge"
            )
        )

    def add_documents(
        self,
        documents,
        embeddings,
        ids
    ):

        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            ids=ids
        )

    def search(
        self,
        embedding,
        top_k=3
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )