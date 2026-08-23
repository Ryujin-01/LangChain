from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

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

# NOTE: Here we are using the "from_documents" method. It loads the documents while initialising.
# Also we are not specifying a directory for the vector store hence it will be stored in the RAM.
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    collection_name="example_collection",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

query = input("Ask: ")

result = retriever.invoke(query)

for i, doc in enumerate(result):
    print("Result ", i + 1, ":\n", doc, "\n\n")
