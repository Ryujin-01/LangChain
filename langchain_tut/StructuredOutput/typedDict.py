from typing import TypedDict


# This is how you define a typed dictionary
class Person(TypedDict):
    name: str
    age: int


# This is how you use the TypedDict
person1: Person = {"name": "Ryu", "age": 21}

# Here we defined the age as a string instead of an integer.
# The problem is that this code will run too without any error.
# Hence TypedDict is only used to tell the programmer the value type of the variable, it does not validate any of them.
person2: Person = {"name": "Jin", "age": "21"}

print(person1["name"])  # This is how to access an element
print(person1, "\n", person2)
