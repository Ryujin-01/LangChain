from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", temperature=1.8)

parser = StrOutputParser()


class sentimentClassification(BaseModel):
    category: Literal["Positive", "Negative"] = Field(
        description="Give sentiment of the review"
    )


pydanticParser = PydanticOutputParser(pydantic_object=sentimentClassification)

classifier_prompt = PromptTemplate(
    template="Analyse this review.\n {review} \n {classify}",
    input_variables=["review"],
    partial_variables={"classify": pydanticParser.get_format_instructions()},
)

prompt1 = PromptTemplate(
    template="""You are a customer service agent. Write ONLY the response message to the customer.
                Do not include explanations, options, or tips. Just write the actual response.

                Positive review: {review}

                Your response to the customer:""",
    input_variables=["review"],
)

prompt2 = PromptTemplate(
    template="""You are a customer service agent. Write ONLY the response message to the customer.
                Do not include explanations, options, or tips. Just write the actual response.

                Negative review: {review}

                Your response to the customer:""",
    input_variables=["review"],
)


branchChain = RunnableBranch(
    # (condition, chain) --> This is the structure
    # lambda x: - Anonymous function that takes input x
    # x["classification"] - Access the classification object.
    # .category - Get the category attribute (either "Positive" or "Negative")
    (lambda x: x["classification"].category == "Positive", prompt1 | model | parser),
    (lambda x: x["classification"].category == "Negative", prompt2 | model | parser),
    # We need to define a default chain (required for RunnableBranch)
    # A RunnableLambda is simply a way to drop a standard Python function into a LangChain pipeline.
    # Using this saved a expensive LLM call
    # If the code reaches this point, it bypasses the AI completely and just returns the hardcoded string: "Could not find sentiment".
    RunnableLambda(lambda x: "Could not find sentiment"),
)

classifier_chain = classifier_prompt | model | pydanticParser

# The Master Chain
# RunnablePassthrough.assign takes original input and adds a 'classification' key
# We require the original response because we are passing it to the branchChain prompts as the "review" variable
chain = RunnablePassthrough.assign(classification=classifier_chain) | branchChain

review = "This product is dog shit crazy"
result = chain.invoke({"review": review})

print(result)

chain.get_graph().print_ascii()
