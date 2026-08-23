from langchain_core.tools import tool


# We can also use other methods to define a tool
@tool
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers"""
    return a * b


# A toolkit becomes really necessary when we bind it with an LLM
class MathToolKit:
    # This "get_tools" name is not necessary, we can give this function any other name and then later use it
    def get_tools(self):
        return [add, multiply]


toolkit = MathToolKit()
tools = toolkit.get_tools()

for tool in tools:
    print("Name: ", tool.name)
    print("Description: ", tool.description, "\n")
