import wikipedia as wiki
# print(wiki.search("Python"))
# print(wiki.suggest("Pyth"))
# print(wiki.summary("Python"))

wiki.set_lang("fr")
print(wiki.summary("Python"))

# wiki.set_lang("en")
# p = wiki.page("Python")
# print(p.title)
# print(p.url)
# print(p.content)
# print(p.links)
# print(p.images)