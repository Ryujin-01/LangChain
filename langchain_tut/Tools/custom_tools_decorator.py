# By using custom tools, we can define our own tools

from langchain_core.tools import tool

# Just use "@tool" above the function to make it a LangChain tool

# @tool
# def multiply(a, b):
#     return a * b

# This works completely fine, however this is not the recommended approach to define a tool


# This is the recommended way to define a tool
# Here we gave type hints to our variables and also gave the description inside the docstrings.
# These help the LLM to get to know our tool better.


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers"""
    return a * b


a = input("a: ")
b = input("b: ")

# A tool is also a runnable hence we can use it with other runnables and also use the methods of runnables.
result = multiply.invoke({"a": a, "b": b})
print("Result: ", result)

# Gives the name of the tool, in this case it is the name of the function
print("Name: ", multiply.name)

# Gives the description of the tool, here it is the description we gave in the docstrings
print("Description: ", multiply.description)

# Gives the arguments of the tool
print("Arguments: ", multiply.args)

# Give the JSON schema that is given to the LLM
print("Schema: ", multiply.args_schema.model_json_schema())
