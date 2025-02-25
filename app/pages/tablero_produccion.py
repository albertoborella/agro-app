import streamlit as st 
import pandas as pd  
import matplotlib.pyplot as plt  
import plotly.express as px 
from data import * 
from visualizations import ultimas_producciones, mostrar_produccion_mensual
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)
with st.sidebar:
    st.page_link("main.py", label="🏠 Inicio")
    st.page_link("pages/tablero_produccion.py", label="📊 Tablero mensual de producción")
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
df_produccion_copy['Fecha'] = pd.to_datetime(df_produccion_copy['Fecha'], dayfirst=True)
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
# Formatear la columna 'Fecha' en el formato día/mes/año
df_produccion_filtrado.loc[:, 'Fecha'] = pd.to_datetime(df_produccion_filtrado['Fecha']).dt.strftime('%d/%m/%Y')
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
# Calcular el total producido en el mes en curso y en el mes anterior
total_producido_actual = df_produccion_copy[(df_produccion_copy['Año'] == parAnio) & (df_produccion_copy['Mes'] == meses_numeros[parMes])]['Total Producido'].sum()
if meses_numeros[parMes] == 1:
    mes_anterior_produccion = 12
    anio_anterior_produccion = parAnio - 1
else:
    mes_anterior_produccion = meses_numeros[parMes] - 1
    anio_anterior_produccion = parAnio
total_producido_anterior = df_produccion_copy[(df_produccion_copy['Año'] == anio_anterior_produccion) & (df_produccion_copy['Mes'] == mes_anterior_produccion)]['Total Producido'].sum()

# Calcular la variación y el porcentaje
variacion_precio = precio_ultimo_mes['Precio'].values[0] - precio_mes_anterior['Precio'].values[0]
porcentaje_variacion = (variacion_precio / precio_mes_anterior['Precio'].values[0]) * 100
# Determinar la dirección de la flecha
if variacion_precio > 0:
    flecha = "⬆️"  # Flecha hacia arriba
elif variacion_precio < 0:
    flecha = "⬇️"  # Flecha hacia abajo
else:
    flecha = "➡️"  # Sin variación
# Calcular la variación de producción y el porcentaje
variacion_produccion = total_producido_actual - total_producido_anterior
porcentaje_variacion_produccion = (variacion_produccion / total_producido_anterior) * 100 if total_producido_anterior != 0 else 0
# Determinar la dirección de la flecha para la producción
if variacion_produccion > 0:
    flecha_produccion = "⬆️"  # Flecha hacia arriba
elif variacion_produccion < 0:
    flecha_produccion = "⬇️"  # Flecha hacia abajo
else:
    flecha_produccion = "➡️"  # Sin variación

st.markdown("<div style='text-align: center;'><h2>Tablero de producción</h2></div>", unsafe_allow_html=True)
# Metricas
c1, c2, c3, c4, c5, c6 = st.columns(6)
# Función para crear una tarjeta estilizada
def tarjeta(titulo, valor, flecha=None, color_fondo="#f9f9f9", color_texto="#4272f5"):
    return f"""
    <div style='border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: {color_fondo}; text-align: center;'>
        <p style='margin: 0; font-size: 16px; text-align: center'>{titulo}</p>
        <p style='font-size: 17px; font-weight: 600; color: {color_texto};'>{flecha if flecha else ''} {valor}</p>
    </div>
    """
with c1:
    st.markdown(tarjeta("Producción mes anterior", "lts.", total_producido_anterior), unsafe_allow_html=True)
with c2:
    st.markdown(tarjeta("Producción mes actual", "lts.",total_producido_actual), unsafe_allow_html=True)
with c3:
    st.markdown(tarjeta("Variación de Producción", f"{abs(porcentaje_variacion_produccion):.2f}%", flecha_produccion), unsafe_allow_html=True)
with c4:
    st.markdown(tarjeta("Precio anterior cobrado", "$",precio_mes_anterior['Precio'].values[0]), unsafe_allow_html=True)
with c5:
    st.markdown(tarjeta("Último precio cobrado", "$",precio_ultimo_mes['Precio'].values[0]), unsafe_allow_html=True)
with c6:
    st.markdown(tarjeta("Variación de Precio", f"{abs(porcentaje_variacion):.2f}%", flecha), unsafe_allow_html=True)
st.markdown("""
        <hr style="height: 4px; border: none; color: #FF5733; background-color: #FF5733;" />
    """, unsafe_allow_html=True)
# Mostrar producción diaria
st.markdown("<div><h3>Producción diaria en el período</h3></div>", unsafe_allow_html=True)
st.dataframe(df_produccion_filtrado.drop(columns=['Mes', 'Mes Nombre', 'Año']))
# Llamar a las funciones para mostrar visualizaciones (asegúrate de que estas funciones hagan algo)
ultimas_producciones()
mostrar_produccion_mensual()