import requests

url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": "cats", "limit": 2}
)

data = response.json()
#print(data)
print(data["results"])

#print(data["joke"])