import requests
from APOD import nasa_apod
from dotenv import load_dotenv
import os

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")

BASE_URL = "https://api.nasa.gov/planetary/apod"

while True:

    date = input("Enter a birth date after 1995-06-16 (YYYY-MM-DD) or 'q' to quit: ")

    if date == 'q':

        break

    else:
        params = {
            "api_key": NASA_API_KEY,
            "date": date
        }
        
        apod_result = requests.get(BASE_URL, params=params).json()

        apod = nasa_apod(**apod_result)

        print(apod)

