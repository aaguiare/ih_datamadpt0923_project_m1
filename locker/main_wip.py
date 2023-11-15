#Data and imports
import numpy as np
import argparse
import modules_database_wip as data 
import modules_function_wip as function
from scipy.spatial.distance import cdist
import geopandas as gpd
from shapely.geometry import Point

#Main Challenge, csv input includes static bike availability

def main(service, title):

    if service == 'bicimad' and title == "All":
        station_coords_bicimad = data.data_bicimad[['Latitude', 'Longitude']].to_numpy()

        def nearest_bicimad_direction(row):
            distances = cdist([(row['location.latitude'], row['location.longitude'])], station_coords_bicimad)
            min_index = np.argmin(distances)
            nearest_station_adress_bicimad = data.data_bicimad["address"].iloc[min_index]
            return nearest_station_adress_bicimad

        data.key_places['Station Location'] = data.key_places.apply(nearest_bicimad_direction, axis=1)

        def nearest_bicimad_station(row):
            distances = cdist([(row['location.latitude'], row['location.longitude'])], station_coords_bicimad)
            min_index = np.argmin(distances)
            nearest_station_name_bicimad = data.data_bicimad["name"].iloc[min_index].split("- ")[1]
            return nearest_station_name_bicimad

        data.key_places['Bicimad station'] = data.key_places.apply(nearest_bicimad_station, axis=1)

        def to_mercator_bicimad(lat, long):
            point = gpd.GeoSeries([Point(long, lat)], crs=4326)
            point_mercator = point.to_crs(3857)
            return point_mercator

        def distance_meters_bicimad(start_point, finish_point):
            return start_point.distance(finish_point).iloc[0]

        station_coords_mercator_bicimad = [to_mercator_bicimad(lat, lon) for lat, lon in station_coords_bicimad]

        def nearest_distance_bicimad(row):
            row_mercator = to_mercator_bicimad(row['location.latitude'], row['location.longitude'])
            distances = [distance_meters_bicimad(row_mercator, station) for station in station_coords_mercator_bicimad]
            nearest_distance_bicimad = min(distances)
            return f'{round((nearest_distance_bicimad/1000), 2)} km'

        data.key_places['Station Distance'] = data.key_places.apply(nearest_distance_bicimad, axis=1)

        final_df_bicimad = data.key_places[['title', "address.street-address", 'Bicimad station','Station Location', 'Station Distance']].copy()
        final_df_bicimad['address.street-address'] = final_df_bicimad['address.street-address'].apply(lambda x: x.title())
        final_df_bicimad.rename(columns={'title': 'Place of Interest', 
                                'address.street-address': 'Place address'}, inplace=True)
        final_df_bicimad['Type of place'] = 'Instalaciones accesibles municipales'

        # Export to CSV
        csv_file_path = './output/resultkeyplacesbicimaddataframe.csv' 
        result = final_df_bicimad.to_csv(csv_file_path, index=False)
    elif service == 'bicipark' and title == "All":

        station_coords_bicipark = data.data_bicipark[['Latitude', 'Longitude']].to_numpy()

        def nearest_bicipark_direction(row):
            distances = cdist([(row['location.latitude'], row['location.longitude'])], station_coords_bicipark)
            min_index = np.argmin(distances)
            nearest_station_adress_bicipark = data.data_bicipark["address"].iloc[min_index]
            return nearest_station_adress_bicipark

        data.key_places['Station Location'] = data.key_places.apply(nearest_bicipark_direction, axis=1)

        def nearest_station_bicipark(row):
            distances = cdist([(row['location.latitude'], row['location.longitude'])], station_coords_bicipark)
            min_index = np.argmin(distances)
            nearest_station_name_bicipark = data.data_bicipark["stationName"].iloc[min_index]
            return nearest_station_name_bicipark

        data.key_places['Bicipark station'] = data.key_places.apply(nearest_station_bicipark, axis=1)

        def to_mercator_bicipark(lat, long):
            point = gpd.GeoSeries([Point(long, lat)], crs=4326)
            point_mercator = point.to_crs(3857)
            return point_mercator

        def distance_meters_bicipark(start_point, finish_point):
            return start_point.distance(finish_point).iloc[0]

        station_coords_mercator_bicipark = [to_mercator_bicipark(lat, lon) for lat, lon in station_coords_bicipark]

        def nearest_distance_bicipark(row):
            row_mercator = to_mercator_bicipark(row['location.latitude'], row['location.longitude'])
            distances = [distance_meters_bicipark(row_mercator, station) for station in station_coords_mercator_bicipark]
            nearest_distance = min(distances)
            return f'{round((nearest_distance/1000), 2)} km'

        data.key_places['Station Distance'] = data.key_places.apply(nearest_distance_bicipark, axis=1)

        final_df_bicipark = data.key_places[['title', "address.street-address", 'Bicipark station', 'Station Location', 'Station Distance']].copy()
        final_df_bicipark['address.street-address'] = final_df_bicipark['address.street-address'].apply(lambda x: x.title())
        final_df_bicipark.rename(columns={'title': 'Place of Interest', 
                                'address.street-address': 'Place address'}, inplace=True)
        final_df_bicipark['Type of place'] = 'Instalaciones accesibles municipales'

        # Export to CSV
        csv_file_path = './output/resultkeyplacesbiciparkdataframe.csv' 
        result = final_df_bicipark.to_csv(csv_file_path, index=False)
    
    elif service == 'bicipark' and title:
        result = function.nearestbicipark_input(title)

    elif service == 'bicimad' and title:
        result = function.nearestbicimad_input(title)

    
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find nearest service station.')
    parser.add_argument('-p', '--service', choices=['bicipark', 'bicimad'], required=True, help='Choose service (bicipark or bicimad)')
    parser.add_argument('-t', '--title', required=True, help='Title of the point of origin')

    args = parser.parse_args()

    main(args.service, args.title)
    