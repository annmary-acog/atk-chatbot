from langchain import embeddings
from langchain.docstore.document import Document
from atk_vectordbs.vector_dbs import BaseVectorDB
from atk_embeddings.chunker import Chunker
from typing import List
import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(level='INFO')


class EmbeddingsPipeline:
    def __init__(self, embed_model: embeddings, vector_db: BaseVectorDB):
        self.embed_model: embeddings = embed_model
        self.vector_db: BaseVectorDB = vector_db

    @staticmethod
    def chunk_docs(source_docs: List[Document]) -> List[Document]:
        chunker = Chunker()
        chunks = chunker.create_chunks(source_docs)
        return chunks

    def create_embeddings(self, chunks) -> None:
        self.vector_db.store(chunks, self.embed_model)
