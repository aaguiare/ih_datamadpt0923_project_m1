#Imports 
import pandas as pd 
import modules_database_wip as data
import geo_calculations as geo


#User input
def nearestbicimad_input(title):
    index = data.key_places[data.key_places['title']==title].index.item()
    dist = [geo.distance_meters(data.key_places['location.latitude'][index],data.key_places['location.longitude'][index], data.data_bicimad['Latitude'][i], data.data_bicimad['Longitude'][i])[0] for i in range(len(data.data_bicimad))]
    nearest_index = dist.index(min(dist))
    result =  data.data_bicimad.loc[nearest_index]
    resultbicimad_df = pd.DataFrame([result], columns=result.index)
    finalresultbicimad_df = resultbicimad_df[['name', "address", 'dock_bikes',"free_bases"]].copy()

    finalresultbicimad_df.rename(columns={'name': 'Bicimad Station', 
                         'address': 'Station address',
                        'dock_bikes': 'Bikes available',
                        "free_bases": 'Free bases available'}, inplace=True)
    finalresultbicimad_df.to_csv('./output/resultbicimadinput.csv', index=False)
    return f'Your nearest station is {data.data_bicimad["name"][dist.index(min(dist))].split("- ")[1]} located at {round(min(dist), 2)} meters from you and has {data.data_bicimad["dock_bikes"][dist.index(min(dist))]} bikes and {data.data_bicimad["free_bases"][dist.index(min(dist))]} free bases available. The CSV is ready in the Output folder.'


def nearestbicipark_input(title):
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
    return f'Your nearest station is {data.data_bicipark["stationName"][dist.index(min(dist))]} located at {round(min(dist), 2)} meters from you and has {data.data_bicipark["free_places"][dist.index(min(dist))]} free bases available. The CSV is ready in the Output folder.'

