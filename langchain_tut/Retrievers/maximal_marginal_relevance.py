from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(
        page_content="Teams can improve football performance by improving their passing accuracy and maintaining possession."
    ),
    Document(
        page_content="Better passing and ball possession can significantly improve a football team's performance."
    ),
    Document(
        page_content="Successful teams improve performance through accurate short passes and maintaining control of possession."
    ),
    Document(
        page_content="Football teams can improve performance through fitness training, sprinting ability, endurance, and recovery."
    ),
    Document(
        page_content="Analytics can improve football performance by identifying weaknesses, evaluating expected goals, and analyzing player movements."
    ),
    Document(
        page_content="Defensive organization can improve team performance by reducing spaces and preventing opponents from creating chances."
    ),
]

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    collection_name="example_collection",
)

# In "search_type" we can specify different types of search algorithms for the retriever, "similarity" being one of them. Here we are using mmr.
# "fetch_k" first selects most relevant documents (whatever it is set) and then "k" gives the top most documents. It is better to use "fetch_k" as it gives the mmr bigger pool to choose from.
# "lambda_mult" is a type of multiplier where "0" means huge diversity in results and "1" means least diversity (basically similarity search) in results.

retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"fetch_k": 5, "k": 3, "lambda_mult": 0.5}
)

query = "How do football teams improve their performance?"

# Results by using similarity search
result1 = vector_store.similarity_search(query, k=3)

# Results by using retriever
result2 = retriever.invoke(query)

print("Using Similarity Search:")
for i, doc in enumerate(result1):
    print("Document ", i + 1, ":\n", doc, "\n\n")

print("Using Retriever:")
for i, doc in enumerate(result2):
    print("Document ", i + 1, ":\n", doc, "\n\n")
