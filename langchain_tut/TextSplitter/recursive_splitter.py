from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.document_loaders import PyPDFLoader

loader = PyPDFLoader("1.pdf")

docs = loader.load()

# The separators follows a hierarchy here.
# 1. "\n\n"  → Try paragraph boundaries first
# 2. "\n"    → If necessary, try line boundaries
# 3. " "     → If necessary, try word boundaries
# 4. ""      → Finally, split at character level

# Let's say our document has 3 paragraphs: Para 1 (80 characters), Para 2 (120 characters), Para 3 (100 characters).
# And our chunk size is 100 and chunk overlap is 0 and separators is ["\n\n", "\n", " ", ""].
# Now the recursive splitter will first split the docs according to the paragraph. So the doc will be separated into 3 paragraphs.
# Now it will check the size of each para, the first and third paragraphs are well within the chunk size, hence they are okay.
# But the second paragraph is of 120 characters which is above the chunk size, hence now the recursive splitter will split according to new lines "\n".
# If this fails too, then it will break it with respect to the spaces (" ")... and so on.

# NOTE: If you are using multiple separators then use the keyword "separators" else use "separator"

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=0, separators=["\n\n", "\n", " ", ""]
)

result = splitter.split_documents(docs)

# It will also give a list of objects who have their own page_content and metadata
print(result[0].page_content)
