from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a buggy and grammatically inaccurate customer review about {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Extracts a strict Positive or Negative rating for the Marketing team about this {review}",
    input_variables=["review"],
)

prompt3 = PromptTemplate(
    template="Scrapes the text solely for technical errors to send to the QA Engineering team about this {review}",
    input_variables=["review"],
)

prompt4 = PromptTemplate(
    template="Extracts suggestions for new features to send to the Product Design team about this {review}",
    input_variables=["review"],
)

parallel_chain = RunnableParallel(
    sentiment=prompt2 | model | parser,
    QA=prompt3 | model | parser,
    suggestion=prompt4 | model | parser,
)

# Using RunnablePassthrough and assign() to keep the generated review in the final output.
# Generate the review and save it to the "review" key
# Pass that key into the parallel chain, save the results to "analysis"
# This generates a dictionary with two keys: review and analysis.
chain = {"review": prompt1 | model | parser} | RunnablePassthrough.assign(
    analysis=parallel_chain
)

query = input("Topic: ")

result = chain.invoke(query)

print("\n--- ORIGINAL BUGGY REVIEW ---")
print(result["review"])

print("\n--- PARALLEL EXTRACTIONS ---")
print(result["analysis"])

# This way you can visualise the chain
chain.get_graph().print_ascii()
