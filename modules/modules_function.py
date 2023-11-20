#Imports 
import pandas as pd 
from modules import modules_database as data
from modules import geo_calculations as geo
from modules import module_api_data as api
from modules import key_map_creation as mapkey




#User input
def nearestbicimad_input(title):
    index = data.key_places[data.key_places['title']==title].index.item()
    dist = [geo.distance_meters(data.key_places['location.latitude'][index],data.key_places['location.longitude'][index], data.data_bicimad['Latitude'][i], data.data_bicimad['Longitude'][i])[0] for i in range(len(data.data_bicimad))]
    nearest_index = dist.index(min(dist))
    result =  data.data_bicimad.loc[nearest_index]
    numberstation = data.data_bicimad["number"][dist.index(min(dist))]
    numberstation_apiref = api.stations_api_data[api.stations_api_data["number"] == numberstation ].index
    if not numberstation_apiref.empty:
        number_api = numberstation_apiref[0]
    resultbicimad_df = pd.DataFrame([result], columns=result.index)
    finalresultbicimad_df = resultbicimad_df[['name', "address", 'dock_bikes',"free_bases"]].copy()

    finalresultbicimad_df.rename(columns={'name': 'Bicimad Station', 
                         'address': 'Station address',
                        'dock_bikes': 'Bikes available',
                        "free_bases": 'Free bases available'}, inplace=True)
    finalresultbicimad_df.to_csv('./output/resultbicimadinput.csv', index=False)
    m = mapkey.create_map_bicimad(nearest_index,index)
    m.save("./output/mapbetweentwopointsbicimad.html")
    print(f'Your nearest station is {data.data_bicimad["name"][dist.index(min(dist))].split("- ")[1]} located at {round((min(dist)/1000), 2)} km from you and has {api.stations_api_data["dock_bikes"][number_api]} bikes and {api.stations_api_data["free_bases"][number_api]} free bases available. CSV file and map are ready in the Output folder.')


def nearestbicipark_input(title):
    #test = input("por favor seleccione destino: ")
    #print(f"ha elegido {test}")
    index = data.key_places[data.key_places['title']==title].index.item()
    dist = [geo.distance_meters(data.key_places['location.latitude'][index],data.key_places['location.longitude'][index], data.data_bicipark['Latitude'][i], data.data_bicipark['Longitude'][i])[0] for i in range(len(data.data_bicipark))]
    nearest_index = dist.index(min(dist))
    result =  data.data_bicipark.loc[nearest_index]
    resultbicipark_df = pd.DataFrame([result], columns=result.index)
    finalresultbicimad_df = resultbicipark_df[['stationName', "address", 'free_places']].copy()
    finalresultbicimad_df.rename(columns={'stationName': 'Bicipark Station', 
                         'address': 'Station address',
                        'free_places': 'Free bases available'}, inplace=True)
    finalresultbicimad_df.to_csv('./output/resultbiciparkinput.csv', index=False)
    b = mapkey.create_map_bicipark(nearest_index,index)
    b.save("./output/mapbetweentwopointsbicipark.html")
    print(f'Your nearest station is {data.data_bicipark["stationName"][dist.index(min(dist))]} located at {round((min(dist)/1000), 2)} km from you and has {data.data_bicipark["free_places"][dist.index(min(dist))]} free bases available. CSV file and map are ready in the Output folder.')

