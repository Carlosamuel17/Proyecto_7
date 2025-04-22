import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import streamlit as st # type: ignore

car_data = pd.read_csv('vehicles_us.csv') 

st.title('Datos de anuncios de coches')
st.text('En esta página web podremos analizar el dataframe sobre \nanuncios de coches, contiene la siguiente información:')

st.dataframe(car_data)

build_histogram = st.checkbox('Construir histograma de distancia recorrida')

if build_histogram: # al hacer clic en el botón se crea un mensaje y el histograma interactivo
    st.write('Histograma de distancia recorrida por el coche')
    fig = px.histogram(car_data, x="odometer", )    
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión de precio vs distancia recorrida')

if build_scatter: # al hacer clic en el botón se crea un mensaje y el gráfico de dispersión interactivo
    st.write('Gráfico de disperción de precio vs distancia recorrida')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

