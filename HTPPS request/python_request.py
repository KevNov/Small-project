import requests

url = "https://finance.detik.com/fintech"
respond = requests.get(url)

#print(respond.text)
print(f"your request to {url} came back w/ status code {respond.status_code}")
