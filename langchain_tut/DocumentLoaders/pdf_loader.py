from langchain_classic.document_loaders import PyPDFLoader

loader = PyPDFLoader("1.pdf")

docs = loader.load()

# Here too the docs will be a list, but instead of one element, the docs will now contain as much as the number of pages in the pdf file.
print(type(docs), len(docs))

# This way we can print the contents of a particular page of the pdf file.
print(docs[5])

# Limitations: Does not work with scanned pdf or complex layouts. Hence you will need to find other alternatives.
