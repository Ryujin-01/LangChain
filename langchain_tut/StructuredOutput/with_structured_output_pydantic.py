from typing import Literal, Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.2)


# For multiple line string, we use """""" in python
# This acts as the raw, unstructured user data we want the AI to process
feedback = """I bought this tenkeyless board hoping for a stealthy office typing experience, and it mostly delivers. The custom-lubed 'Whisper' linear switches are incredibly smooth and genuinely silent, making it perfect for an open-plan workspace. The solid aluminum casing gives it a premium, heavy feel that refuses to slide around on the desk, even during intense typing sessions.

Unfortunately, the keycaps are a major letdown. They are cheap ABS plastic instead of textured PBT, meaning they started developing a greasy shine after just two weeks of heavy use. Furthermore, the wireless Bluetooth connection has a noticeable two-second delay when waking the keyboard from sleep mode, which is incredibly frustrating when you need to type a quick message.

Overall, it is a fantastic sounding and feeling board, but you will almost certainly want to spend extra money to replace the stock keycaps immediately. 

Pros: Truly silent linear switches, heavy aluminum build, great factory stabilizers.
Cons: Cheap ABS keycaps, noticeable Bluetooth wake delay, no dedicated number pad."""

# Pydantic is used for data representation as well as for validation
# Below is the same code as the "with_structured_output_typedict.py" but using pydantic


class Review_optional(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review"
    )
    # key_themes: Annotated[
    #     list[str], "Write down all the key themes discussed in the review"
    # ]

    summary: str = Field(description="A brief summary of the reveiw")
    # summary: Annotated[str, "A brief summary of the review"]

    sentiment: Literal["Positive", "Negative"] = Field(
        description="Return sentiment of the review"
    )
    # sentiment: Annotated[
    #     Literal["Positive, Negative"], "Return sentiment of the review."
    # ]

    pros: Optional[list[str]] = Field(
        description="Write down all the pros mentioned in the review"
    )
    # pros: Annotated[
    #     Optional[list[str]], "Write down all the pros mentioned in the review"
    # ]

    cons: Optional[list[str]] = Field(
        description="Write down all the cons mentioned in the review"
    )
    # cons: Annotated[
    #     Optional[list[str]], "Write down all the cons mentioned in the review"
    # ]

    name: Optional[str] = Field(
        description="Extract the human author's name. If no human name is explicitly written, return null"
    )
    # name: Annotated[
    #     Optional[str],
    #     "Extract the human author's name. If no human name is explicitly written, return null",
    # ]

    age: Optional[int] = Field(
        description="Write the age of the author. If no human age is explicitly written, return null"
    )
    # age: Annotated[
    #     Optional[int],
    #     "Write the age of the author. If no human age is explicitly written, return null",
    # ]


# Bind the blueprint to the model
# This strips away the AI's conversational personality and forces it to only output the dictionary structure defined above
# When you call model.with_structured_output(Review), LangChain is acting as a translator between your Python code and Google's backend servers.
# Behind the scenes, LangChain converts your Python code into this exact text block:
# {
#   "type": "object",
#   "properties": {
#     "summary": { "type": "string" },
#     "sentiment": { "type": "string" }
#   },
#   "required": ["summary", "sentiment"]
# }

# Not all LLM support with_structured_output() function.
# For .with_structured_output() to work, the LLM you are using must natively support a backend feature called Tool Calling (sometimes called Function Calling) or a strict JSON Mode.
# When you use .with_structured_output(), LangChain checks if the model supports these features.
# If it does, LangChain flips the switch on the API, mathematically restricting the tokens the model is allowed to generate.
# If the model does not support these features, LangChain will throw an error.
structured_model = model.with_structured_output(Review_optional)

# Send the raw feedback through the strict pipeline
# The model reads the text, extracts the data, formats it into our dictionary shape, and returns it
result = structured_model.invoke(feedback)

# Overall this would look like
# result = model.with_structured_output(Review).invoke(feedback)
# We can think of it like, before invoking the model we are passing a specific structure "Review", now the result will be displayed in this strucutre.

print(type(result))
print(result)
