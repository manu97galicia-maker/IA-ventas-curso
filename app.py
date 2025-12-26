import streamlit as st
import pandas as pd

st.set_page_config(page_title="IA Ventas", layout="wide")

st.title("📊 IA para Optimizar Ventas de Cursos")

# Datos simulados
data = {
    "Lead": ["Ana", "Carlos", "María", "Jorge"],
    "Probabilidad de Cierre (%)": [82, 45, 67, 30],
    "Valor (€)": [2400, 1200, 1800, 900],
    "Comercial Asignado": ["Laura", "Juan", "Ana", "Juan"],
    "Canal Óptimo": ["Llamada", "WhatsApp", "Videollamada", "Email"],
    "Hora Recomendada": ["18:30", "19:00", "17:00", "10:00"],
    "Siguiente Acción": [
        "Llamar hoy",
        "Retargeting WhatsApp",
        "Segunda llamada mañana",
        "Email automático"
    ]
}

df = pd.DataFrame(data)

st.subheader("🔥 Leads priorizados hoy")
st.dataframe(df, use_container_width=True)

st.subheader("📈 Impacto estimado")
col1, col2, col3 = st.columns(3)
col1.metric("Leads analizados", "124")
col2.metric("Cierres estimados", "+32 %")
col3.metric("Ingresos extra", "+18.400 €")

st.subheader("📞 Canales más efectivos")
st.bar_chart(df["Canal Óptimo"].value_counts())