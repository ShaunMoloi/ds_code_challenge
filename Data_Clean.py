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

sr_hex_drop = new_merge.drop(['centroid_lon', 'centroid_lat', 'hex_point', 'sr_point', '_merge', 'Unnamed: 0'], axis=1)
sr_hex = sr_hex_drop.rename(columns = {'index': 'h3_level8_index'}).fillna(0)

sr_hex.drop_duplicates(subset ='NotificationNumber',
                     keep = 'first', inplace = True)
sr_hex.to_csv('hexConvert2.csv')

#Python 2: 
#print datetime.now() - startTime 

#Python 3: 
#print(datetime.now() - startTime)

#print('My Version')
#print(sr_hex.describe())
#print(sr_hex.head())
#print(sr_hex['CreationTimestamp'].dtypes)

#sr_compare = pd.read_csv ('Data/service_request_compare/sr_hex.csv')
#print('Compare')
#print(sr_compare.describe())
#print(sr_compare.head())


#print(sr_hex)
#print(sr_hex['NotificationNumber'] == '1011845437' )

#Verification 
#rslt_df = new_merge.loc[new_merge['index'] != 'NaN']

#print(rslt_df)
#rslt_df = new_merge[new_merge['index']  1]
#print(new_merge[10:23])
#print(sr_df['Longitude'].dtypes)
#print(sr_df.head())
#Create Point
#pd.concat()
#Practice
#merge1 = pd.read_csv ('Data/service_request/merge1.csv')
#merge2 = pd.read_csv ('Data/service_request/merge2.csv')

#merge1['Lat'] = merge1['Lat'].astype(str)
#merge1['Lon'] = merge1['Lon'].astype(str)
#merge1['Point'] = merge1['Lat'] + ' ' + merge1['Lon']
#print(merge1)

#merge2['M_Lat'] = merge2['M_Lat'].astype(str)
#merge2['M_Lon'] = merge2['M_Lon'].astype(str)
#merge2['M_Point'] = merge2['M_Lat'] + ' ' + merge2['M_Lon']

#print(merge2)
#new_merge = pd.merge(merge1,merge2, how='left', left_on = 'Point', right_on = 'M_Point', indicator= True)
#print(new_merge.dtypes(merge1, columns = ['ID']))


#print(merge1['ID'].dtypes)
#print(new_merge)



#hex = hex_geo[{'index', 'centroid_lat', 'centroid_lon'}]
#hex_df = pd.DataFrame(hex)
#sr = pd.read_csv ('Data/service_request/sr.csv')

#N = 1000000

#hex_df['centroid_lat'] = np.round(hex_df['centroid_lat']*N).fillna(0).astype(np.int64)
#hex_df['centroid_lon'] = np.round(hex_df['centroid_lon']*N).fillna(0).astype(np.int64)



#sr['Latitude'] = np.round(sr['Latitude']*N).fillna(0).astype(np.int64)
#sr['Longitude'] = np.round(sr['Longitude']*N).fillna(0).astype(np.int64)


#new_merge = pd.merge(sr, hex_df, how='left', left_on = ['Latitude','Longitude'], right_on = ['centroid_lat','centroid_lon']
#, indicator= True
#)


#Working_Code

#new_merge.to_csv('hexConvert1.csv')
#new_merge = pd.merge(sr, hex_df, how='left', left_on = ['Latitude'], right_on = ['centroid_lat'], indicator= True)
#rslt_df = new_merge.loc[new_merge['index'] != 'NaN']

#print(new_merge['_merge'])
#rslt_df = new_merge[new_merge['index']  1]


#sr.Latitude = sr.Latitude / N
#print(hex_df['index'])
#print(sr[['Latitude','Longitude']])
#print(sr['Latitude','Longitude'].dtypes)
#print(sr['Longitude'].dtypes)


#print(hex_df['centroid_lat','centroid_lon'])
#print(sr['centroid_lat'].dtypes)

#print(rslt_df)
#sr.Latitude = sr.Latitude / N
#print(new_merge[['Latitude','Longitude']])
#
#print(new_merge[10:23])

