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

# Customize page title
st.title("Разработка и совершенствование интегрированных систем защиты плодовых, овощных, зерновых, кормовых, бобовых и карантина растений")

st.markdown(
    """
Цель программы:
Адаптация прогрессивных агротехнологий в борьбе с карантинными и особо опасными вредными организмами в целях обеспечения фитосанитарной безопасности в АПК Республики Казахстан. 

    """
)

st.header("3.Задачи программы.")

markdown = """
1. 	Проектирование интегрированной системы защиты растений от вредных организмов. 
2. 	Разработка математической модели развития вредных организмов. 


"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True, center=[54.177862,69.536348],
    zoom=12)
m.add_basemap("HYBRID")
m.to_streamlit(width=1000, height=400)
