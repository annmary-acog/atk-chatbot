
# atk-converters

This package consists of four classes which extracts documents from four different sources and converts them to langchain documents.

category: tech

The atk-converters has a Pipeline class which brings together four different classes that extract data from different sources and converts them to langchain documents. These documents are combined and returned by the Pipeline class. The extractor classes are called only if the path to the sources are provided in the config file "ingestion_config.yaml". The four different classes are:

GDriveLoader: This class inherits from the BaseLoader class of langchain.document_loaders. On receiving a folder_id or file_id from the config file, it checks if the user is authorized to access this folder. If yes, it gets all the file MIME types from the directory. Based on if the MIME type is a document, spreadsheet, presentation, or pdf it calls the respective loader to convert the files to Document objects. If the MIME type is none of the above, the unstructured_dataloader is called. This function downloads and stores all the videos in that folder in a specific directory mentioned in the config file, while the other MIME types are downloaded and the unstructured_data_loader function tries to process those file types. The file types that are successfully processed will also be converted to Document objects. In case the input folder contains another folder within it, the whole process is repeated on that folder, until there are no more folders left. All the above Document objects are combined and returned by the class.

VideoExtractor:

DirectoryExtractor: The DirectoryExtractor uses the DirectoryLoader from langchain.document_loaders to load all the files residing in the path specified in the config file. It then returns these loaded files which are of type langchain Documents.

WebsiteExtractor: The WebsiteExtractor class uses the `crawl` function to crawl through the website given in the config file to get a list of all the hyperlinks present in that website. It then parses this list of websites to create Document objects out of it using the WebBaseLoader from langchain.document_loaders and returns them. The `crawl` function generates the list of hyperlinks from the website by creating a queue containing a set of the visited hyperlinks. It does this by employing functions to get all the links in the website and filtering these links by eliminating all the links that do not contain text/html content as well as the ones ending with image extensions. The domain of the original website are then attached to those links which do not have the full path. The crawl function repeats this process for every hyperlink that it comes across in the original website.
  

  Created on Sun Apr 30 17:55:24 IST 2023
  Built with poetry

# Purpose
This package can be used to create langchain Document objects from most types of files in Google Drive, the local directory and from websites. These Documents can then serve as a knowledge base for various other applications such as a chatbot.

# Installation
The libraries required for this code to work are given in the tool.poetry.dependencies section of the pyproject.toml file. This package can be installed with the command pip install atk-converters. 

Prerequisites for using the GdriveLoader class:
1. Create a Google Cloud project
2. Enable the Google Drive API: https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com
3. Authorize credentials for desktop app: https://developers.google.com/drive/api/quickstart/python#authorize_credentials_for_a_desktop_application # noqa: E501
4. For service accounts visit https://cloud.google.com/iam/docs/service-accounts-create

Prerequisite for using the VideoExtractor class:

Whisper: This automatic speech recognition system is required for the transcription of video files and can be installed using the command `pip install git+https://github.com/openai/whisper.git`

# How to use it
The pipeline can be run with the function call `run_pipeline(config: Dict[str, str] = config)` where config is a dictionary created by parsing the ingestion_config.yaml file by the Config library of aganitha_base_utils. This .yaml file contains the paths to each of the sources from which the individual classes extract data from. The function returns a list of the combined Document objects from each source.  

# Related information
https://python.langchain.com/en/latest/modules/indexes/document_loaders.html
