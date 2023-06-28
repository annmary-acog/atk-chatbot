from atk_embeddings.pipeline import EmbeddingsPipeline
from langchain import embeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from atk_vectordbs.vector_dbs import BaseVectorDB, FaissDB
from langchain.docstore.document import Document
from typing import List
import typer


def run_pipeline(source_docs: List[Document], embed_model: embeddings = OpenAIEmbeddings(), vector_db: BaseVectorDB = FaissDB(), pickle_file: str = typer.Option(None)):
    pipe = EmbeddingsPipeline(embed_model=embed_model, vector_db=vector_db)
    chunks = pipe.chunk_docs(source_docs)
    pipe.create_embeddings(chunks, pickle_file)
