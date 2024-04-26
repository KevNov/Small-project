import requests

url = "https://icanhazdadjoke.com/"
#url = "https://oto.detik.com/mobil-listrik/d-6937193/mobil-listrik-ini-dijual-rp-105-jutaan-tampang-ala-ford-bronco"
response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()
print(data["joke"])
