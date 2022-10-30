import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("О нас")
st.sidebar.info(
    """
   Казахский агротехнический университет имени С.Сейфуллина: <https://kazatu.edu.kz/>
   
    """
)

st.sidebar.title("Контакты")
st.sidebar.info(
    """
   2022
    """
)

st.title("Методика матмоделей")

with st.expander("Входные данные"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
        regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

        m.add_geojson(regions, layer_name='US Regions')
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column='region',
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )
image= 'satelliteimgs/meteo.png'
st.image(image, caption =" Расположение метеостанций")

m.to_streamlit(height=700)
