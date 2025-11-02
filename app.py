import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Coches')

print("Con este botón, verás un histograma que refleja la cantidad de coches disponibles por la distancia que han recorrido (en Millas)")

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

print("Con este botón, verás un gráfico de dispersión que refleja la relación de la distancia que los coches han recorrido (en Millas) y su precio")

disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)

