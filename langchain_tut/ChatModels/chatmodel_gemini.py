from langchain_google_genai import ChatGoogleGenerativeAI # To import the google package of langchain
from dotenv import load_dotenv # This package is imported to read the .env file

load_dotenv(); # reading the .env file

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5) # Loading the model. 
# Temperature parameter adjusts the randomness or creativity of the response. temperature = 0, means no creativity, and temperature = 1.5+ means a lot of creativity.

prompt = input("Ask: ") # Asking for the prompt
 
result = model.invoke(prompt) # Storing the result of the prompt from the ChatModel

print(result.content); # Printing the content of the result as result contains a lot of things.