import geopandas as gpd
import pandas as pd
import numpy as np
from datetime import datetime
startTime = datetime.now()

hex_geo = gpd.read_file('Data/city-hex-polygons-8.geojson')


hex = hex_geo[{'index', 'centroid_lat', 'centroid_lon'}]
hex_df = pd.DataFrame(hex)
hex_df['index'] = hex_df['index'].astype(str)


hex_df['centroid_lat'] = hex_df['centroid_lat'].fillna(0).astype(str).str[0:6]
hex_df['centroid_lon'] = hex_df['centroid_lon'].fillna(0).astype(str).str[0:5]
hex_df['hex_point'] = hex_df['centroid_lat'] + hex_df['centroid_lon'].astype(str)



sr = pd.read_csv ('Data/service_request/sr.csv')

sr_df = pd.DataFrame(sr)

sr_df['Latitude'] = sr_df['Latitude'].fillna(0).astype(str).str[0:6]
sr_df['Longitude'] = sr_df['Longitude'].fillna(0).astype(str).str[0:5]
sr_df['sr_point'] = sr_df['Latitude'] + sr_df['Longitude'].astype(str)

new_merge = pd.merge(sr_df,hex_df, how='left', left_on = 'sr_point', right_on = 'hex_point', indicator= True)
rslt_df = new_merge.loc[new_merge['_merge'] != 'both']
rslt_df.to_csv('Output/Data_Extraction/sr_hex_Failed_Merges.csv')


sr_hex_drop = new_merge.drop(['centroid_lon', 'centroid_lat', 'hex_point', 'sr_point', '_merge', 'Unnamed: 0'], axis=1)
sr_hex = sr_hex_drop.rename(columns = {'index': 'h3_level8_index'}).fillna(0)

sr_hex.drop_duplicates(subset ='NotificationNumber',
                     keep = 'first', inplace = True)
sr_hex.to_csv('Output/Data_Extraction/sr_hex_Shaun_Moloi.csv')


print("Script time")
print(datetime.now() - startTime)