import streamlit as st  
from forms import mostrar_formulario
from data import agregar_datos

with st.sidebar:
      st.page_link("main.py",label="Inicio")
      st.page_link("pages/tabla_produccion_leche.py",label="Producción de Leche")
      st.page_link("pages/tabla_precios_leche.py", label="Precios por litro de leche")
      st.page_link("pages/analisis_produccion.py", label="Anáĺisis de Producción de Leche")
      st.page_link('pages/datos_produccion.py', label="Ingreso de producción")
      st.page_link("pages/datos_precios_leche.py", label="Ingreso del precio de leche")
      
st.markdown("<h3 style='text-align:center;'>Ingreso de datos de Producción de Leche</h3>", unsafe_allow_html=True)
mostrar_formulario(agregar_datos)