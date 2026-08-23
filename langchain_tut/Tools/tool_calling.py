from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

load_dotenv()


# Creating our tool here
@tool
def clown_add(a: int, b: int) -> int:
    """Takes two integers a and b and concatenates them to return ab"""
    s = str(a) + str(b)
    return int(s)


# Defining an llm
llm_model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

# Binding our tool with the llm
# We can give multiple tools to bind with the llm
llm_with_tools = llm_model.bind_tools([clown_add])

# Here we can see that the llm did not call the tool as the query does not require that.
print(llm_with_tools.invoke("Hello how are you ?").content, "\n")

a = input("a: ")
b = input("b: ")
query = f"Clown add these two numbers: {a} {b}"
print(query)

tool_call_result = llm_with_tools.invoke(query)

# Here we can see that the content is empty. Instead the llm is suggesting us to call the "clown_add" tool
print(tool_call_result, "\n")

# We can also fetch the tool calls. It returns a list of all the tool calls suggested.
print(tool_call_result.tool_calls, "\n")


# This is how we can execute the tool call

# Passing the arguments will only give us the results.
print(clown_add.invoke(tool_call_result.tool_calls[0]["args"]), "\n")

# But passing the whole tool call will give us a nice ToolMessage with the content and all the metadata inside.
# This one is more preferred
result = clown_add.invoke(tool_call_result.tool_calls[0])

print(result, "\n")


# How to do all that in one go
# The first one is HumanMessage, the second one is AIMessage, and the third one is "ToolMessage"
history = [HumanMessage(query), tool_call_result, result]

print(history)

final_response = llm_with_tools.invoke(history)

# This is the desired response from the LLM
print(final_response.content)
