# This code sets up a local Hugging Face model for chat-based interactions using the LangChain library. 

# Python has a built-in library called os (which stands for Operating System). 
# Importing this gives your Python script permission to talk directly to your Windows computer, allowing it to read or change system-level settings, create folders, or look at file paths.
# NOTE: This path must be set befor importing the Hugging Face library, otherwise it will download the model to the default location and not your custom folder.
import os 

# os.environ: This is a dictionary inside the os library that holds all of your computer's current Environment Variables.
# ["HF_HOME"]: This targets the specific variable that Hugging Face looks for to know where to download massive model files.
# = "file path": This overwrites whatever the default value was and points it to your custom folder.
os.environ["HF_HOME"] = "C:/A/Coding/LangChain/huggingface_cache"

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv();

# Setting up the llm
LLM = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs=dict(
        temperature = 1,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm = LLM)

prompt = input("Ask: ")
result = model.invoke(prompt)
print(result.content)