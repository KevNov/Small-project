import requests
from random import choice

user_input = input("what type of jokes are you searching? ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"search":user_input}
).json()

num_jokes = res["total_jokes"]
result = res["results"]

if num_jokes > 1:
    print(f"There's {num_jokes} about {user_input}, here's one")
    print(choice(result)["joke"])
elif num_jokes == 1:
    print("There's only one result")
else:
    print(f"your{user_input} isnt in this website")