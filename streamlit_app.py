import streamlit as st
from PIL import Image

st.title("📊 Evaluasi Data & Model - HR Analytics")

# Tampilkan gambar satu per satu
st.header("1. Korelasi Data")
st.image(Image.open("data.png"), caption="Correlation Matrix of Numeric Features", use_column_width=True)

st.header("2. Korelasi Lanjutan & Feature Importance")
st.image(Image.open("data2.png"), caption="Top 15 Most Important Features", use_column_width=True)
st.image(Image.open("data3.png"), caption="Feature Distribution by Attrition", use_column_width=True)

st.header("3. Evaluasi Model")
st.image(Image.open("model.png"), caption="Model Performance Comparison & ROC Curves", use_column_width=True)

st.header("4. Confusion Matrix")
st.image(Image.open("model2.png"), caption="Confusion Matrix - Optimized Random Forest", use_column_width=True)

st.header("5. Feature Importance (Optimized Random Forest)")
st.image(Image.open("model3.png"), caption="Top 10 Feature Importance", use_column_width=True)