import streamlit as st
 
def mostrar_formulario(agregar_datos):
    st.subheader('Ingresar datos de Producción')
    with st.form(key='formulario', clear_on_submit=True):
        fecha = st.date_input('Fecha')
        litros_vend = st.number_input('Litros vendidos', min_value=0, step=1)
        litros_cons = st.number_input('Litros consumidos', min_value=0, step=1)
        submit_button = st.form_submit_button('Agregar datos')
        if submit_button:
            agregar_datos(fecha, litros_vend, litros_cons)
