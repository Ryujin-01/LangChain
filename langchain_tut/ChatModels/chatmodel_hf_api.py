# This code sets up a Hugging Face model for chat-based interactions using the LangChain library, specifically utilizing the Hugging Face API.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Setting up the LLM (Language Model) using the Hugging Face Endpoint.
# The repo_id specifies which model to use, task specifies the type of task (in this case, text generation), temperature controls the creativity of the response, and max_new_tokens limits the length of the generated response.
LLM = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    temperature=1,
    max_new_tokens=200 # Generates the response within the given amomunt of tokens
)

model = ChatHuggingFace(llm=LLM)
prompt = input("Ask: ")
result = model.invoke(prompt)

print(result.content)