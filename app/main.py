import streamlit as st

st.set_page_config(
      layout="wide",
      initial_sidebar_state="expanded",
)

def main():
    
   with st.sidebar:
      st.page_link("main.py",label="🏠 Inicio")
      st.page_link('pages/datos_produccion.py', label="📈 Produccion diaria de leche")
      st.page_link("pages/tabla_produccion_leche.py",label="📋 Tablas de produccion")
      st.page_link("pages/tablero_produccion.py", label="📊 Tablero mensual de producción")
   
if __name__ == '__main__':
    main()
    st.markdown(
        "<h3 style='text-align: center;'>Bienvenido a la aplicación de análisis de producción de leche</h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h3 style='text-align: center;color: #4272f5;'>Maria Emilia Armando</h3>",
        unsafe_allow_html=True
    )
    st.markdown("""
        <hr style="height: 4px; border: none; color: #FF5733; background-color: #FF5733;" />
    """, unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;color:#1e1e1f;'>Esta aplicación permite analizar la producción de leche del establecimiento y los precios pagados por la industria.</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;color:#1e1e1f;'>Es recomendable tener los datos de producción diaria actualizados para no causar distorsiones.</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;color:#1e1e1f;'>Si desea ingresar datos de producción diaria o modificar el precio pagado por la industria seleccione la opción correspondiente en el menú lateral.</h6>", unsafe_allow_html=True)
