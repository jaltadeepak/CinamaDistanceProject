#CONVERT JSON TO CSV
import csv
import json

class JSONtoCSV:
    def __init__(self) -> None:
        pass
    
    def converter(self):
        with open("cinemas.json", "r") as file:
            data = json.load(file)

        with open('data.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name",  "Distance", "Address", "Latitude", "Longitude"])

            for cinema in data["Cinemas"]:    
                writer.writerow([cinema["Name"], round(cinema["Distance"], 2), cinema["Address"], cinema["Latitude"], cinema["Longitude"]])