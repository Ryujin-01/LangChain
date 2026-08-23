# Base tool is the abstract base class for all the tools in LangChain.
# It defines the core structure and interface that any tool must follow.

from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
from typing import Type


# Defining the structure
class MultiplyStructure(BaseModel):
    a: int = Field(description="The first number to add")
    b: int = Field(description="The second number to add")


# Defining the BaseTool
# We can do deep level customizations here, like defining asychronous funtions etc.
class multiply_tool(BaseTool):
    name: str = "multiply"
    description: str = "Multiplies two numbers"
    args_schema: Type[BaseModel] = MultiplyStructure

    # NOTE: We need to name this function "_run" or it won't work
    def _run(self, a, b) -> int:
        return a * b


multiply = multiply_tool()

a = input("a: ")
b = input("b: ")

result = multiply.invoke({"a": a, "b": b})
print("Result: ", result)

print("Name: ", multiply.name)
print("Description: ", multiply.description)
print("Arguments: ", multiply.args)
print("Schema: ", multiply.args_schema.model_json_schema())
