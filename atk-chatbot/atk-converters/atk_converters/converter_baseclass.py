from abc import ABC, abstractmethod
from atk_converters.gdriveloader import GDriveLoader
from atk_converters.video_extractor import VideoExtractor
from atk_converters.directory_documents_extractor import DirectoryExtractor
from atk_converters.website_extractor import WebsiteExtractor
from langchain.docstore.document import Document
from typing import List, Dict


class BaseConverter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load(self, config: Dict[str, str]) -> List[Document]:
        pass


class GDrive(BaseConverter):
    def load(self, config: Dict[str, str]) -> List[Document]:
        gdrive = GDriveLoader(folder_id=config['FOLDER_ID'], shared_dir=config['VIDEO_DIRECTORY'])
        gdrive_docs = gdrive.load()
        return gdrive_docs


class Video(BaseConverter):
    def load(self, config: Dict[str, str]) -> List[Document]:
        video_knowledge = VideoExtractor(config['VIDEO_DIRECTORY'])
        video_docs = video_knowledge()
        return video_docs


class Directory(BaseConverter):
    def load(self, config: Dict[str, str]) -> List[Document]:
        directory_docs = []
        for path in config['KNOWLEDGE_DIRECTORY']:
            directory_docs = DirectoryExtractor.directory_loader(path)
            directory_docs.extend(directory_docs)
        return directory_docs


class Website(BaseConverter):
    def load(self, config: Dict[str, str]) -> List[Document]:
        website_docs = []
        for website in config['WEBSITE_URLS']:
            website_docs = WebsiteExtractor.website_loader(website)
            website_docs.extend(website_docs)
        return website_docs

