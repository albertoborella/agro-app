import streamlit as st  
from forms import mostrar_formulario, mostrar_formulario_precios
from data import agregar_datos, agregar_precio

with st.sidebar:
      st.page_link("main.py",label="Inicio")
      st.page_link('pages/datos_produccion.py', label="Produccion diaria de leche y precio mensual")
      st.page_link("pages/tabla_produccion_leche.py",label="Tablas de produccion y precio de ventas")
      st.page_link("pages/analisis_produccion.py", label="Anáĺisis mensual de producción")

st.markdown("<h3 style='text-align:center;'>Ingreso de datos de Producción de Leche</h3>", unsafe_allow_html=True)    
c1, c2 = st.columns(2)
with c1:
      st.markdown("<h5 style='text-align:center;'>Ingreso de datos de Producción</h5>", unsafe_allow_html=True)
      mostrar_formulario(agregar_datos)
with c2:
      st.markdown("<h5 style='text-align:center;'>Modificacion precios de leche</h5>", unsafe_allow_html=True)
      mostrar_formulario_precios(agregar_precio)