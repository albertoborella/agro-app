import pandas as pd
import os
import uuid

csv_file = 'produc_leche.csv'

def crear_csv():
    if not os.path.isfile(csv_file):
        df = pd.DataFrame(columns=['id', 'Fecha', 'Litros Vendidos', 'Litros Consumidos'])
        df.to_csv(csv_file, index=False)

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