# The langchain_community is being archived, hence it is not maintained and there will be no updates.
# Hence its better to use langchain_classic cause it is still being maintained.

# This code would also work.
# from langchain_community.document_loaders import TextLoader

# The TextLoader is being deprecated, so it better to use other alternatives.
from langchain_classic.document_loaders import TextLoader

from langchain_classic.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

# The first parameter is the path of the file that we want to load.
# The second parameter is the encoding of the document, utf-8 is the most common encoding and can read a variety of text.
# Each character is represented by certain bytes. An encoder in tells the loader how to decode the bytes to characters in the text file.
loader = TextLoader("football.txt", encoding="utf-8")

# Loads the text file.
docs = loader.load()

# The loader loads the docs as a list. We can check here.
print(type(docs))

# Prints the number of docs in the list.
print(len(docs))

# Prints the first doc in the list
# print(docs[0])

# Prints the page_content and metadata seperately
print(docs[0].page_content)
print(docs[0].metadata)

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
parser = StrOutputParser()

template = PromptTemplate.from_template(
    template="Write the summary of the following:\n{text}"
)

chain = template | model | parser

print(chain.invoke(docs[0].page_content))
