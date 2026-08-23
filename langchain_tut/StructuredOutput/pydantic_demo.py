from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# Pydantic validates the code at runtime, something that TypeDict does not do.
# If you pass wrong value to some field, the code will throw an error.
class Student(BaseModel):
    # If you pass anything other that string, the code will throw an error.
    name: str

    # This way you can pass default values to the field
    age: int = 21

    # This is how you pass optional fields, if this field is not passed the code will return none.
    gender: Optional[str] = None

    # Buitlin Validation
    # This is a builtin data type in pydantic that will validate whether the passed value is an email or not
    email: Optional[EmailStr] = None

    # the Field function is the primary tool for adding extra information and strict validation rules to a single field within a model.
    # ge (greater than or equal to), gt(greater than), similarily le and lt.
    # default: We can set a default value for the field.
    # description: We can add a description for the LLM. Similar to Annotations in TypeDict
    cgpa: float = Field(
        ge=0,
        le=10,
        default=5,
        description="A decimal value representing the score of the student",
    )

    # pattern: We can set strict formatting rules for the LLM
    # Must be exactly 3 uppercase letters, a dash, 4 digits, a dash, 2 uppercase letters
    roll_no: str = Field(
        pattern=r"^[A-Z]{3}-\d{4}-[A-Z]{2}$",
        description="The standardized roll number of the student",
        default="AAA-0000-AA",
    )


student_A = {"name": "Ryu", "age": 25}

# If we pass this dictionary, then the code will throw an error
student_B = {"name": 23}

# If a field is not passed, it will show its default value
student_C = {"name": "Jin"}

# Type coercion
# If possible, pydantic will try to do data conversion to the correct field type
# e.g. For student_D, age is passed as string number, but pydantic will convert it into integer
# But for student_E, it cannot convert the given string into integer, hence it will throw an error
student_D = {"name": "lala", "age": "33"}
student_E = {"name": "lala", "age": "hala"}

# Email Validation
student_F = {
    "name": "John",
    "email": "haha$lol.com",
}  # This will throw an error as email is not valid

# Field function
student_G = {"name": "Lalilalo"}


# ** unpacks the dictionary
# This returns a pydantic object
student = Student(**student_G)
# studentB = Student(**student_B)

print(student)

# This is how you fetch the type of an attribute from the dictionary
print(student.age)

# This converts the pydantic object "student" into an dictionary
student_dict = student.model_dump()
print(student_dict)
# This way we can access a variable in the dictionary
print(student_dict["age"])

# This converts the pydantic object "student" into a JSON
student_json = student.model_dump_json()
print(student_json)


# There is also an easy way to make a pydantic object
student_H = Student(name="Raja", age=22, email="raja@raja.raja")

print(student_H)
