from atk_converters.converter_baseclass import GDrive
from atk_converters.converter_baseclass import Video
from atk_converters.converter_baseclass import Directory
from atk_converters.converter_baseclass import Website
from langchain.docstore.document import Document
from typing import List, Dict


class ConverterPipeline:
    def __init__(self):
        self.source_docs: List[Document] = []

    def gdrive_to_docs(self, config: Dict[str, str]) -> None:
        gdrive = GDrive()
        gdrive_docs = gdrive.load(config)
        self.source_docs.extend(gdrive_docs)

    def video_to_docs(self, config: Dict[str, str]) -> None:
        video = Video()
        video_docs = video.load(config)
        self.source_docs.extend(video_docs)

    def directory_to_docs(self, config: Dict[str, str]) -> None:
        directory = Directory()
        directory_docs = directory.load(config)
        self.source_docs.extend(directory_docs)

    def websites_to_docs(self, config: Dict[str, str]) -> None:
        website = Website()
        website_docs = website.load(config)
        self.source_docs.extend(website_docs)
