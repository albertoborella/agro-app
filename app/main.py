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
      st.page_link("pages/tablero_produccion.py", label="Tablero mensual de produccion")
   
if __name__ == '__main__':
    main()
    st.markdown(
        "<h3 style='text-align: center;'>Bienvenido a la aplicación de análisis de producción de leche</h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: center;color: #fcba03;'>María Emilia Armando</h4>",
        unsafe_allow_html=True
    )
    st.markdown("""
        <hr style="height: 4px; border: none; color: #FF5733; background-color: #FF5733;" />
    """, unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;color:#bdb8aa;'>Esta aplicación permite analizar la producción de leche del establecimiento y los precios pagados por la industria.</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;color:#bdb8aa;'>Es recomendable tener los datos de producción diaria actualizados para no causar distorsiones.</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;color:#bdb8aa;'>Si desea ingresar datos de producción diaria o modificar el precio pagado por la industria seleccione la opción correspondiente en el menú lateral.</h6>", unsafe_allow_html=True)
