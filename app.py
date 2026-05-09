import streamlit as st

# Configuración de la página
st.set_page_config(page_title="NutriAsistente", page_icon="🍏", layout="centered")

st.title("🍏 Asistente de Nutrición")
st.subheader("Cálculo Automático de IMC")

# Entradas de datos optimizadas para móvil
peso = st.number_input("Ingresa el peso (kg):", min_value=1.0, max_value=300.0, step=0.1, value=60.0)
altura_input = st.number_input("Ingresa la altura (en cm o metros):", min_value=0.1, max_value=250.0, step=1.0, value=165.0)

# Procesar altura automáticamente
altura = altura_input / 100 if altura_input > 3 else altura_input

if st.button("Calcular Diagnóstico", use_container_width=True):
    imc = peso / (altura ** 2)
    
    # Determinar categoría y alertas visuales
    if imc < 18.5:
        st.info(f"**IMC: {imc:.2f}** \n\nClasificación: Bajo peso")
    elif 18.5 <= imc < 25:
        st.success(f"**IMC: {imc:.2f}** \n\nClasificación: Peso normal")
    elif 25 <= imc < 30:
        st.warning(f"**IMC: {imc:.2f}** \n\nClasificación: Sobrepeso")
    elif 30 <= imc < 35:
        st.error(f"**IMC: {imc:.2f}** \n\nClasificación: Obesidad Grado I")
    elif 35 <= imc < 40:
        st.error(f"**IMC: {imc:.2f}** \n\nClasificación: Obesidad Grado II")
    else:
        st.error(f"**IMC: {imc:.2f}** \n\nClasificación: Obesidad Grado III")
