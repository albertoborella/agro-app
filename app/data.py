import pandas as pd
import os
import uuid
from datetime import datetime

csv_file = 'produc_leche.csv'
precio_csv_file = 'precio_leche.csv'

def crear_csv():
    if not os.path.isfile(csv_file):
        df = pd.DataFrame(columns=['id', 'Fecha', 'Litros Vendidos', 'Litros Consumidos'])
        df.to_csv(csv_file, index=False)

def crear_precio_csv():
    if not os.path.isfile(precio_csv_file):
        df = pd.DataFrame(columns=['id', 'Mes', 'Año', 'Precio'])
        df.to_csv(precio_csv_file, index=False)

def agregar_datos(fecha, litros_vend, litros_cons):
    nuevo_id = str(uuid.uuid4())
    # Convertir la fecha a datetime
    fecha_dt = pd.to_datetime(fecha)
    
    nuevo_dato = pd.DataFrame([[nuevo_id, fecha_dt, litros_vend, litros_cons]], columns=['id', 'Fecha', 'Litros Vendidos', 'Litros Consumidos'])
    df_existente = pd.read_csv(csv_file)
    df_actualizado = pd.concat([df_existente, nuevo_dato], ignore_index=True)
    df_actualizado.to_csv(csv_file, index=False)

# def cargar_datos():
#     crear_csv()  # Asegúrate de que esta función esté definida
#     df = pd.read_csv(csv_file)
#     # Convertir la columna 'Fecha' a datetime
#     df['Fecha'] = pd.to_datetime(df['Fecha'])
#     # Calcular el total producido
#     df['Total Producido'] = df['Litros Vendidos'] + df['Litros Consumidos']
#     # Eliminar la columna 'id'
#     df = df.drop(columns=['id'])
#     # Ordenar por fecha
#     #df = df.sort_values(by='Fecha', ascending=False)
#     return df

def cargar_datos():
    try:
        crear_csv()  # Asegúrate de que esta función esté definida
        df = pd.read_csv(csv_file)
        # Limpiar la columna 'Fecha'
        df['Fecha'] = df['Fecha'].str.strip().str.replace(' 00:00:00', '', regex=False)
        # Convertir la columna 'Fecha' a datetime
        df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
        # Calcular el total producido
        df['Total Producido'] = df['Litros Vendidos'] + df['Litros Consumidos']
        # Eliminar la columna 'id'
        df = df.drop(columns=['id'])
        df = df.sort_values(by='Fecha', ascending=False)
        return df
    except Exception as e:
        print(f"Error al cargar datos: {e}")

# Diccionario para convertir nombres de meses a números
meses = {
    'Enero': 1,
    'Febrero': 2,
    'Marzo': 3,
    'Abril': 4,
    'Mayo': 5,
    'Junio': 6,
    'Julio': 7,
    'Agosto': 8,
    'Septiembre': 9,
    'Octubre': 10,
    'Noviembre': 11,
    'Diciembre': 12
}
def agregar_precio(mes, año, precio):
    nuevo_id = str(uuid.uuid4())
    # Convertir el mes de texto a número
    mes_numero = meses.get(mes)
    if mes_numero is None:
        raise ValueError(f"Mes '{mes}' no es válido.")
    # No necesitas crear una fecha si no la vas a usar
    nuevo_dato = pd.DataFrame([[nuevo_id, mes, año, precio]], columns=['id', 'Mes', 'Año', 'Precio'])
    # Leer el CSV existente
    df_existente = pd.read_csv(precio_csv_file)
    # Concatenar los nuevos datos
    df_actualizado = pd.concat([df_existente, nuevo_dato], ignore_index=True)
    # Guardar el DataFrame actualizado en el CSV
    df_actualizado.to_csv(precio_csv_file, index=False)

# Diccionario inverso para convertir números de meses a nombres
meses_inverso = {v: k for k, v in meses.items()}
def cargar_precio():
    try:
        crear_precio_csv()  # Asegúrate de que esta función esté definida
        df = pd.read_csv(precio_csv_file)
        # Limpiar la columna 'Mes' y 'Año' si es necesario
        df['Mes'] = df['Mes'].str.strip()
        df['Año'] = df['Año'].astype(int)  # Asegurarse de que 'Año' sea un entero
        # Convertir 'Mes' a un número si es necesario
        df['Mes'] = df['Mes'].map(meses)
         # Eliminar la columna 'id'
        df = df.drop(columns=['id'])
        # Convertir los números de mes de vuelta a nombres
        df['Mes'] = df['Mes'].map(meses_inverso)
        # Ordenar por 'Año' y 'Mes' en forma descendente
        df = df.sort_values(by=['Año', 'Mes'], ascending=[False, False])
        return df
    except Exception as e:
        print(f"Error al cargar precios: {e}")
