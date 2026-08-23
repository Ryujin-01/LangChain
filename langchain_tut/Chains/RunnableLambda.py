from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
parser = StrOutputParser()

prompt = PromptTemplate.from_template(template="Generate a joke on {topic}")

query = input("Topic: ")


def count(text):
    return len(text.split())


# RunnableLambda converts a normal Python function to a Runnable, so that we can use it with the Runnable environment.

chain = (
    prompt
    | model
    | parser
    | RunnableParallel({"joke": RunnablePassthrough(), "count": RunnableLambda(count)})
)

# Instead of using a function, we can also define lambda functions inside RunnableLambda.
# e.g. The count function can also be written as "RunnableLambda(lambda x: len(x.split()))", and now there is no need to explicitly define a function.
# This is the reason why it is called RunnableLambda.

result = chain.invoke(query)

print(result)

chain.get_graph().print_ascii()
