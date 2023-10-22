# TO SCRAPE BOOKMYSHOW DATA
class Scraper:
    def __init__(self) -> None:
        with open("requirements.txt", "r") as file:
            self.link = file.read().split('\n')[1]
    
    def scrape(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import json

        WEBPAGE_LINK = self.link

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome()
        driver.get(WEBPAGE_LINK)

        CinemaNameElements = driver.find_elements(By.XPATH, '//*[@id="super-container"]/div[2]/div[2]/div/div/div/div/div[2]/div[1]')
        CinemaNames = [cinema.text for cinema in CinemaNameElements]

        CinemaAddressElements = driver.find_elements(By.XPATH, '//*[@id="super-container"]/div[2]/div[2]/div/div/div/div/div[2]/div[2]')
        CinemaAddresses = [cinema.text for cinema in CinemaAddressElements]

        data = {
            "Cinemas":[
                {"Name": name, "Address": address} for name, address in zip(CinemaNames, CinemaAddresses)
            ]
        }

        with open("cinemas.json", "w") as json_file:
            json.dump(data, json_file, indent=4)