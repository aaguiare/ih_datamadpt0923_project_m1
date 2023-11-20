#Data and imports
import numpy as np
import argparse
import modules_database_wip as data 
import modules_function_wip as function
from scipy.spatial.distance import cdist
import geopandas as gpd
from shapely.geometry import Point
 
if __name__ == "__main__":
    def parse_arguments():
        parser = argparse.ArgumentParser(description='Find nearest service station.')
        parser.add_argument('-p', '--service', choices=['bicipark', 'bicimad'], required=True, help='Choose service (bicipark or bicimad)')
        parser.add_argument('-t', '--title', required=True, help='Title of the point of origin')

        return parser.parse_args()

    def main():
        args = parse_arguments()

        if args.service == 'bicipark' and args.title:

            result = function.nearestbicipark_input(args.title)

        elif args.service == 'bicimad' and args.title:

            result = function.nearestbicimad_input(args.title)

        elif args.service == 'bicimad' and not args.title:

            station_coords = data.data_bicimad[['Latitude', 'Longitude']].to_numpy()

            def nearest_bicimad_direction(row):
                distances = cdist([(row['location.latitude'], row['location.longitude'])], station_coords)
                min_index = np.argmin(distances)
                nearest_station_adress = data.data_bicimad["address"].iloc[min_index]
                return nearest_station_adress

            data.key_places['Station Location'] = data.key_places.apply(nearest_bicimad_direction, axis=1)

            def nearest_station(row):
                distances = cdist([(row['location.latitude'], row['location.longitude'])], station_coords)
                min_index = np.argmin(distances)
                nearest_station_name = data.data_bicimad["name"].iloc[min_index].split("- ")[1]
                return nearest_station_name

            data.key_places['Bicimad station'] = data.key_places.apply(nearest_station, axis=1)

            def to_mercator(lat, long):
                point = gpd.GeoSeries([Point(long, lat)], crs=4326)
                point_mercator = point.to_crs(3857)
                return point_mercator

            def distance_meters(start_point, finish_point):
                return start_point.distance(finish_point).iloc[0]

            station_coords_mercator = [to_mercator(lat, lon) for lat, lon in station_coords]

            def nearest_distance(row):
                row_mercator = to_mercator(row['location.latitude'], row['location.longitude'])
                distances = [distance_meters(row_mercator, station) for station in station_coords_mercator]
                nearest_distance = min(distances)
                return f'{round(nearest_distance, 1)} meters'

            data.key_places['Station Distance'] = data.key_places.apply(nearest_distance, axis=1)

            final_df = data.key_places[['title', "address.street-address", 'Bicimad station','Station Location', 'Station Distance']].copy()
            final_df['address.street-address'] = final_df['address.street-address'].apply(lambda x: x.title())
            final_df.rename(columns={'title': 'Place of Interest', 
                                    'address.street-address': 'Place address'}, inplace=True)
            final_df['Type of place'] = 'Instalaciones accesibles municipales'

            # Export to CSV
            csv_file_path = './output/resultkeyplacesbicimaddataframe.csv' 
            result = final_df.to_csv(csv_file_path, index=False)
        elif args.service == 'bicipark' and not args.title:

            station_coords = data.data_bicipark[['Latitude', 'Longitude']].to_numpy()

            def nearest_bicipark_direction(row):
                distances = cdist([(row['location.latitude'], row['location.longitude'])], station_coords)
                min_index = np.argmin(distances)
                nearest_station_adress = data.data_bicipark["address"].iloc[min_index]
                return nearest_station_adress

            data.key_places['Station Location'] = data.key_places.apply(nearest_bicipark_direction, axis=1)

            def nearest_station(row):
                distances = cdist([(row['location.latitude'], row['location.longitude'])], station_coords)
                min_index = np.argmin(distances)
                nearest_station_name = data.data_bicipark["stationName"].iloc[min_index]
                return nearest_station_name

            data.key_places['Bicipark station'] = data.key_places.apply(nearest_station, axis=1)

            def to_mercator(lat, long):
                point = gpd.GeoSeries([Point(long, lat)], crs=4326)
                point_mercator = point.to_crs(3857)
                return point_mercator

            def distance_meters(start_point, finish_point):
                return start_point.distance(finish_point).iloc[0]

            station_coords_mercator = [to_mercator(lat, lon) for lat, lon in station_coords]

            def nearest_distance(row):
                row_mercator = to_mercator(row['location.latitude'], row['location.longitude'])
                distances = [distance_meters(row_mercator, station) for station in station_coords_mercator]
                nearest_distance = min(distances)
                return f'{round(nearest_distance, 1)} meters'

            data.key_places['Station Distance'] = data.key_places.apply(nearest_distance, axis=1)

            final_df = data.key_places[['title', "address.street-address", 'Bicipark station', 'Station Location', 'Station Distance']].copy()
            final_df['address.street-address'] = final_df['address.street-address'].apply(lambda x: x.title())
            final_df.rename(columns={'title': 'Place of Interest', 
                                    'address.street-address': 'Place address'}, inplace=True)
            final_df['Type of place'] = 'Instalaciones accesibles municipales'

            # Export to CSV
            csv_file_path = './output/resultkeyplacesbiciparkdataframe.csv' 
            result = final_df.to_csv(csv_file_path, index=False)

        return result

