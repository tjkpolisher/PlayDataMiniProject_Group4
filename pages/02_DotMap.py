import streamlit as st
from streamlit_folium import st_folium
import folium
import common
from folium.plugins import MarkerCluster
import numpy as np

common.page_config()
st.title("Dot Map Visualization")

df = common.get_data()

location = df.groupby('Station code')['PM2.5'].agg([np.mean])
location['Latitude'] = df['Latitude'].unique()
location['Longitude'] = df['Longitude'].unique()


def color_select(x):
    if x >= 30:
        return 'red'
    elif x >= 25:
        return 'yellow'
    else:
        return 'blue'

# Map 초기화
seoul = folium.Map(location=[37.4971850, 126.927595], zoom_start=14)

# Circle
for i in range(len(location)):
    folium.Circle(location=[location.iloc[i,1], location.iloc[i,2]], radius = location.iloc[i, 0] * 40, color=color_select(location.iloc[i,0]),fill_color='#ffffgg').add_to(seoul)

# Marker / Sejong Univ.
folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='아지트', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)

st_folium(seoul, width=1000)