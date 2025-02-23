import streamlit as st  
from data import *

st.set_page_config(
      layout="wide",
      initial_sidebar_state="expanded",
)

with st.sidebar:
      st.page_link("main.py",label="Inicio")
      st.page_link('pages/datos_produccion.py', label="Produccion diaria de leche y precio mensual")
      st.page_link("pages/tabla_produccion_leche.py",label="Tablas de produccion y precio de ventas")
      st.page_link("pages/analisis_produccion.py", label="Anáĺisis mensual de producción")

st.markdown("<h3 style='text-align:center;'>Ingreso de datos de Producción de Leche</h3>", unsafe_allow_html=True)    
c1, c2 = st.columns([65,35])
with c1:
      st.markdown("<h5 style='text-align:center;'>Datos de Producción de Leche</h5>", unsafe_allow_html=True)
      df_actual = cargar_datos()
      st.write(df_actual)
with c2:
      st.markdown("<h5 style='text-align:center;'>Precios de litro de leche</h5>", unsafe_allow_html=True)
      df_actual = cargar_precio()
      st.write(df_actual)