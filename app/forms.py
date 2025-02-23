import streamlit as st
from datetime import datetime
#from data import agregar_precio, cargar_precios

# Formulario para ingresar litros vendidos y consumidos
def mostrar_formulario(agregar_datos):
    with st.form(key='formulario', clear_on_submit=True):
        fecha = st.date_input('Fecha')
        litros_vend = st.number_input('Litros vendidos', min_value=0, step=1)
        litros_cons = st.number_input('Litros consumidos', min_value=0, step=1)
        submit_button = st.form_submit_button('Agregar datos')
        if submit_button:
            agregar_datos(fecha, litros_vend, litros_cons)
            st.success(f"Litros Totales Producidos el {fecha}: {litros_vend + litros_cons} litros")

# Formulario para ingresar datos
def mostrar_formulario_precios(agregar_precio):
    with st.form(key='precio_form'):
        mes = st.selectbox("Selecciona el mes:", 
                        ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        año = st.number_input("Ingresa el año:", min_value=2000, max_value=2100, value=2025)
        precio = st.number_input("Ingresa el precio:", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button(label='Agregar Precio')

        if submit_button:
            agregar_precio(mes, año, precio)
            st.success(f"Precio de leche agregado: {mes} {año} - ${precio:.2f}")



        

