import streamlit as st
import pandas as pd

st.title("Mi primer Dashboard")

st.write("¡Hola! Este es mi primer dashboard con Streamlit.")

nombre = st.text_input("¿Cómo te llamas?")

if nombre:
    st.success(f"Bienvenido, {nombre} 👋")


if st.button("Haz clic"):
    st.balloons()
    st.write("¡Funcionó!")

edad = st.slider("Selecciona tu edad", 0, 100)



st.write("Tu edad:", edad)

df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [20, 25, 30]
})

st.table(df)

st.write("GRAFICO DE VENTAS:")
df = pd.DataFrame({
    "Ventas": [10, 15, 8, 20, 30]
})

st.line_chart(df)