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
**AP08052747**
Подпрограмма 102 «Грантовое финансирование научных исследований».
Приоритетное направление «Устойчивое развитие агропромышленного комплекса и безопасность сельскохозяйственной продукции»

    """
)

# Customize page title
st.title(" Фитосанитарный контроль за нестадными саранчовыми в земледельческих районах Северного Казахстана на основе инновации ГИС-технологий и методов дистанционного зондирования Земли")

st.markdown(
    """
**Объект исследования** - комплекс нестадных саранчовых вредителей, состоящий из 9 выявленных видов.

**Цель исследования** –  разработка методики фитосанитарного контроля нестадных саранчовых на основе ГИС-технологий и методов дистанционного зондирования для повышения эффективности защитных мероприятий и предотвращения ущерба от опасных вредителей в земледельческих районах Северного Казахстана.  
    """
)

st.header("3.Результаты исследований.")

markdown = """
1. 	Результат моделирования: Фундаментальная ниша ареала заселения 
нестадных саранчовых вредителей 
 
2. 	. Фитосанитарное зонирование земледельческих районов Северного Казахстана по степени заселенности и вредоносности комплекса вредных нестадных саранчовых в зависимости от агроклиматических условий . 


"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True, center=[54.177862,69.536348],
    zoom=12)
m.add_basemap("HYBRID")
m.to_streamlit(width=1000, height=400)
