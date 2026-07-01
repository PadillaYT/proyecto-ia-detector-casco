import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile

# Configuración de página
st.set_page_config(
    page_title="Detector Inteligente de Casco",
    page_icon="🏍️",
    layout="wide"
)

# Título
st.title("🏍️ Sistema Inteligente de Detección de Casco")

st.markdown("""
Este sistema utiliza **Visión Artificial** y **YOLOv8** para detectar
motociclistas que utilizan casco y aquellos que no cumplen con esta medida
de seguridad vial.
""")

# Información lateral
with st.sidebar:
    st.header("ℹ️ Información")
    st.write("**Modelo:** YOLOv8")
    st.write("**Clases:**")
    st.write("🟢 With Helmet")
    st.write("🔴 Without Helmet")
    st.write("**Autor:** Cristian Padilla")

# Cargar modelo
@st.cache_resource
def cargar_modelo():
    return YOLO("modelo/best.pt")

model = cargar_modelo()

uploaded_file = st.file_uploader(
    "📷 Selecciona una imagen",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    with st.spinner("Analizando imagen..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            image.save(tmp.name)

            results = model(tmp.name)

    resultado = results[0].plot()

    # Contadores
    con_casco = 0
    sin_casco = 0

    for box in results[0].boxes:

        clase = int(box.cls[0])

        if clase == 0:
            con_casco += 1

        elif clase == 1:
            sin_casco += 1

    # Métricas
    st.subheader("📊 Resumen de detecciones")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("🟢 Con casco", con_casco)

    with col2:
        st.metric("🔴 Sin casco", sin_casco)

    # Imágenes lado a lado
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Imagen original")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Resultado de la detección")
        st.image(resultado, use_container_width=True)

    # Mensaje final
    if sin_casco > 0:
        st.warning(
            f"⚠️ Se detectaron {sin_casco} motociclistas sin casco."
        )
    else:
        st.success(
            "✅ Todos los motociclistas detectados utilizan casco."
        )
