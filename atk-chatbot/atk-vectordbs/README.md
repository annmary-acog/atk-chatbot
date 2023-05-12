
# atk-vectordbs

This library contains the classes FaissDB and MilvusDB, both of which take an embedding model and a list of Document objects as input to create, index and store the resulting vectors.   

category: tech


  The classes FaissDB and MilvusDB inherit from an Abstract Base Class called BaseVectorDB which consists of an abstractmethod `store`. The class FaissDB uses FAISS from langchain.vectorstores to create, index and store vectors based on the embedding model and list of Documents given to it. It then creates a pickle file and dumps the vectors into it.
The class MilvusDB uses a customised version of Milvus from langchain.vectorstores to create, index and store vectors. The customised Milvus class is in milvus.py. The `store` function of MilvusDB takes the same inputs as FaissDB. Since Milvus stores vectors in cloud, it also takes in some arguments for cloud connection. The embedding vectors are then created, indexed and stored.

  Created on Sun Apr 30 16:52:41 IST 2023
  Built with poetry

# Purpose
The classes in this package can be used to create and store vector embeddings from chunks of langchain Documents. These databases can then be used for the retrieval of relevant information stored in them based on its similarity with the query vector.

# Installation

The libraries required for this code to work are given in the tool.poetry.dependencies section of the pyproject.toml file. This package can be installed with the command `pip install atk-vectordbs`.

# How to use it

To run the code,

`vector_db.store(chunks: List[Document], embed_model: embeddings)` 

where vector_db is of type BaseVectorDB and can be either FaissDB() or MilvusDB(), chunks is a list of langchain Documents and embed_model is any embedding model of type langchain.embeddings. By default, the function uses OpenAIEmbeddings() as the embed model.
E.g. 

`FaissDB.store(chunks, embed_model)`

`MilvusDB.store(chunks, embed_model)`

# Related information
https://python.langchain.com/en/latest/modules/indexes/vectorstores.html

https://python.langchain.com/en/latest/reference/modules/embeddings.html