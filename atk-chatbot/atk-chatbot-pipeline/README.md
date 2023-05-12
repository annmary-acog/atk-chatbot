
# atk-chatbot-pipeline

This project assembles the packages atk-converters, atk-embeddings and atk-vectordbs to create a class PipelineRunner that extracts information from various sources, creates embeddings, indexes and stores them. 

category: tech

The atk-chatbot-pipeline uses the ConverterPipeline from the atk-converters package to extract data from sources such as Google Drive folder, website or local directory based on if the path or folder_id of these sources are given in the config file "ingestion_config.yaml". For each of the sources, ConverterPipeline has a separate class that extracts data from them and converts them to Document objects. These Document objects are combined and processed using the EmbeddingsPipeline class from the atk-embeddings package. The functions of this class are applied to the Documents, which creates chunks from the Documents, creates embeddings out of these chunks, indexes the embeddings and finally stores these vector embeddings. The function using the EmbeddingsPipeline takes as inputs the embedding model and the vectordb. By default, the function uses OpenAIEmbeddings() as the embed model and FAISS as the vectordb.
  
  
Created on Tue May  2 11:44:40 IST 2023
  Built with poetry


# Purpose
This project can be used to create a vector database of embeddings which in turn are created by extracting data from google drive, websites and local directories. This database can then be used as the knowledge base to retrieve information from.

# Installation
The libraries required for this package to work are listed in the pyproject.toml file under the tool.poetry.dependencies section. The package can be installed with the command `pip install atk-chatbot-pipeline`

# How to use it
The pipeline can be run with the function call `run_pipeline(config, embed_model, vector_db)` where config is a dictionary created by parsing the ingestion_config.yaml file by the Config library of aganitha_base_utils. This .yaml file contains the paths to each of the sources from which the individual classes extract data from. 'embed_model' is any embedding model of type langchain.embeddings and 'vector_db' is a database class from the atk-vector_dbs package of type BaseVectorDB. By default, the function uses OpenAIEmbeddings() as the embed model and FAISS as the vectordb. E.g. 

`run_pipeline(config=config, embed_model=OpenAIEmbeddings(), vector_db=FaissDB())'`

# Related information
https://python.langchain.com/en/latest/modules/indexes/document_loaders.html

https://python.langchain.com/en/latest/reference/modules/text_splitter.html

https://python.langchain.com/en/latest/modules/indexes/vectorstores.html

https://python.langchain.com/en/latest/reference/modules/embeddings.html

https://python.langchain.com/en/latest/modules/indexes/vectorstores.html

https://python.langchain.com/en/latest/reference/modules/embeddings.html
