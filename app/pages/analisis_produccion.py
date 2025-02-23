import streamlit as st
from visualizations import ultimas_producciones, mostrar_produccion_mensual

with st.sidebar:
      st.page_link("main.py",label="Inicio")
      st.page_link('pages/datos_produccion.py', label="Produccion diaria de leche y precio mensual")
      st.page_link("pages/tabla_produccion_leche.py",label="Tablas de produccion y precio de ventas")
      st.page_link("pages/analisis_produccion.py", label="Anáĺisis mensual de producción")
      
st.markdown("<h3 style='text-align:center;'>Análisis de la Producción de Leche</h3>", unsafe_allow_html=True)
ultimas_producciones()
mostrar_produccion_mensual()