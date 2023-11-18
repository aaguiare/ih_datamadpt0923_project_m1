import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

r=requests.get("https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/", headers={"email": (os.getenv('email')), "password": os.getenv('password') })

token = r.json()['data'][0]['accessToken']

url_stations = f'https://openapi.emtmadrid.es/v1/transport/bicimad/stations/'
s = requests.get(url_stations, headers = {'accessToken':token})
response = s.json()
stations_api_data = pd.json_normalize(response['data'])