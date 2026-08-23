from langchain_classic.retrievers import WikipediaRetriever

# Initialize the retriever (optional: set language and top k)
retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = input("Ask: ")

# Get relevant wikipedia documents
# NOTE: Retrievers are runnables.
docs = retriever.invoke(query)

print(type(docs), len(docs))

for i, doc in enumerate(docs):
    print("Result ", i + 1, ":\n", doc, "\n\n")
