import streamlit as st
import pandas as pd

# Configuración general (optimizada para móvil)
st.set_page_config(
    page_title="IA Ventas Cursos",
    layout="wide"
)

st.title("🧠 IA para Optimización Total de Ventas de Cursos")
st.caption("Prioriza leads, optimiza llamadas, segunda llamada y retargeting")

# =============================
# DATOS SIMULADOS (como CRM)
# =============================
data = {
    "Lead": ["Ana", "Carlos", "María", "Jorge", "Lucía"],
    "Edad": [52, 34, 45, 29, 57],
    "Curso": ["Executive", "Marketing", "MBA", "Programación", "Executive"],
    "Precio (€)": [3200, 1200, 2800, 900, 3500],
    "Probabilidad de Cierre (%)": [78, 42, 65, 25, 82],
    "Primer Contacto": [
        "No respondió",
        "Respondió",
        "No compró",
        "No respondió",
        "Respondió"
    ],
    "Comercial Ideal": ["Ana", "Juan", "Laura", "Juan", "Ana"]
}

df = pd.DataFrame(data)

# =============================
# MOTOR DE DECISIÓN
# =============================
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
    else:
        return "—"

def retargeting(row):
    if row["Probabilidad de Cierre (%)"] < 40:
        return "Email + Ads suaves"
    elif row["Probabilidad de Cierre (%)"] < 70:
        return "WhatsApp recordatorio"
    else:
        return "No necesario"

df["Canal Óptimo"] = df.apply(canal_optimo, axis=1)
df["Siguiente Acción"] = df.apply(siguiente_accion, axis=1)
df["Segunda Llamada"] = df.apply(segunda_llamada, axis=1)
df["Retargeting"] = df.apply(retargeting, axis=1)

# =============================
# DASHBOARD PRINCIPAL
# =============================
st.subheader("🔥 Leads priorizados y acciones recomendadas")

st.dataframe(
    df[
        [
            "Lead",
            "Probabilidad de Cierre (%)",
            "Precio (€)",
            "Comercial Ideal",
            "Canal Óptimo",
            "Siguiente Acción",
            "Segunda Llamada",
            "Retargeting"
        ]
    ],
    use_container_width=True
)

# =============================
# MÉTRICAS DE IMPACTO
# =============================
st.subheader("📈 Impacto estimado en ventas")

col1, col2, col3 = st.columns(3)
col1.metric("Leads analizados", len(df))
col2.metric("Mejora tasa de cierre", "+29 %")
col3.metric("Ingresos extra estimados", "+21.600 €")

# =============================
# EXPLICACIÓN SIMPLE
# =============================
with st.expander("🤔 ¿Por qué la IA recomienda estas acciones?"):
    st.write("""
    • Leads con alta probabilidad → llamada inmediata  
    • Leads templados → segunda llamada optimizada  
    • Leads fríos → retargeting automático  
    • Comercial asignado según perfil del lead  
    • Canal elegido según edad y comportamiento  
    """)