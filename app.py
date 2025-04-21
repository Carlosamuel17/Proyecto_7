import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') 

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # al hacer clic en el botón se crea un mensaje y el histograma interactivo
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")    
    st.plotly_chart(fig, use_container_width=True)