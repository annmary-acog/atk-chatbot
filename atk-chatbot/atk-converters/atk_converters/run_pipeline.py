from atk_converters.pipeline import ConverterPipeline
from langchain.docstore.document import Document
from typing import List
import typer
import os
os.environ['ATK_CONFIG_PATH'] = '../config'
from aganitha_base_utils import Config


config = Config().params('ingestion_config')
app = typer.Typer()


@app.command()
def run_pipeline() -> List[Document]:
    pipe = ConverterPipeline()
    if config['FOLDER_ID']:
        pipe.gdrive_to_docs(config)
    if config['VIDEO_DIRECTORY']:
        pipe.video_to_docs(config)
    if config['KNOWLEDGE_DIRECTORY']:
        pipe.directory_to_docs(config)
    if config['WEBSITE_URLS']:
        pipe.websites_to_docs(config)
    return pipe.source_docs


def main():
    app()
