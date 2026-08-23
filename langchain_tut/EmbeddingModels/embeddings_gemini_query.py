from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv();

# Setting up the embedding model
# Dimensions represents the size of the vector that will be generated for each input text.
# A smaller dimension means a more compact representation, while a larger dimension can capture more nuances but may require more computational resources.
# In this case, we are using a dimension of 32, which is relatively small and may be suitable for simple tasks or when computational efficiency is a concern.
embedding_model = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2-preview", dimensions = 32)

text = "What is the capital of France?"

embedding = embedding_model.embed_query(text)
print(embedding)
