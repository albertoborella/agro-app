import pandas as pd  
import streamlit as st  
import os
import uuid

# Nombre del archivo CSV
csv_file = 'produc_leche.csv'

# Función para crear el archivo CSV si no existe
def crear_csv():
    if not os.path.isfile(csv_file):
        df = pd.DataFrame(columns=['id','Fecha','Litros Vendidos','Litros Consumidos'])
        df.to_csv(csv_file, index=False)

# Funcion para agregar datos al CSV
def agregar_datos(fecha, litros_vend, litros_cons):
    # Generar un ID único
    nuevo_id = str(uuid.uuid4())
    # Crear un nuevo DataFrame con los datos
    nuevo_dato = pd.DataFrame([[nuevo_id, fecha, litros_vend, litros_cons]], columns=['id', 'Fecha', 'Litros Vendidos', 'Litros Consumidos'])
    # Leer el archivo CSV existente
    df_existente = pd.read_csv(csv_file)
    # Concatenar el nuevo dato al DataFrame existente
    df_actualizado = pd.concat([df_existente, nuevo_dato], ignore_index=True)
    # Guardar el DataFrame actualizado en el archivo CSV
    df_actualizado.to_csv(csv_file, index=False) 

# Crear el archivo CSV si no existe
crear_csv()

def main():

    # Crear un sidebar para colocar un menú de multiples páginas
    

    # Crear un formulario para ingresar los datos
    st.subheader('Ingresar datos de Producción')
    with st.form(key='formulario',clear_on_submit=True):
        fecha = st.date_input('Fecha')
        litros_vend = st.number_input('Litros vendidos', min_value=0, step=1)
        litros_cons = st.number_input('Litros consumidos', min_value=0, step=1)

        # Boton para agregar datos
        submit_button = st.form_submit_button('Agregar datos')

        if submit_button:
            if fecha > pd.to_datetime('today').date():
                st.error('La fecha no puede ser futura.')
            else:
                agregar_datos(fecha, litros_vend, litros_cons)
                st.success('Datos agregados exitosamente!')

        # Mostrar los datos actuales del archivo CSV
        st.subheader('Datos registrados')
        df_actual = pd.read_csv(csv_file)
        df_actual['Total'] = df_actual['Litros Vendidos'] + df_actual['Litros Consumidos']
        df_actual_sin_id = df_actual.drop(columns=['id'])  # Eliminar la columna 'id'
        st.write(df_actual_sin_id)



if __name__ == '__main__':
    main()