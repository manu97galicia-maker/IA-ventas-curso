import streamlit as st
import pandas as pd

st.set_page_config(page_title="IA Ventas Cursos", layout="wide")

st.title("🧠 IA para Optimización Total de Ventas de Cursos")
st.caption("Prioriza leads, asigna comerciales, optimiza llamadas y retargeting")

# -----------------------------
# DATOS SIMULADOS (como si vinieran del CRM)
# -----------------------------
data = {
    "Lead": ["Ana", "Carlos", "María", "Jorge", "Lucía"],
    "Edad": [52, 34, 45, 29, 57],
    "Curso": ["Executive", "Marketing", "MBA", "Programación", "Executive"],
    "Precio (€)": [3200, 1200, 2800, 900, 3500],
    "Probabilidad de Cierre (%)": [78, 42, 65, 25, 82],
    "Primer Contacto": ["No respondió", "Respondió", "No compró", "No respondió", "Respondió"],
    "Comercial Ideal": ["Ana", "Juan", "Laura", "Juan", "Ana"],
}

df = pd.DataFrame(data)

# -----------------------------
# MOTOR DE DECISIÓN
# -----------------------------
def siguiente_accion(row):
    if row["Probabilidad de Cierre (%)"] >= 70:
        return "📞 Llamar hoy"
    elif row["Probabilidad de Cierre (%)"] >= 40:
        return "🔁 Segunda llamada programada"
    else:
        return "📲 Retargeting automático"

def canal_optimo(row):
    if row["Edad"] >= 45:
        return "Llamada / Videollamada"
    elif row["Edad"] >= 30:
        return "WhatsApp"
    else:
        return "Email"

def segunda_llamada(row):
    if row["Primer Contacto"] == "No respondió":
        return "📅 Mañana 18:00"
    elif row["Primer Contacto"] == "No compró":
        return "📅 En 3 días 17:00"

def retargeting(row):
    return "📨 Email con oferta personalizada"