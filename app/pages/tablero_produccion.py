import streamlit as st 
import pandas as pd    
import plotly.express as px 
from data import *  
st.set_page_config(
      layout="wide",
      initial_sidebar_state="expanded",
)

with st.sidebar:
      st.page_link("main.py",label="Inicio")
      st.page_link('pages/datos_produccion.py', label="Produccion diaria de leche y precio mensual")
      st.page_link("pages/tabla_produccion_leche.py",label="Tablas de produccion y precio de ventas")
      st.page_link("pages/analisis_produccion.py", label="Anáĺisis mensual de producción")
      st.page_link("pages/tablero_produccion.py", label="Tablero mensual de produccion")
# Cargar los datos
df_produccion = cargar_datos()  # Carga el DataFrame de Total Producido
df_precios = cargar_precio()     # Carga el DataFrame de precios
# Crear un diccionario para mapear nombres de meses a números
meses_numeros = {
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
# Si la columna 'Mes' tiene nombres de meses, conviértelos a números
if df_precios['Mes'].dtype == 'object':
    df_precios['Mes'] = df_precios['Mes'].map(meses_numeros)
# Procesar datos de Total Producido
df_produccion_copy = df_produccion.copy()
df_produccion_copy['Fecha'] = pd.to_datetime(df_produccion_copy['Fecha'])
df_produccion_copy['Año'] = df_produccion_copy['Fecha'].dt.year
df_produccion_copy['Mes'] = df_produccion_copy['Fecha'].dt.month
# Crear un diccionario para los nombres de los meses
meses_nombres = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
}
# Reemplazar los números de mes por sus nombres
df_produccion_copy['Mes Nombre'] = df_produccion_copy['Mes'].map(meses_nombres)
# Declaración de parámetros de la barra lateral
with st.sidebar:
    # Filtro de años y meses
    parAnio = st.selectbox('Año', options=df_produccion_copy['Año'].unique())
    parMes = st.selectbox('Meses', options=df_produccion_copy['Mes Nombre'].unique())
# Filtrar los DataFrames según los filtros seleccionados
df_produccion_filtrado = df_produccion_copy[(df_produccion_copy['Año'] == parAnio) & (df_produccion_copy['Mes Nombre'] == parMes)]
df_produccion_filtrado['Fecha'] = df_produccion_filtrado['Fecha'].dt.date
# Mostrar los datos filtrados
st.write("Datos de Total Producido filtrados:")
st.dataframe(df_produccion_filtrado.drop(columns=['Mes', 'Mes Nombre']))
# Filtrar precios del último mes registrado y el mes anterior
ultimo_anio = df_precios['Año'].max()
meses_disponibles = df_precios[df_precios['Año'] == ultimo_anio]['Mes'].unique()
ultimo_mes = meses_disponibles.max()
# Determinar el mes anterior
if ultimo_mes == 1:
    mes_anterior = 12
    anio_anterior = ultimo_anio - 1
else:
    mes_anterior = ultimo_mes - 1
    anio_anterior = ultimo_anio
# Filtrar los precios
precio_ultimo_mes = df_precios[(df_precios['Año'] == ultimo_anio) & (df_precios['Mes'] == ultimo_mes)]
precio_mes_anterior = df_precios[(df_precios['Año'] == anio_anterior) & (df_precios['Mes'] == mes_anterior)]
# Mostrar precios
st.write("Precio del último mes registrado:")
st.dataframe(precio_ultimo_mes)
st.write("Precio del mes anterior:")
st.dataframe(precio_mes_anterior)
# Calcular el total producido en el mes en curso y en el mes anterior
total_producido_actual = df_produccion_copy[(df_produccion_copy['Año'] == parAnio) & (df_produccion_copy['Mes'] == meses_numeros[parMes])]['Total Producido'].sum()  # Asegúrate de que 'Total Producido' sea el nombre correcto de la columna
st.write(f"Total producido en {parMes} {parAnio}: {total_producido_actual}")
# Calcular el total producido en el mes anterior
if meses_numeros[parMes] == 1:
    mes_anterior_produccion = 12
    anio_anterior_produccion = parAnio - 1
else:
    mes_anterior_produccion = meses_numeros[parMes] - 1
    anio_anterior_produccion = parAnio
total_producido_anterior = df_produccion_copy[(df_produccion_copy['Año'] == anio_anterior_produccion) & (df_produccion_copy['Mes'] == mes_anterior_produccion)]['Total Producido'].sum()  # Asegúrate de que 'Total Producido' sea el nombre correcto de la columna
st.write(f"Total producido en {meses_nombres[mes_anterior_produccion]} {anio_anterior_produccion}: {total_producido_anterior}")

