import os
os.environ["HF_HOME"] = "C:/A/Coding/LangChain/huggingface_cache"

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv();

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "What is the capital of France?"

embeddings = embeddings.embed_query(text)
print(embeddings)