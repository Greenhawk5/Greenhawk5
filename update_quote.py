import json


with open("quote.json", "r", encoding="utf-8") as f:
    data = json.load(f)


quote = data[0]["quote"]
author = data[0]["author"]


new_quote = f"""> "{quote}"

> — {author}"""


with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()


start = "<!-- QUOTE_START -->"
end = "<!-- QUOTE_END -->"


before = readme.split(start)[0]
after = readme.split(end)[1]


updated = (
    before
    + start
    + "\n\n"
    + new_quote
    + "\n\n"
    + end
    + after
)


with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)