import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Detector de Casco",
    page_icon="🏍️"
)

st.title("🏍️ Detector de Uso de Casco en Motociclistas")

st.write(
    "Sube una imagen y el modelo detectará motociclistas "
    "con casco y sin casco."
)

# Cargar modelo
@st.cache_resource
def cargar_modelo():
    return YOLO("modelo/best.pt")

model = cargar_modelo()

uploaded_file = st.file_uploader(
    "Selecciona una imagen",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Imagen original")
    st.image(image, use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        image.save(tmp.name)

        results = model(tmp.name)

    resultado = results[0].plot()

    st.subheader("Resultado de la detección")
    st.image(resultado, use_container_width=True)

    st.success("Detección completada")
    