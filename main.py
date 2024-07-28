import requests

response=requests.get("https://www.omdbapi.com/?i=tt3896198&apikey=fff9b9a4")

with open("index.html","w") as file:
    file.write(response.text)
