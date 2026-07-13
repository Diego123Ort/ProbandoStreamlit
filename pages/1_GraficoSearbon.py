import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Gráfico con Seaborn")

df = pd.DataFrame({
    "Producto": ["Laptop", "Celular", "Tablet", "Monitor", "Teclado"],
    "Ventas": [35, 50, 25, 40, 20]
})

fig, ax = plt.subplots()

sns.barplot(
    data=df,
    x="Producto",
    y="Ventas",
    palette="viridis",
    ax=ax
)

st.pyplot(fig)