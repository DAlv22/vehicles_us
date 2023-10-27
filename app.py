import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us_formatted.csv') # leer los datos
st.header('Visualización de conjunto de datos de anuncios de venta de coches')
st.write('Esta aplicación es una práctica')


show_only_excellent_condition = st.checkbox('Mostrar solo vehículos en condición excelente')
if show_only_excellent_condition:
    car_data = car_data[car_data['condition'] == 'excellent']
    car_data = car_data.reset_index(drop=True)
st.dataframe(car_data)


hist_button = st.checkbox('Construir histograma')

if hist_button:
    st.write('Distribución de kilometraje de vehículos')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.checkbox('Contruir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre kilometraje y precio de vehículos')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


selected_type = st.selectbox(
    'Seleccione el tipo de vehículo',
    car_data['type'].unique())
filtered_data = car_data[car_data['type'] == selected_type]
filtered_data = filtered_data.reset_index(drop=True)
st.dataframe(filtered_data)
