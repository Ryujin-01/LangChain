from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.8)


class Schema(BaseModel):
    facts: list[str] = Field(
        description="A list of five interesting facts about the topic. Keep them numbered"
    )


structured_model = model.with_structured_output(
    Schema
)  # This line is removed for output_parser.

# This is the code for output parser. We are using PydanticOutputParser() here.

# parser = PydanticOutputParser(pydantic_object=Schema)


template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Australian pirate. Answer the query in the same way."),
        (
            "human",
            """
            Give me facts about {topic}.
            """,
        ),
    ]
)

# This is the code for output_parser.

# template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are an Australian pirate. Answer the query in the same way."),
#         (
#             "human",
#             """
#             Give me facts about {topic}.

#             {format_instructions}
#             """,
#         ),
#     ]
# )

topic = input("Topic: ")

chain = template | structured_model

result = chain.invoke({"topic": topic})

# This is the code for output_parser.

# chain = template | model | parser

# result = chain.invoke(
#     {"topic": topic, "format_instructions": parser.get_format_instructions()}
# )

print(result)
