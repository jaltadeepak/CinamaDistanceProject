import json
import requests

class Geocoder:
    def __init__(self) -> None:
        with open('requirements.txt', 'r') as file:
            self.API_KEY = file.read().split('\n')[3]
        self.HERE_API = 'https://geocode.search.hereapi.com/v1/geocode'

    def geocodeCinemas(self):
        #GEOCODE CINEMA ADDRESSES AND ADD TO JSON FILE
        with open('cinemas.json', 'r') as file:
            data = json.load(file)

        for cinema in data["Cinemas"]:
            parameters = {
                "q": cinema["Address"],
                "apiKey": self.API_KEY,
            }
            print(parameters)
            try:
                response = requests.get(url=self.HERE_API, params=parameters).json()
            except:
                cinema["Latitude"] = None
                cinema["Longitude"] = None
            else:
                cinema["Latitude"] = (response['items'][0]['position']['lat'])
                cinema["Longitude"] = (response['items'][0]['position']['lng'])

        with open('cinemas.json', 'w') as file:
            json.dump(data, file, indent=4)

    def geocodeCurrentAddress(self):
        #GEOCODE CURRENT ADDRESS
        with open('currentaddress.txt', 'r') as file:
            CURRENT_ADDRESS = file.read().split('\n')[0]
            print(CURRENT_ADDRESS)
            parameters = {
                "q": CURRENT_ADDRESS,
                "apiKey": self.API_KEY,
            }
            response = requests.get(url=self.HERE_API, params=parameters).json()

            lat = response['items'][0]['position']['lat']
            lng = response['items'][0]['position']['lng']

        with open('currentaddress.txt', 'w') as file:
            file.write(f"{CURRENT_ADDRESS}\n{lat}\n{lng}")