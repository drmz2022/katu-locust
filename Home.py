import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("О нас")
st.sidebar.info(
    """
    КАТУ имени С.Сейфуллина
    : <https://kazatu.edu.kz/>
    """
)

st.sidebar.title("Контакты")
st.sidebar.info(
    2022
)

st.title("Разработка и совершенствование интегрированных систем защиты плодовых, овощных, зерновых, кормовых, бобовых и карантина растений")

st.markdown(
    """
   2.	Цель программы.
Адаптация прогрессивных агротехнологий в борьбе с карантинными и особо опасными вредными организмами в целях обеспечения фитосанитарной безопасности в АПК Республики Казахстан. .

    """
)

st.info("Навигация по веб-порталу.")

#st.subheader("Timelapse of Satellite Imagery")
#st.markdown(
#"""
 #   The following timelapse animations were created using the Timelapse web app. Click `Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
#"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
