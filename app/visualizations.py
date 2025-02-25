import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from data import *

# Cargar datos de producción y precios
df_produccion = cargar_datos()
df_precios = cargar_precio()

def ultimas_producciones():
    # La columna 'Fecha' en formato de fecha
    df_produccion['Fecha'] = pd.to_datetime(df_produccion['Fecha'], format='%d/%m/%Y', dayfirst=True)
    # Filtrar los registros de los últimos 10 días
    fecha_hasta = df_produccion['Fecha'].max()  # Obtener la fecha más reciente
    fecha_desde = fecha_hasta - pd.Timedelta(days=10)  # Calcular la fecha de hace 10 días
    produccion_df = df_produccion[(df_produccion['Fecha'] >= fecha_desde) & (df_produccion['Fecha'] <= fecha_hasta)]
    
    # Si hay menos de 10 registros, usar solo los disponibles
    if len(produccion_df) > 10:
        produccion_df = produccion_df.tail(10)
    st.markdown("<h5 style='text-align:center;'>Últimos 10 días de producción</h5>", unsafe_allow_html=True)
    plt.figure(figsize=(3, 1))
    plt.plot(produccion_df['Fecha'], produccion_df['Total Producido'], marker='o', markersize=1, linewidth=0.5)
    plt.title('')
    plt.xlabel('Fecha', fontsize=3)
    plt.ylabel('Litros', fontsize=3)
    # Ajustar la cuadrícula
    plt.grid(linewidth=0.5)  # Hacer la cuadrícula más fina
    # Ajustar las propiedades de los ejes
    ax = plt.gca()  # Obtener el objeto de los ejes actuales
    for spine in ax.spines.values():
        spine.set_linewidth(0.2)  # Hacer las líneas del borde más finas
    plt.xticks(fontsize=2.5)
    plt.yticks(fontsize=3)
    st.pyplot(plt)
    st.markdown("""
        <hr style="height: 4px; border: none; color: #FF5733; background-color: #FF5733;" />
    """, unsafe_allow_html=True)  

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
    fig = px.bar(df_mensual, x='Mes', y='Total Producido', title=f'Producción Mensual - {año_seleccionado}',
                 labels={'Total Producido': 'Producción Total (Litros)', 'Mes': 'Mes'})
    fig.update_layout(xaxis_title='Mes', yaxis_title='Producción Total (Litros)')
    st.plotly_chart(fig)




