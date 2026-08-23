from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.8)

parser = StrOutputParser()

chain = model | parser

chat_history = []

# This model has basic memory.
# We are storing all the chat in the chat_history and giving the entire history to the LLM so that it can have some context.
while True:
    user_input = input("You: ")
    if(user_input == "exit"):
        print("Goodbye :)")
        break
    chat_history.append(user_input)
    result = chain.invoke(chat_history)
    print("Buddy: ", result, "\n")
    chat_history.append(result)

print(chat_history)