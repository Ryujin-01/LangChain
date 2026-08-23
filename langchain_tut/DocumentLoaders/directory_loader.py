from langchain_classic.document_loaders import DirectoryLoader, PyPDFLoader

# "path" is the location of the directory
# "glob" tells the loader which files to select to load
# "loader_cls" tells which loader to use to read the files
loader = DirectoryLoader(path="Research Papers", glob="*.pdf", loader_cls=PyPDFLoader)

docs = loader.load()

# Type will again be list. The length would be total number of pages of all the files combined.
# Hence each index will contain data about one page of all the combined pages loaded in stack.
print(type(docs), len(docs))

print(docs[0])
