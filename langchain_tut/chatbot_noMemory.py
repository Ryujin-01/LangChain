from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.8)

parser = StrOutputParser()

chain = model | parser

# This model has no context/memory.
while True:
    user_input = input("You: ")
    if(user_input == "exit"):
        print("Goodbye :)")
        break
    result = chain.invoke(user_input)
    print("AI: ", result)

