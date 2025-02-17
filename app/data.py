import pandas as pd
import os
import uuid

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
    nuevo_dato = pd.DataFrame([[nuevo_id, fecha, litros_vend, litros_cons]], columns=['id', 'Fecha', 'Litros Vendidos', 'Litros Consumidos'])
    df_existente = pd.read_csv(csv_file)
    df_actualizado = pd.concat([df_existente, nuevo_dato], ignore_index=True)
    df_actualizado.to_csv(csv_file, index=False)

def cargar_datos():
    crear_csv()
    df = pd.read_csv(csv_file)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Fecha'] = df['Fecha'].dt.strftime('%d/%m/%y')
    df['Total Producido'] = df['Litros Vendidos'] + df['Litros Consumidos']
    df = df.drop(columns=['id'])
    return df

# Nuevas funciones para manejar precio_leche.csv
def agregar_precio(mes, año, precio):
    nuevo_id = str(uuid.uuid4())
    nuevo_dato = pd.DataFrame([[nuevo_id,mes,año,precio]], columns=['id','Mes','Año','Precio'])
    df_existente = pd.read_csv(precio_csv_file)
    df_actualizado = pd.concat([df_existente, nuevo_dato], ignore_index=True)
    df_actualizado.to_csv(precio_csv_file, index=False)

def cargar_precios():
    crear_precio_csv()
    df = pd.read_csv(precio_csv_file)
    df = df.drop(columns=['id'])
    return df
