from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.8)
parser = StrOutputParser()

chat_history = []

Template = ChatPromptTemplate(
    [
        (
            "system",
            "You are an Australian pirate expert in {domain}. Give brief answers.",
        ),
        MessagesPlaceholder("history"),
        ("human", "{question}"),
    ]
)
chain = Template | model | parser

domain = input("Domain: ")

print("Type 'exit' to exit the app\n")

while True:
    query = input("Ask: ")
    if query == "exit":
        break
    result = chain.invoke(
        {"domain": domain, "history": chat_history, "question": query}
    )
    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=result))
    print(result)

print(chat_history)
