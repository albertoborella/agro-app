import streamlit as st
from forms import mostrar_formulario
from data import cargar_datos, agregar_datos
from visualizations import mostrar_graficos

def main():
    st.title('Producción de Leche')

    # Mostrar formulario
    mostrar_formulario(agregar_datos)

    # Cargar y mostrar datos
    df_actual = cargar_datos()
    st.subheader('Datos registrados')
    st.write(df_actual)

    # Mostrar gráficos
    mostrar_graficos(df_actual)

if __name__ == '__main__':
    main()