#!/usr/bin/env python3

# @raycast.title Article
# @raycast.description Get article for the Dutch word

# @raycast.icon images/search.png
# @raycast.mode fullOutput
# @raycast.packageName Google
# @raycast.schemaVersion 1

# @raycast.argument1 { "type": "text", "placeholder": "word"}


import re
import sys
import urllib.request
import urllib.error


def get_body(word: str) -> str:
    url = f"https://www.welklidwoord.nl/{word}"
    request = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
        exit(1)
    except urllib.error.URLError as e:
        print("Error reason: ", e.reason)
        exit(1)
    else:
        data_text = response.read().decode("utf-8", errors="ignore")
        return data_text

def get_article(word: str) -> str:
    body = get_body(word)

    found = False
    for line in body.split("\n"):
        if "nieuwH2" in line:
            found = True
            continue
        if found:
            article = re.match("\s+<span>(\w+)<\/span>.+", line)
            return article.group(1)

word = sys.argv[1]
article = get_article(word)
print(f"{article} {word}")
