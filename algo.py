import streamlit as st
import pandas as pd


# Cria um DataFrame com dados de exemplo
df = pd.DataFrame({
    "m": ["A", "B"],
    "n": [100, 20]

})

# Exibe o gráfico
st.bar_chart(
    data=df, 
    x="m", 
    y="n", 
    
    )

