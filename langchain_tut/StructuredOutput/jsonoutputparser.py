from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

parser = JsonOutputParser()

# This is how you define a json parser
# FLAW: We cannot specify the schema for the output. THe schema for the output will entirely be decided by the LLM
prompt = PromptTemplate(
    template="Give a 5 most important fact about {topic}. \n {formatter}",
    input_variables=["topic"],
    # It is called partial variables because it is not passed by the user
    # parser.get_format_instructions() injects instructions that guide the model to produce valid JSON, making parsing much more reliable.
    partial_variables={"formatter": parser.get_format_instructions()},
)

chain = prompt | model | parser

topic = input("Topic: ")

result = chain.invoke(topic)

print(result)
