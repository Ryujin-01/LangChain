# This is a special type of tool where the input to the tool follows a structured schema, typically defined using a Pydantic model.

from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool


# Defining the structure
class MultiplyStructure(BaseModel):
    a: int = Field(description="The first number to add")
    b: int = Field(description="The second number to add")


# Defining the function
# Here we are not using type hints because we already defined it's structure in the Pydantic model.
# We are also not giving any description cause we'll give it later
def MultiplyFunction(a, b) -> int:
    return a * b


# Defining our tool
multiply = StructuredTool.from_function(
    name="multiply",
    description="Multiplies two numbers",
    func=MultiplyFunction,
    args_schema=MultiplyStructure,
)

a = input("a: ")
b = input("b: ")

result = multiply.invoke({"a": a, "b": b})
print("Result: ", result)

print("Name: ", multiply.name)
print("Description: ", multiply.description)
print("Arguments: ", multiply.args)
print("Schema: ", multiply.args_schema.model_json_schema())
