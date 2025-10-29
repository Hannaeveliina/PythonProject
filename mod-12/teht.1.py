import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Chuck Norris -vitsi:")
        print(data["value"])
    else:
        print("Vitsin hakeminen epäonnistui. Yritä uudelleen myöhemmin.")

if __name__ == "__main__":
    hae_chuck_norris_vitsi()
