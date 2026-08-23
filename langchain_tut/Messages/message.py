from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv();

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)

# Messages can help you distinguish between the Human query and AI response, this would be helpful for the AI to maintain context.
chat_history=[
    # Passing a role to the AI
    SystemMessage(content="You are an Australian Pirate. You should talk exactly how an Australian pirate would talk"),
    # Passing the prompt
    HumanMessage(content="Which sport is the best on the Planet ?")
]

results = model.invoke(chat_history)

# Storing the AI result
chat_history.append(AIMessage(results.content))

print(chat_history)