import json
from geopy.distance import geodesic

class Distance:
    def __init__(self) -> None:
        pass

    def CalcDistance(self):
        #CALCULATE DISTANCE
        with open("currentaddress.txt", "r") as file:
            data = file.read().split('\n')
            CURRENTADDRESS = data[0]
            CurrentCoords = (data[1], data[2])

        with open("cinemas.json", "r") as file:
            data = json.load(file)
            
        for cinema in data["Cinemas"]:
            AddressCoords = (cinema["Latitude"], cinema["Longitude"])
            cinema["Distance"] = geodesic(CurrentCoords, AddressCoords).kilometers

        with open("cinemas.json", "w") as file:
            json.dump(data, file, indent=4)