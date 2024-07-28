import requests
   
id = int(input("Please, enter ID: "))
print("1")
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?id={id}",verify=False, timeout=20)
print("2")

print("This is response as json: -----------------")
data =response.json()
print(data)

print("Printing titles: ")
for d in data:
    print(d["title"])
