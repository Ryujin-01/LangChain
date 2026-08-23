from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_classic.retrievers.contextual_compression import (
    ContextualCompressionRetriever,
)
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(
        page_content="""
        The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years.
        """,
        metadata={"source": "Doc1"},
    ),
    Document(
        page_content="""
        In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls.
        """,
        metadata={"source": "Doc2"},
    ),
    Document(
        page_content="""
        Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets.
        NBA is now a global league.
        """,
        metadata={"source": "Doc3"},
    ),
    Document(
        page_content="""
        The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design.
        """,
        metadata={"source": "Doc4"},
    ),
]

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    collection_name="example_collection",
)

query = "Explain Photosynthesis"

# Setting up the base retriever
# Here the base retriever will return top k documents to the compression retriever to compress.
base_retriever = vector_store.as_retriever(
    search_type="similarity", search_kwargs={"k": 2}
)

# Setting up the compressor
# LLMChainExtractor is a LangChain component that uses an LLM to extract the portions of a document that are relevant to a query.
LLM = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
compressor = LLMChainExtractor.from_llm(LLM)

retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor,
)

# Results from normal similarity search
result1 = base_retriever.invoke(query)

# Results from contextula compression retriever.
result2 = retriever.invoke(query)

print("Using Similarity Search:")
for i, doc in enumerate(result1):
    print("Document ", i + 1, ":\n", doc, "\n\n")

print("Using Retriever:")
for i, doc in enumerate(result2):
    print("Document ", i + 1, ":\n", doc, "\n\n")
