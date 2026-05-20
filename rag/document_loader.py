# from pathlib import Path
# from sentence_transformers import (
#     SentenceTransformer
# )
# import uuid

# from rag.chroma_manager import (
#     ChromaManager
# )


# EMBEDDING_MODEL = (
#     SentenceTransformer(
#         "all-MiniLM-L6-v2"
#     )
# )


# class DocumentLoader:

#     def __init__(self):

#         self.chroma = (
#             ChromaManager()
#         )

#     def load_documents(self):

#         folder = Path(
#             "rag/knowledge_base"
#         )

#         docs = []
#         embeddings = []
#         ids = []

#         for file in folder.glob("*.txt"):

#             content = file.read_text(
#                 encoding="utf-8"
#             )

#             chunks = self.chunk_text(
#                 content
#             )

#             for chunk in chunks:

#                 embedding = (
#                     EMBEDDING_MODEL
#                     .encode(chunk)
#                     .tolist()
#                 )

#                 docs.append(chunk)

#                 embeddings.append(
#                     embedding
#                 )

#                 ids.append(
#                     str(uuid.uuid4())
#                 )

#         self.chroma.add_documents(
#             docs,
#             embeddings,
#             ids
#         )

#         print(
#             f"{len(docs)} chunks loaded"
#         )

#     def chunk_text(
#         self,
#         text,
#         chunk_size=300
#     ):

#         return [
#             text[i:i + chunk_size]
#             for i in range(
#                 0,
#                 len(text),
#                 chunk_size
#             )
#         ]
from pathlib import Path
import uuid

from rag.chroma_manager import (
    ChromaManager
)


class DocumentLoader:

    def __init__(self):

        self.chroma = (
            ChromaManager()
        )

    def load_documents(self):

        base_dir = (
            Path(__file__)
            .resolve()
            .parent
        )

        knowledge_path = (
            base_dir /
            "knowledge_base"
        )

        print(
            "Knowledge path:",
            knowledge_path
        )

        txt_files = list(
            knowledge_path.glob(
                "*.txt"
            )
        )

        print(
            "Files found:",
            len(txt_files)
        )

        docs = []
        ids = []

        for file in txt_files:

            print(
                f"Loading {file.name}"
            )

            content = (
                file.read_text(
                    encoding="utf-8"
                )
            )

            docs.append(content)

            ids.append(
                str(uuid.uuid4())
            )

        self.chroma.collection.add(
            documents=docs,
            ids=ids
        )

        print(
            "Documents loaded"
        )