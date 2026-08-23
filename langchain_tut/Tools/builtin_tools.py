from langchain_classic.tools import DuckDuckGoSearchRun

# Setting up our search tool.
# This is particularily helpful to get up to date answers for our queries as llm's tend to be outdated.
search_tool = DuckDuckGoSearchRun()

query = input("Ask: ")

results = search_tool.invoke(query)
print(type(results), results)
