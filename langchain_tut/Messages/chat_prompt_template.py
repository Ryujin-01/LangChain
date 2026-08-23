from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# This is used to pass dynamic prompt to chatbots

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful AI expert in {domain}"),
#     HumanMessage(content="Explain what is {topic}")
# ])

# This is wrong because:
# In LangChain, a standard SystemMessage or HumanMessage is completely static. It expects a finished string.
# If you put {domain} inside a SystemMessage, LangChain doesn't know it's a variable; it literally just prints the characters {domain}.

# This is the right way
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful AI expert in {domain}"),
    ("human", "Explain what is {topic}")
])

formatted_prompt = chat_template.invoke({"domain":"Football", "topic":"knuckleball"})

print(formatted_prompt)