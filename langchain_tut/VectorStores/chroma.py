from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

docs = [
    Document(
        page_content="""
        Football is a team sport played between two teams of eleven players.
        The objective is to score more goals than the opposing team.
        A standard match consists of two 45-minute halves.
        """,
        metadata={"topic": "football", "id": 1},
    ),
    Document(
        page_content="""
        Lionel Messi is an Argentine footballer known for his dribbling,
        close control, passing, creativity, and goalscoring ability.
        He has won numerous individual and team awards during his career.
        """,
        metadata={"topic": "football_players", "id": 2},
    ),
    Document(
        page_content="""
        Cricket is played between two teams, usually consisting of eleven
        players each. The batting team attempts to score runs while the
        bowling and fielding team tries to prevent runs and take wickets.
        """,
        metadata={"topic": "cricket", "id": 3},
    ),
    Document(
        page_content="""
        Basketball is played between two teams that attempt to score points
        by putting the ball through the opponent's hoop. Players can pass,
        dribble, shoot, and defend throughout the game.
        """,
        metadata={"topic": "basketball", "id": 4},
    ),
    Document(
        page_content="""
        Python is a high-level programming language known for its simple
        syntax and extensive ecosystem of libraries. It is commonly used
        for web development, automation, data analysis, and artificial intelligence.
        """,
        metadata={"topic": "programming", "id": 5},
    ),
    Document(
        page_content="""
        Machine learning is a branch of artificial intelligence where models
        learn patterns from data. Supervised learning uses labeled examples,
        while unsupervised learning attempts to discover patterns in unlabeled data.
        """,
        metadata={"topic": "machine_learning", "id": 6},
    ),
    Document(
        page_content="""
        Vector embeddings represent text as numerical vectors. Texts with
        similar meanings generally produce vectors that are close to each
        other in the embedding space.
        """,
        metadata={"topic": "embeddings", "id": 7},
    ),
    Document(
        page_content="""
        A vector database stores embeddings and allows applications to
        perform similarity searches. It can retrieve documents whose
        embeddings are most similar to a query embedding.
        """,
        metadata={"topic": "vector_database", "id": 8},
    ),
    Document(
        page_content="""
        Retrieval-Augmented Generation, or RAG, combines information
        retrieval with a language model. Relevant documents are retrieved
        from a knowledge base and provided to the language model as context.
        """,
        metadata={"topic": "rag", "id": 9},
    ),
    Document(
        page_content="""
        Renewable energy comes from naturally replenishing sources such as
        sunlight, wind, flowing water, and geothermal heat. Solar panels
        convert sunlight into electricity, while wind turbines convert
        wind energy into electrical power.
        """,
        metadata={"topic": "renewable_energy", "id": 10},
    ),
]

# "embedding_function" tells which embedding model to use
# "collection_name" specifies the name of the collection under which the embeddings will be generated.
# "persist_directory" specifies the directory path to store the database. We can remove it if not necessary. Then it will be stored in RAM.
vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    collection_name="example_collection",
    persist_directory="./VectorStores/chroma_database",
)

ids = []
for doc in docs:
    ids.append(str(doc.metadata["id"]))

# We are explicitly giving an id to each document because when we run this code again, we don't want the same document to be added again.
# Before adding documents, Chroma checks whether a document with and id already exists in the database. If yes then it will not add it again.
# If we do not give id's to the document, then Chroma will generate random id's for each document and while running the code again, each document will be added again because each id is randomly generated.
vector_store.add_documents(documents=docs, ids=ids)

query = input("Ask: ")

# # Here k=2 means return top '2' similar documents
# This will give us similar documents with their similarity score
result = vector_store.similarity_search_with_score(query=query, k=2)

# We can also use this code if we don't want the similarity score.
# result = vector_store.similarity_search(query=query, k=2)

for i in result:
    print(i)

# Used to see the details about the database.
print(vector_store.get(include=["documents", "embeddings", "metadatas"]))

# We can also do filtering in simialrity searches.
print(
    vector_store.similarity_search_with_score(
        query=" ", filter={"topic": "machine_learning"}, k=2
    )
)

# This is how to update a document
updated_document = Document(
    page_content="This is the updated document.",
    metadata={"topic": "testing"},  # The id will remain the same
)
vector_store.update_document(document_id="10", document=updated_document)
print(vector_store.get(include=["documents", "metadatas"]))

# This is how to delete a document
vector_store.delete(ids="10")
print(vector_store.get(include=["documents", "metadatas"]))
