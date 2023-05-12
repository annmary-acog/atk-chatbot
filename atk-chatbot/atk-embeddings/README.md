
# atk-embeddings

This package consists of an embeddings pipeline, which takes a list of langchain documents as input, divides it into chunks and creates vector embeddings out of it. It uses the atk-vectordbs package to create and store the vectors. 

category: tech

The atk-embeddings package uses the class `Chunker` to create chunks of size 1024 out of the list of langchain Documents given to it. It then uses a vectorDB class from the atk-extractors package to create, index and store the resulting vector embeddings. Depending on the vectorDB class chosen, it either stores the vector embeddings in a pickle file or cloud. 

  Created on Sun Apr 30 17:10:55 IST 2023
  Built with poetry

# Purpose
Given a list of langchain Documents, this package can be used to create and store vector embeddings. These databases can then be used for the retrieval of relevant information stored in them based on its similarity with the query vector.

# Installation
The libraries required for this package to work are listed in the pyproject.toml file under the tool.poetry.dependencies section. The package can be installed with the command `pip install atk-embeddings`

# How to use it
The pipeline can be run with the function call `run_pipeline(source_docs: List[Document], embed_model: embeddings, vector_db: BaseVectorDB)`

where source_docs is a list of langchain Documents, embed_model is any embedding model of type langchain.embeddings and vector_db is a database class from the atk-vector_dbs package of type BaseVectorDB. By default, the function uses OpenAIEmbeddings() as the embed model and FAISS as the vectordb. E.g.

`run_pipeline(docs = docs, embed_model = OpenAIEmbeddings(), vector_db = FaissDB())`


# Related information
https://python.langchain.com/en/latest/reference/modules/text_splitter.html

https://python.langchain.com/en/latest/modules/indexes/vectorstores.html

https://python.langchain.com/en/latest/reference/modules/embeddings.html
