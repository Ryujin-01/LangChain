from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# By the time I learned this topic, it was already removed from langchain
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

# This is how you define a structured output parser
# Structured Output Parser helps extract structured JSON data from LLM responses based on predefined field schemas
# PROS: We can specify the schema for the result to the LLM
# FLAW: We cannot validate the schema

schema = [
    ResponseSchema(name="Fact_1", description="1'st fact about the topic"),
    ResponseSchema(name="Fact_2", description="2'st fact about the topic"),
    ResponseSchema(name="Fact_3", description="3'st fact about the topic"),
    ResponseSchema(name="Fact_4", description="4'st fact about the topic"),
    ResponseSchema(name="Fact_5", description="5'st fact about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

prompt = PromptTemplate(
    template="Give a 5 most important fact about {topic}. \n {formatter}",
    input_variables=["topic"],
    partial_variables={"formatter": parser.get_format_instructions()},
)

chain = prompt | model | parser

topic = input("Topic: ")

result = chain.invoke(topic)

print(result)
