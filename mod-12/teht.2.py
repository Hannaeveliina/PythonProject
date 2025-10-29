import requests

def hae_saa(paikkakunta, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    parametrit = {
        "q": paikkakunta,
        "appid": api_key,
        "units": "metric",
        "lang": "fi"
    }

    vastaus = requests.get(url, params=parametrit)
    if vastaus.status_code != 200:
        print("Virhe:", vastaus.json().get("message", "Tuntematon virhe"))
        return

    data = vastaus.json()
    kuvaus = data["weather"][0]["description"]
    lampotila = data["main"]["temp"]

    print(f"Sää paikkakunnassa {paikkakunta}: {kuvaus}")
    print(f"Lämpötila: {lampotila:.1f} °C")

if __name__ == "__main__":
    api_avain = input("Anna OpenWeatherMap API-avain: ")
    kaupunki = input("Anna paikkakunnan nimi: ")
    hae_saa(kaupunki, api_avain)
