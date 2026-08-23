from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a detailed report about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Give me 5 important points from this report.\n {report}",
    input_variables=["report"],
)

query = input("Topic: ")

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke(query)

print(result, "\n")

# This way you can visualise the chain
chain.get_graph().print_ascii()
