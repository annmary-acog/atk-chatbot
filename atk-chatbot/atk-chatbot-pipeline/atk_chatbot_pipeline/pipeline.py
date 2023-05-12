from langchain.docstore.document import Document
from atk_converters.pipeline import ConverterPipeline
from atk_embeddings.pipeline import EmbeddingsPipeline
from langchain import embeddings
from atk_vectordbs.vector_dbs import BaseVectorDB
from typing import List, Dict


class PipelineRunner:
    def __init__(self):
        self.source_docs: List[Document] = []

    def create_docs(self, config: Dict[str, str]) -> None:
        pipe = ConverterPipeline()
        if config['FOLDER_ID']:
            pipe.gdrive_to_docs(config)
        if config['VIDEO_DIRECTORY']:
            pipe.video_to_docs(config)
        if config['KNOWLEDGE_DIRECTORY']:
            pipe.directory_to_docs(config)
        if config['WEBSITE_URLS']:
            pipe.websites_to_docs(config)
        self.source_docs = pipe.source_docs

    def create_embeddings(self, embed_model: embeddings, vector_db: BaseVectorDB):
        pipe = EmbeddingsPipeline(embed_model=embed_model, vector_db=vector_db)
        chunks = pipe.chunk_docs(self.source_docs)
        pipe.create_embeddings(chunks)
