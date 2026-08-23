# Since langchain_community is being deprecated, this is an alternate way to load a text file
# There are several other alternatives for other documnet formats, you can look them up on the internet

from langchain_core.documents import Document

# To read a file using python
with open("football.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Loading the document
docs = Document(page_content=text, metadata={"source": "football.txt"})

print(docs)
print(type(docs))
