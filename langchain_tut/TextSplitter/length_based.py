from langchain_text_splitters import CharacterTextSplitter
from langchain_classic.document_loaders import PyPDFLoader

loader = PyPDFLoader("1.pdf")

docs = loader.load()

# The "chunk_size" tells the splitter the number of characters after which it should split
# The "chunk_overlap" tells the splitter how many character it should overlap from the previous chunk.
# "seperator" is the boundary character or string where the text splitter tries to break the text.
# e.g.
# Football is fun.\nCricket is fun.\nTennis is fun. (Here \n is a new line character).
# separator="\n". Now the splitter will look for "\n" and try to split around that. Hence this becomes
# Football is fun.
# Cricket is fun.
# Tennis is fun.
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="")

result = splitter.split_documents(docs)

# It will also give a list of objects who have their own page_content and metadata
print(result[0].page_content)
