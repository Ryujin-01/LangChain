from langchain_classic.document_loaders import DirectoryLoader, PyPDFLoader

# "path" is the location of the directory
# "glob" tells the loader which files to select to load
# "loader_cls" tells which loader to use to read the files
loader = DirectoryLoader(path="Research Papers", glob="*.pdf", loader_cls=PyPDFLoader)

docs = loader.lazy_load()

# Here the len() function would not work as there are no list of objects (they are generators).
print(type(docs))

# This code will also not work for the same reason.
# print(docs[0])

# This is how to access them
for doc in docs:
    print(doc.metadata)
