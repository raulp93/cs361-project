import webbrowser
import json
import time


print("display_article.py is running...")

while True:

    with open("article.txt", "r") as infile:
        text = infile.read()
    
    if text == 'run':
        with open("article.txt", "w") as outfile:
            outfile.write("ok")

        with open("article.json", 'r') as infile:
            request = json.load(infile)

        url = request["url"]

        webbrowser.open(url)

    time.sleep(0.25)