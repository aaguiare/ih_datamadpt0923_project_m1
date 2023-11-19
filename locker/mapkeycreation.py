import folium
import modules_database_wip as data
import pandas as pd 

def create_map_bicimad(nearest_index,index):

    data.key_places["Combined coordinates"] = data.key_places.apply(lambda row: [row["location.latitude"], row["location.longitude"]], axis=1)
    data.data_bicimad["Combined coordinates"] = data.data_bicimad.apply(lambda row:[row["Latitude"], row["Longitude"]], axis=1)

    m = folium.Map(location=[40.416775, -3.703790], zoom_start=12)

   
    if 0 <= nearest_index < len(data.data_bicimad):
        bicimad_point = data.data_bicimad.iloc[nearest_index]
        folium.Marker(
            location=bicimad_point["Combined coordinates"],
            popup=f"Bicimad Station: {bicimad_point['name']}<br>Address: {bicimad_point['address']}",
            icon=folium.Icon(color='blue')
        ).add_to(m)

    
    if 0 <= index < len(data.key_places):
        key_place = data.key_places.iloc[index]
        folium.Marker(
            location=key_place["Combined coordinates"],
            popup=f"Place of interest: {key_place['title']}<br>Address: {key_place['address.street-address']}",
            icon=folium.Icon(color='orange')
        ).add_to(m)

    if 0 <= nearest_index < len(data.data_bicimad) and 0 <= index < len(data.key_places):
        points = [data.data_bicimad.iloc[nearest_index]["Combined coordinates"], 
                  data.key_places.iloc[index]["Combined coordinates"]]
        folium.PolyLine(points, weight=5, opacity=1).add_to(m)


   
        df = pd.DataFrame(points, columns=['Lat', 'Lon'])
        sw = df.min().values.tolist()
        ne = df.max().values.tolist()
        m.fit_bounds([sw, ne])

    return m

def create_map_bicipark(nearest_index,index):

    data.key_places["Combined coordinates"] = data.key_places.apply(lambda row: [row["location.latitude"], row["location.longitude"]], axis=1)
    data.data_bicipark["Combined coordinates"] = data.data_bicipark.apply(lambda row:[row["Latitude"], row["Longitude"]], axis=1)

    b = folium.Map(location=[40.416775, -3.703790], zoom_start=12)

   
    if 0 <= nearest_index < len(data.data_bicipark):
        bicipark_point = data.data_bicipark.iloc[nearest_index]
        folium.Marker(
            location=bicipark_point["Combined coordinates"],
            popup=f"Bicipark Station: {bicipark_point['stationName']}<br>Address: {bicipark_point['address']}",
            icon=folium.Icon(color='blue')
        ).add_to(b)

    
    if 0 <= index < len(data.key_places):
        key_place = data.key_places.iloc[index]
        folium.Marker(
            location=key_place["Combined coordinates"],
            popup=f"Place of interest: {key_place['title']}<br>Address: {key_place['address.street-address']}",
            icon=folium.Icon(color='orange')
        ).add_to(b)

    if 0 <= nearest_index < len(data.data_bicipark) and 0 <= index < len(data.key_places):
        points = [data.data_bicipark.iloc[nearest_index]["Combined coordinates"], 
                  data.key_places.iloc[index]["Combined coordinates"]]
        folium.PolyLine(points, weight=5, opacity=1).add_to(b)


   
        df = pd.DataFrame(points, columns=['Lat', 'Lon'])
        sw = df.min().values.tolist()
        ne = df.max().values.tolist()
        b.fit_bounds([sw, ne])

    return b
