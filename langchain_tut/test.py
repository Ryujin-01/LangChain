import wikipedia

wikipedia.set_lang("en")

page = wikipedia.page("Albert Einstein")

print(page.title)
print(page.summary)
