import streamlit as st
import common

common.page_config()

st.title("Air Pollution data - Seoul")
st.caption("""
데이터셋 출처: https://www.kaggle.com/datasets/bappekim/air-pollution-in-seoul  
""")
st.write("""
본 데이터셋은 2017년부터 2019년까지의 서울시 대기 오염 물질에 대한 데이터셋입니다.  
서울시 내 총 25개 측정 장소에서의 대기 오염 물질($\mathbf{SO}_2$, $\mathbf{NO}_2$, $\mathbf{O}_3$, PM10, PM2.5)의 농도를 이용합니다.
""")
st.image("img/dataset_cover.jpg")