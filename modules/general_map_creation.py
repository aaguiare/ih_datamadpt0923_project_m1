import folium
from modules import modules_database as data 


def map_bicimad(): 
    m = folium.Map(location=[40.41521683750571,-3.7001360145276], tiles='OpenStreetMap', zoom_start=11)
    for index, row in data.data_bicimad.iterrows():
        lat_bicimad = row['Latitude']
        lng_bicimad = row['Longitude']
        station_name_bicimad = row['name']
        address_bicimad = row['address']

        # Create popup text
        popup_text = f"Bicimad Station: {station_name_bicimad}<br>Address: {address_bicimad}"
        folium.Marker(
            location=[lat_bicimad, lng_bicimad],
            popup=popup_text,
            icon=folium.Icon(color='blue')
        ).add_to(m)
    for index, row in data.key_places.dropna().iterrows():
        lat_key = row['location.latitude']
        lng_key = row['location.longitude']
        station_name_key = row['title']
        address_key = row['address.street-address']

        # Create popup text
        popup_text = f"Place of interest: {station_name_key}<br>Address: {address_key}"
        folium.Marker(
            location=[lat_key, lng_key],
            popup=popup_text,
            icon=folium.Icon(color='orange')
        ).add_to(m)

    return m.save("./output/mapbicimadall.html")

def map_bicipark(): 
    t = folium.Map(location=[40.41521683750571,-3.7001360145276], tiles='OpenStreetMap', zoom_start=11)
    for index, row in data.data_bicipark.iterrows():
        lat_bicipark = row['Latitude']
        lng_bicipark = row['Longitude']
        station_name_bicipark = row['stationName']
        address_bicipark = row['address']

        # Create popup text
        popup_text = f" Bicipark Station: {station_name_bicipark}<br>Address: {address_bicipark}"
        folium.Marker(
            location=[lat_bicipark, lng_bicipark],
            popup=popup_text,
            icon=folium.Icon(color='blue')
        ).add_to(t)
    for index, row in data.key_places.dropna().iterrows():
        lat_key = row['location.latitude']
        lng_key = row['location.longitude']
        station_name_key = row['title']
        address_key = row['address.street-address']

        # Create popup text
        popup_text = f"Place of interest: {station_name_key}<br>Address: {address_key}"
        folium.Marker(
            location=[lat_key, lng_key],
            popup=popup_text,
            icon=folium.Icon(color='orange')
        ).add_to(t)

    return t.save("./output/mapbiciparkall.html")
