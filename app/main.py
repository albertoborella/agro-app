import streamlit as st
from forms import mostrar_formulario, mostrar_formulario_precios
from data import cargar_datos, agregar_datos, agregar_precio, cargar_precios
from visualizations import mostrar_graficos

def main():
    #st.title('Producción de Leche')

    # Crear el menú de seleccion
    menu = st.sidebar.selectbox('Selecciona una opción', ['Ingreso de produccion de leche',
                                                          'Ingreso el Precio de Leche',
                                                          'Tabla de Producción de Leche',
                                                          'Tabla de Precios de Leche'])

    if menu == "Ingreso de produccion de leche":
        st.subheader("Ingreso de datos de Producción de Leche")
        mostrar_formulario(agregar_datos)
    elif menu == "Tabla de Producción de Leche":
        st.subheader("Tabla de datos de Producción de Leche")
        df_actual = cargar_datos()
        st.write(df_actual)
    elif menu == "Ingreso el Precio de Leche":
        st.subheader("Precio de Leche vendida a Industria")
        mostrar_formulario_precios(agregar_precio)
    elif menu == "Tabla de Precios de Leche":
        st.subheader("Tabla de datos de Precios de Leche")
        df_actual = cargar_precios()
        st.write(df_actual)
        # Mostrar gráficos
        #mostrar_graficos(df_actual)

if __name__ == '__main__':
    main()