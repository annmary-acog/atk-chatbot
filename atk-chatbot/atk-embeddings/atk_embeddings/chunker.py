from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from typing import List
import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(level='INFO')


class Chunker:
    def __init__(self):
        self.splitter = CharacterTextSplitter(separator=" ", chunk_size=1024, chunk_overlap=0)

    def create_chunks(self, source_docs: List[Document]) -> List[Document]:
        chunks = []
        for doc in source_docs:
            for chunk in self.splitter.split_text(doc.page_content):
                chunks.append(Document(page_content=chunk, metadata=doc.metadata))
        return chunks
