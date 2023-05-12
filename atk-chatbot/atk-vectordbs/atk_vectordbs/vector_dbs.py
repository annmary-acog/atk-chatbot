from langchain.docstore.document import Document
from langchain.vectorstores import FAISS
from atk_vectordbs.milvus import Milvus
from abc import ABC, abstractmethod
from langchain import embeddings
from typing import List
import pickle
import logging
import warnings
import os

warnings.filterwarnings("ignore")
logging.basicConfig(level='INFO')


class BaseVectorDB(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def store(self, chunks: List[Document], embed_model: embeddings) -> None:
        pass


class FaissDB(BaseVectorDB):
    def store(self, chunks: List[Document], embed_model: embeddings) -> None:
        faiss_index = FAISS.from_documents(chunks, embed_model)
        with open("faiss_index.pickle", "wb") as f:
            pickle.dump(faiss_index, f)
        logging.info("FAISS search_index created")


class MilvusDB(BaseVectorDB):
    def store(self, chunks: List[Document], embed_model: embeddings) -> None:
        connection_args = {
            "alias": "default",
            "uri": "https://in01-84cae738bde3a79.aws-us-west-2.vectordb.zillizcloud.com:19541",
            "secure": True,
            "user": os.getenv("MILVUS_USER"),
            "password": os.getenv("MILVUS_PASSWORD")
        }
        Milvus.from_documents(chunks, embed_model, connection_args=connection_args,)
        logging.info("MILVUS index created")