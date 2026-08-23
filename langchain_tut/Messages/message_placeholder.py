from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Setting up the placeholder
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer care assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{query}")
])

# Loading the chat history
history = []
with open(r"C:/A/Coding/LangChain/langchain/Messages/chat_history.txt") as f:
    for line in f:
        # Clean up whitespace and ignore empty lines
        line = line.strip()
        if line:
            # Remove the trailing comma from your text file lines so eval() doesn't get confused
            if line.endswith(","):
                line = line[:-1]
            
            # eval() magically turns your text string into the actual LangChain object!
            message_object = eval(line)
            history.append(message_object)

# Final prompt
formatted_history = chat_template.invoke({"query": "Where is my product ?", "history":history})

print(formatted_history)