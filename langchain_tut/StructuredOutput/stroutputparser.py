from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

# It converts the model's response into a plain Python string.
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Give a detailed report on {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a 50 word summary of this report. \n {report}",
    input_variables=["report"],
)

chain = prompt1 | model | parser | prompt2 | model | parser

topic = input("Topic: ")

result = chain.invoke(topic)

print(result)
