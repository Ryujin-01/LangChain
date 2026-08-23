from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(
        page_content="Regular walking boosts heart health and can reduce symptoms of depression.",
        metadata={"source": "H1"},
    ),
    Document(
        page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.",
        metadata={"source": "H2"},
    ),
    Document(
        page_content="Deep sleep is crucial for cellular repair and emotional regulation.",
        metadata={"source": "H3"},
    ),
    Document(
        page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.",
        metadata={"source": "H4"},
    ),
    Document(
        page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.",
        metadata={"source": "H5"},
    ),
    Document(
        page_content="The solar energy system in modern homes helps balance electricity demand.",
        metadata={"source": "I1"},
    ),
    Document(
        page_content="Python balances readability with power, making it a popular system design language.",
        metadata={"source": "I2"},
    ),
    Document(
        page_content="Photosynthesis enables plants to produce energy by converting sunlight.",
        metadata={"source": "I3"},
    ),
    Document(
        page_content="The 2022 FIFA World Cup was held in Qatar and drew global attention and excitement.",
        metadata={"source": "I4"},
    ),
    Document(
        page_content="Black holes bend spacetime and store immense gravitational energy.",
        metadata={"source": "I5"},
    ),
]

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    collection_name="example_collection",
)

query = "I feel very low energy. How to balance it ?"

# NOTE: MultiQureyRetriever does not have a simple "k" argument that we can set to get top k most relevant documents.
multi_query_retriever = MultiQueryRetriever.from_llm(
    # Here k = 3 means that for each query that the llm generates, retriever will take the top 3 most relevant documents.
    # e.g. If the llm generates 5 queries, then retriever will give total 5*3=15 documents.
    # Now the MultiQueryRetriever will remove the duplicates and give the remaining ones.
    # Hence if we need top k documents from multiquery retriever, we need to remove it from the resuts itself.
    retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
    llm=ChatGoogleGenerativeAI(model="gemini-3-flash-preview"),
)

# Results from normal similarity search
result1 = vector_store.similarity_search(query, k=5)

# Results from multi query retriever.
result2 = multi_query_retriever.invoke(query)

print("Using Similarity Search:")
for i, doc in enumerate(result1):
    print("Document ", i + 1, ":\n", doc, "\n\n")

print("Using Retriever:")
for i, doc in enumerate(result2):
    print("Document ", i + 1, ":\n", doc, "\n\n")
