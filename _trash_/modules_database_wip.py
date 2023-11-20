#Imports
import requests
import pandas as pd 

#Madrid data
base_url = "https://datos.madrid.es/egob"
defined_json = "/catalogo/202162-0-instalaciones-accesibles-municip.json"

key_places = pd.json_normalize(requests.get(base_url + defined_json).json()["@graph"])
key_places

#Data Bicipark and coordinates cleaning

data_bicipark = pd.read_csv("../data/bicipark_stations.csv", sep=";")
data_bicipark[['Longitude', 'Latitude']] = data_bicipark['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype("float64")

#Data Bicimad and coordinates cleaning

data_bicimad = pd.read_csv("../data/bicimad_stations.csv", sep="\t")
data_bicimad[['Longitude', 'Latitude']] = data_bicimad['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype("float64")
