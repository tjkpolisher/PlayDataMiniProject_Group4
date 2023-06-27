import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_data():
    data = pd.read_csv("https://media.githubusercontent.com/media/qkrtnqls1216/air_pollution/main/Measurement_summary.csv")
    data[['Latitude', 'Longitude']] = data[['Latitude', 'Longitude']].replace("-", np.NaN)
    data[['Latitude', 'Longitude']] = data[['Latitude', 'Longitude']].astype('f')
    data.dropna(inplace=True)
    return data

def page_config():
    st.set_page_config(
        page_title="Air Pollution - Seoul",
        page_icon="🏭"
    )