from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write 5 interesting facts about {topic}", input_variables=["topic"]
)

query = input("Topic: ")

chain = prompt | model | parser

result = chain.invoke(query)

print(result, "\n")

# This way you can visualise the chain
chain.get_graph().print_ascii()
