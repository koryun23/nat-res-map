import folium
import pandas
map = folium.Map(location=[40.0691, 45.0382], zoom_start=8, tiles="Stamen Terrain")
def generate_colors(arg):
    if arg == 'CALCITE':
        color = 'red'
    elif arg == 'TUFF':
        color = 'yellow'
    elif arg == 'COPPER':
        color = 'black'
    elif arg == 'MULTI-METAL ORE':
        color = 'grey'
    elif arg == 'BASALT':
        color = 'green'
    elif arg == 'SALT':
        color = 'brown'
    elif arg == "CHROME":
        color = 'orange'
    return color
data = pandas.read_csv('natres.txt', sep=';')
natural_resources = list(data['NATRES'])
lon = list(data['LON'])
lat = list(data['LAT'])

print(natural_resources)
fg_calcite = folium.FeatureGroup(name='կրաքար')
fg_tuff = folium.FeatureGroup(name='տուֆ')
fg_copper = folium.FeatureGroup(name='պղինձ')
fg_basalt = folium.FeatureGroup(name='բազալտ')
fg_salt = folium.FeatureGroup(name='կերակրի աղ')
fg_chrome = folium.FeatureGroup(name='քրոմիտ')
fg_mmore = folium.FeatureGroup(name='բազմամետաղային հանքաքար')
for i in range(len(natural_resources)):
    if 'CALCITE' == natural_resources[i]:
        fg_calcite.add_child(folium.CircleMarker(location=[lon[i], lat[i]], popup=str(lon[i])+' '+str(lat[i]), radius=6, fill_color=generate_colors('CALCITE'), color=generate_colors('CALCITE'), fill_opacity=0.7))
    elif 'TUFF' == natural_resources[i]:
        fg_tuff.add_child(folium.CircleMarker(location=[lon[i], lat[i]], popup=str(lon[i])+' '+str(lat[i]), radius=6, fill_color=generate_colors('TUFF'), color=generate_colors('TUFF'), fill_opacity=0.7))
    elif 'COPPER' == natural_resources[i]:
        fg_copper.add_child(folium.CircleMarker(location=[lon[i], lat[i]], popup=str(lon[i])+' '+str(lat[i]), radius=6, fill_color=generate_colors('COPPER'), color=generate_colors('COPPER'), fill_opacity=0.7))
    elif 'BASALT' == natural_resources[i]:
        fg_basalt.add_child(folium.CircleMarker(location=[lon[i], lat[i]], popup=str(lon[i])+' '+str(lat[i]), radius=6, fill_color=generate_colors('BASALT'), color=generate_colors('BASALT'), fill_opacity=0.7))
    elif 'SALT' == natural_resources[i]:
        fg_salt.add_child(folium.CircleMarker(location=[lon[i], lat[i]], popup=str(lon[i])+' '+str(lat[i]), radius=6, fill_color=generate_colors('SALT'), color=generate_colors('SALT'), fill_opacity=0.7))
    elif 'CHROME' == natural_resources[i]:
        fg_chrome.add_child(folium.CircleMarker(location=[lon[i], lat[i]], popup=str(lon[i])+' '+str(lat[i]), radius=6, fill_color=generate_colors('CHROME'), color=generate_colors('CHROME'), fill_opacity=0.7))
    elif 'MULTI-METAL ORE' == natural_resources[i]:
        fg_mmore.add_child(folium.CircleMarker(location=[lon[i], lat[i]], popup=str(lon[i])+' '+str(lat[i]), radius=6, fill_color=generate_colors('MULTI-METAL ORE'), color=generate_colors('MULTI-METAL ORE'), fill_opacity=0.7))
map.add_child(fg_calcite)
map.add_child(fg_tuff)
map.add_child(fg_copper)
map.add_child(fg_basalt)
map.add_child(fg_salt)
map.add_child(fg_chrome)
map.add_child(fg_mmore)

map.add_child(folium.LayerControl())

map.save('new_map.html')
