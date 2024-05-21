import json

url = {"url" :'https://wrpsa.com/the-official-rules-of-rock-paper-scissors/'}

print("Do you want to see something cool?\n")

see = input()

if see == 'yes':

    with open("article.txt", 'w') as outfile:
        outfile.write("run")

    
    with open("article.json", "w") as outfile:
        outfile.write(json.dumps(url))
