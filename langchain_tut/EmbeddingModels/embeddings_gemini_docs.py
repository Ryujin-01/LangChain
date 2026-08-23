from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv();

# Setting up the embedding model
# Dimensions represents the size of the vector that will be generated for each input text.
# A smaller dimension means a more compact representation, while a larger dimension can capture more nuances but may require more computational resources.
# In this case, we are using a dimension of 128, which is relatively large and may be suitable for complex tasks or when capturing detailed information is important.
embedding_model = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2-preview", dimensions = 128)

docs = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome.",
    "The capital of Spain is Madrid."
]

embedding = embedding_model.embed_documents(docs)
print(str(embedding))
