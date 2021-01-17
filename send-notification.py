from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
import mysql.connector
import time
import requests

dt = datetime.now()

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

date_string = '{:%B %d, %Y}'.format(dt)

percent_num = float(percent_vaccinated.get_text().rstrip("%"))

benchmark = None

if (percent_num < 5 and percent_num > 1):
	benchmark = 1
elif (percent_num > 5 and percent_num < 10):
	benchmark = 5
elif (percent_num > 10 and percent_num < 15):
	benchmark = 10
elif (percent_num > 15 and percent_num < 20):
	benchmark = 15
elif (percent_num > 20 and percent_num < 25):
	benchmark = 20
elif (percent_num > 25 and percent_num < 30):
	benchmark = 25
elif (percent_num > 30 and percent_num < 40):
	benchmark = 30
elif (percent_num > 40 and percent_num < 50):
	benchmark = 40
elif (percent_num > 50 and percent_num < 60):
	benchmark = 50
elif (percent_num > 60 and percent_num < 70):
	benchmark = 60
elif (percent_num > 70 and percent_num < 80):
	benchmark = 70
elif (percent_num > 80 and percent_num < 90):
	benchmark = 80
elif (percent_num > 90 and percent_num < 99):
	benchmark = 90
else:
	benchmark = 100

def send_notification():
    return requests.post(
        "YOUR_MAILGUN_ENDPOINT_URL",
        auth=("api", "YOUR_MAILGUN_API_KEY"),
        data={"from": "COVID Vaccination Report <SENDER_EMAIL>",
              "to": ["RECEIVER_EMAIL"],
              "subject": "COVID-19 Vaccination Report: " + percent_vaccinated.get_text(),
              "text": percent_vaccinated.get_text() + " of the population has been vaccinated \n" + people_vaccinated.get_text() + " people have been vaccinated\ndate: " + date_string})

mydb = mysql.connector.connect(
	host="YOUR_DB_HOST",
	user="YOUR_DB_USER",
	password="YOUR_DB_PASS",
	database="YOUR_DB"
)

bm_cursor = mydb.cursor()

get_bm = "SELECT curr_bm FROM benchmark ORDER BY id DESC LIMIT 1"
bm_cursor.execute(get_bm)
curr_bm = bm_cursor.fetchall()
bm_cursor.close()

curr_bm = int(curr_bm[0][0])

ubm_cursor = mydb.cursor()

if (benchmark > curr_bm):
	update_bm = "INSERT INTO benchmark (curr_bm, date) VALUES (%s, %s)"
	new_bm = (benchmark, date_string)
	ubm_cursor.execute(update_bm, new_bm)
	ubm_cursor.close()
	send_notification()
	print("record updated, notification sent")

mycursor = mydb.cursor()
sql = "INSERT INTO vacc (percent_vaccinated, people_vaccinated, date) VALUES (%s, %s, %s)"
val = (percent_vaccinated.get_text(), people_vaccinated.get_text(), date_string)
mycursor.execute(sql, val)
mycursor.close()
 
mydb.commit()

print("current benchmark: " + str(benchmark) + "\n" + percent_vaccinated.get_text() + " of the population has been vaccinated \n" + people_vaccinated.get_text() + " people have been vaccinated\ndate: " + date_string)
driver.quit()
