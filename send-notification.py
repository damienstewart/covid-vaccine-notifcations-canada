from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
start_url = "https://covid19tracker.ca/vaccinationtracker.html"
driver.get(start_url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser")

percent_vaccinated_container = soup.find("div", attrs={"class": "summary-header-percentVaccinated"})
percent_vaccinated = percent_vaccinated_container.find("h1")

people_vaccinated = soup.find("span", attrs={"id": "updateVaxPpl"})


print(percent_vaccinated.get_text() + " of the population has been vaccinated \n" + people_vaccinated.get_text() + " have been vaccinated")
driver.quit()