#print(hex_df)ss    

#new_hex_df = hex_df['centroid_lat'] = hex_df['centroid_lat'].astype(int64)
#new_sr = sr['Latitude'] = sr['Latitude'].astype(int64)


#print(new_merge)
#print(new_merge.dtypes(merge1, columns = ['ID']))

#print(hex_df['centroid_lat'].dtypes)
#new = pd.merge(new_sr,new_hex_df, how='left', left_on = 'Latitude', right_on = 'centroid_lat', indicator= True)
#print(new)
#hex_df = pd.DataFrame(srs)
#hex_df.to_csv('hexConvert.csv')


















#update = hex_df.rename(columns = {'index': 'h3_level8_index'})
#sr = pd.read_csv ('Data/service_request/sr_small.csv')
#print(update.head()#)
#print(pd.dtypes(update, columns = ['index']))
#print(update['centroid_lat'].dtypes)
#print(sr['Latitude'].dtypes)


#hex_df['centroid_lat'] = hex_df['centroid_lat'].astype(str)
#sr['Latitude'] = sr['Latitude'].astype(str)

#print(hex_df.head())

#result = pd.merge(sr,
#                 hex_df['centroid_lat'],
 #                on='Latitude')
#result.head()
#new = pd.merge(sr,hex_df, how='left', left_on = 'Latitude', right_on = 'centroid_lat')
#new = sr.merge(hex_df, on='centroid_lat', how='left')
#new = sr.merge(left_on='Latitude', right_on='centroid_lat', how='left', indicator = True)
#print(new.head())

#sr_hex_drop = new.drop(['h3_level8_index''centroid_lon', 'centroid_lat'], axis = 1)
#sr_hex = sr_hex_drop.rename(columns = {'index': 'h3_level8_index'})

#sr_compare = pd.read_csv ('Data/service_request_compare/sr_hex.csv')

#new.to_csv('sr_hexShaun.csv')

#print(new)
#print(sr_compare.head())


#print(update['centroid_lat'].dtypes)
#print(sr['Latitude'].dtypes)
#drops = sr.dropna(subset = ["Latitude"], inplace=False)
#dupes =drops[drops.duplicated(subset=['Latitude'],keep=False)]    
#print(dupes)
#print(sr.head())
#print(update.head())
#srs.name = 'foo'
#rs.to_frame().geometry
#print(update.head())
#hex = pd.hex_geo


#hex_geo = hex_geo.to_frame().reset_index()
#hex_geo.columns = ['id', 'price']
#sr.merge(df2)
#print(type(df))


#print(sr.head())

#new = sr.merge(update, on='Latitude', how='left')
#new = hex.merge(sr.rename({'centroid_lat': 'Latitude'}, axis=1),
#               left_on='centroid_lat', right_on='Latitude', how='left')
#new = pd.merge(sr,update,left_on='Latitude',right_on='Latitude')



#new.to_csv('sr_hexShaun.csv')
#h3_level8_index = hex['index']
#h3_level8_index.rename(index={0: 'h3_level8_index'})
#h3_level8_index.rename(columns ={'index': 'h3_level8_index'})

#print(h3_level8_index.head())
#
#sr_hex = sr.join(h3_level8_index)
#sr_hex.rename(columns = {'Duration': 'h3_level8_index'})
#sr_hex.rename(columns = {'Duration': 'h3_level8_index'})
#sr_hex.drop(['Unnamed: 0'], axis=1)
#print(sr_hex.head())
#new.to_csv('sr_hexShaun.csv')
#sr_hex.to_csv('hex_shaun.csv',index=False)
#csv-diff one.csv two.csv



#Practice
#merge1 = pd.read_csv ('Data/service_request/merge1.csv')
#merge2 = pd.read_csv ('Data/service_request/merge2.csv')

#new_merge = pd.merge(merge1,merge2, how='left', left_on = 'ID', right_on = 'ID', indicator= True)
#print(new_merge.dtypes(merge1, columns = ['ID']))
#print(merge1['ID'].dtypes)
#print(new_merge)