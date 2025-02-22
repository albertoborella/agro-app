import streamlit as st
# import utilidades as util 

def main():
    
   with st.sidebar:
      st.page_link("main.py",label="Inicio")
      st.page_link("pages/tabla_produccion_leche.py",label="Producción de Leche")
      st.page_link("pages/tabla_precios_leche.py", label="Precios por litro de leche")
      st.page_link("pages/analisis_produccion.py", label="Anáĺisis de Producción de Leche")
      st.page_link('pages/datos_produccion.py', label="Ingreso de producción")
      st.page_link("pages/datos_precios_leche.py", label="Ingreso del precio de leche")

if __name__ == '__main__':
    main()
    st.title("Bienvenido a la aplicación de análisis de producción de leche")
    st.write("Esta aplicación permite analizar la producción de leche de una granja y los precios de la leche en el mercado.")
    st.write("Para comenzar, seleccione una opción del menú lateral.")
    st.write("Si desea ingresar datos, seleccione la opción correspondiente en el menú lateral.")
    st.write("Si desea analizar los datos, seleccione la opción correspondiente en el menú lateral.")
