from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Import the chat history 
from chat_history import saved_history

# Setting up the placeholder
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer care assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{query}")
])

# Pass the saved_history and finalise the prompt
formatted_history = chat_template.invoke({"query": "Where is my product ?", "history":saved_history})

print(formatted_history)