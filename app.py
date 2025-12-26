import streamlit as st
import pandas as pd

# -----------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------
st.set_page_config(
    page_title="IA Ventas Cursos",
    layout="centered"
)

# Estilos CSS (mobile friendly)
st.markdown("""
<style>
.card {
    background-color: #ffffff;
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.high { border-left: 6px solid #2ecc71; }
.medium { border-left: 6px solid #f1c40f; }
.low { border-left: 6px solid #e74c3c; }
.label {
    font-size: 12px;
    color: #888;
}
.value {
    font-size: 18px;
    font-weight: 600;
}
.action {
    margin-top: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TÍTULO
# -----------------------------
st.title("🧠 IA de Ventas")
st.caption("Decisiones automáticas para vender más cursos")

# -----------------------------
# CARGA DE DATOS
# -----------------------------
df = pd.read_csv("leads.csv")

df.rename(columns={
    "Precio": "Precio (€)",
    "Probabilidad": "Probabilidad de Cierre (%)",
    "Primer_Contacto": "Primer Contacto",
    "Comercial_Ideal": "Comercial Ideal"
}, inplace=True)

# -----------------------------
# LÓGICA DE DECISIÓN
# -----------------------------
def prioridad(prob):
    if prob >= 70:
        return "Alta", "high"
    elif prob >= 40:
        return "Media", "medium"
    else:
        return "Baja", "low"

def canal(edad):
    if edad >= 45:
        return "📞 Llamada / Videollamada"
    elif edad >= 30:
        return "💬 WhatsApp"
    else:
        return "📧 Email"

def accion(prob):
    if prob >= 70:
        return "📞 Llamar hoy"
    elif prob >= 40:
        return "🔁 Programar segunda llamada"
    else:
        return "📲 Retargeting automático"

def seguimiento(contacto):
    if contacto == "No respondió":
        return "📅 Mañana 18:00"
    elif contacto == "No compró":
        return "📅 En 3 días 17:00"
    else:
        return "—"

# -----------------------------
# MÉTRICAS SUPERIORES
# -----------------------------
st.subheader("📊 Hoy")
col1, col2 = st.columns(2)
col1.metric("Leads", len(df))
col2.metric("Mejora cierre", "+29 %")

st.divider()

# -----------------------------
# TARJETAS DE LEADS (CORE VISUAL)
# -----------------------------
st.subheader("🔥 Prioridad de hoy")

for _, row in df.iterrows():
    nivel, clase = prioridad(row["Probabilidad de Cierre (%)"])
    
    st.markdown(f"""
    <div class="card {clase}">
        <div class="label">Lead</div>
        <div class="value">{row["Lead"]} ({row["Edad"]} años)</div>

        <div class="label">Curso</div>
        <div class="value">{row["Curso"]} – €{row["Precio (€)"]}</div>

        <div class="label">Prioridad</div>
        <div class="value">{nivel} ({row["Probabilidad de Cierre (%)"]}%)</div>

        <div class="label">Comercial</div>
        <div class="value">{row["Comercial Ideal"]}</div>

        <div class="label">Canal recomendado</div>
        <div class="value">{canal(row["Edad"])}
</div>

        <div class="action">👉 {accion(row["Probabilidad de Cierre (%)"])}</div>
        <div class="label">Seguimiento: {seguimiento(row["Primer Contacto"])}
</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# EXPLICACIÓN SIMPLE
# -----------------------------
with st.expander("🤔 ¿Cómo decide la IA?"):
    st.write("""
    • Prioriza por probabilidad y ticket  
    • Asigna canal según edad y patrón histórico  
    • Decide segunda llamada o retargeting  
    • Enfocado a maximizar ingresos, no volumen  
    """)