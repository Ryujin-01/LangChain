from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.5)
parser = StrOutputParser();

chain = model | parser

chat_history=[
    SystemMessage(content="You are an Australian Pirate. You should talk exactly how an Australian pirate would talk"),
]


while True:
    user_query = input("You: ")
    if(user_query == "exit"):
        print("\nGoodbye :)\n")
        break
    chat_history.append(HumanMessage(content=user_query))
    result = chain.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("AI: ", result, "\n")

print(chat_history)