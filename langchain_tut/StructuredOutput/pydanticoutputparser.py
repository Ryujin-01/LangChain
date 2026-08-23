from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")


# Defining the Schema
class Schema(BaseModel):
    fact1: str = Field(description="1'st fact about the topic")
    fact2: str = Field(description="2'nd fact about the topic")
    fact3: str = Field(description="3'rd fact about the topic")
    fact4: str = Field(description="4'th fact about the topic")
    fact5: str = Field(description="5'th fact about the topic")


# This is how you define a pydantic parser
# It specifies the schema as well as validates it at the runtime
parser = PydanticOutputParser(pydantic_object=Schema)

# Defining the prompt
prompt = PromptTemplate(
    template="Give a 5 most important fact about {topic}. \n {formatter}",
    input_variables=["topic"],
    # It is called partial variables because it is not passed by the user
    partial_variables={"formatter": parser.get_format_instructions()},
)


topic = input("Topic: ")

formatted_prompt = prompt.invoke(topic)
print(formatted_prompt, "\n")  # Read this to know what is happening behind the scenes

chain = model | parser

result = chain.invoke(formatted_prompt)

print(result)
