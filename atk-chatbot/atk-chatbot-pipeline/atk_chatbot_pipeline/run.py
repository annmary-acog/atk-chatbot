from atk_chatbot_pipeline.pipeline import PipelineRunner
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import embeddings
from atk_vectordbs.vector_dbs import BaseVectorDB, FaissDB, MilvusDB
import typer
import os
os.environ['ATK_CONFIG_PATH'] = '../config'
from aganitha_base_utils import Config


config = Config().params('ingestion_config')
app = typer.Typer()


@app.command()
def run_pipeline(embeds: str = "OPENAI", vectordb: str = "FAISS"):
    """ Pipeline is called which pulls the data from all the resources we specify"""
    if embeds == "OPENAI":
        embed_model: embeddings = OpenAIEmbeddings()
    if vectordb == "FAISS":
        vector_db: BaseVectorDB = FaissDB()
    elif vectordb == "MILVUS":
        vector_db: BaseVectorDB = MilvusDB()

    pipe = PipelineRunner()
    pipe.create_docs(config)
    pipe.create_embeddings(embed_model=embed_model, vector_db=vector_db)


def main():
    app()
