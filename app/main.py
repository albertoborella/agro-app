import streamlit as st
# import utilidades as util 

st.set_page_config(
      layout="wide",
      initial_sidebar_state="expanded",
)

def main():
    
   with st.sidebar:
      st.page_link("main.py",label="Inicio")
      st.page_link('pages/datos_produccion.py', label="Produccion diaria de leche y precio mensual")
      st.page_link("pages/tabla_produccion_leche.py",label="Tablas de produccion y precio de ventas")
      st.page_link("pages/analisis_produccion.py", label="Anáĺisis mensual de producción")
   
if __name__ == '__main__':
    main()
    st.subheader("Bienvenido a la aplicación de análisis de producción de leche")
    st.write("Esta aplicación permite analizar la producción de leche de una granja y los precios pagados por la industria.")
    st.write("Para comenzar, seleccione una opción del menú lateral.")
    st.write("Si desea ingresar datos de producción diaria o modificar el precio pagado por la industria seleccione la opción correspondiente en el menú lateral.")
