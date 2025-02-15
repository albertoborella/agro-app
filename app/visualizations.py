import streamlit as st
import plotly.express as px

def mostrar_graficos(df):
    fig = px.line(df, x='Fecha', y='Total Producido', title='Tendencia de Producción Total de Leche', markers=True)
    fig.update_layout(xaxis_title='Fecha', yaxis_title='Producción Total (Litros)', xaxis_tickformat='%d/%m/%y')
    st.plotly_chart(fig)