from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
parser = StrOutputParser()

template = PromptTemplate.from_template(template="Generate a review about {topic}.")

summarizer = PromptTemplate.from_template(template="Summarize this review:\n{review}")


def summarize(text):
    if len(text.split()) > 300:
        print("Review has been summarized.\n\n")
        return True
    return False


review_chain = template | model | parser

analysis_chain = RunnableBranch(
    # (condition, runnable)
    (lambda review: summarize(review), summarizer | model | parser),
    # Default function
    RunnablePassthrough(),
)

query = input("Topic: ")

chain = review_chain | analysis_chain

result = chain.invoke(query)

print(result)
