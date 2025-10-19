import streamlit as st
import pandas as pd
import tensorflow as tf

model_caminho = "C:\Users\felip\OneDrive\Documentos\converted_keras"
model = tf.keras.models.load_models(model_caminho)

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

print("top")
print('67")
