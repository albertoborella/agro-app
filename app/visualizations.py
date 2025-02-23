import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from data import *

# Cargar datos de producción y precios
df_produccion = cargar_datos()
df_precios = cargar_precio()

# Gráfico de producción total de los últimos 30 registros
def ultimas_producciones():
    if len(df_produccion) > 30:
        produccion_df = df_produccion.tail(30)
    else:
        produccion_df = df_produccion

    # Gráfico de producción total diaria
    st.markdown("<h3 style='text-align:center;'>Evolución diaria - Ùltimos 30 registros</h3>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 5))
    plt.plot(produccion_df['Fecha'], produccion_df['Total Producido'], marker='o')
    plt.title('Evolución de la Producción Total')
    plt.xlabel('Fecha')
    plt.ylabel('Total Producido (Litros)')
    plt.grid()
    st.pyplot(plt)

#Función para mostrar el gráfico de producción mensual
def mostrar_produccion_mensual():
    # Seleccionar el año
    año_seleccionado = st.selectbox("Selecciona el año:", df_produccion['Fecha'].dt.year.unique())
    # Filtrar por el año seleccionado
    pd.to_datetime(df_produccion['Fecha'], errors='coerce')
    df_anio = df_produccion[df_produccion['Fecha'].dt.year == año_seleccionado]
    # Agrupar por mes y sumar la producción total
    df_mensual = df_anio.groupby(df_anio['Fecha'].dt.month).agg({'Total Producido': 'sum'}).reset_index()
    df_mensual['Mes'] = df_mensual['Fecha'].apply(lambda x: pd.to_datetime(f"{año_seleccionado}-{x}-01").strftime('%B'))
    # Crear gráfico de barras
    fig = px.bar(df_mensual, x='Mes', y='Total Producido', title=f'Total de Producción Mensual - {año_seleccionado}',
                 labels={'Total Producido': 'Producción Total (Litros)', 'Mes': 'Mes'})
    fig.update_layout(xaxis_title='Mes', yaxis_title='Producción Total (Litros)')
    st.plotly_chart(fig)




