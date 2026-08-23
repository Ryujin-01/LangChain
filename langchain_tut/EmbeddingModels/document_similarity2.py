from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensions=128)

document = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome.",
    "The capital of Spain is Madrid.",
]

doc_embeddings = model.embed_documents(document)

query = ["What is the capital of France ?", "What is the capital of Spain ?"]

query_embeddings = model.embed_documents(query)

scores = cosine_similarity(query_embeddings, doc_embeddings)

print(scores)

index1, score1 = sorted(list(enumerate(scores[0])), key=lambda x: x[1])[-1]
index2, score2 = sorted(list(enumerate(scores[1])), key=lambda x: x[1])[-1]

print(document[index1], "The similarity is", score1)
print(document[index2], "The similarity is", score2)
