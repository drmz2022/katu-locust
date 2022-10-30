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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
