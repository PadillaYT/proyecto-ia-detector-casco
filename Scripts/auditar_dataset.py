import os
import xml.etree.ElementTree as ET
from collections import Counter

# Ruta de la carpeta annotations
ANNOTATIONS_PATH = "annotations"

clases = Counter()
archivos_xml = 0

for archivo in os.listdir(ANNOTATIONS_PATH):

    if not archivo.endswith(".xml"):
        continue

    archivos_xml += 1

    ruta_xml = os.path.join(ANNOTATIONS_PATH, archivo)

    try:
        tree = ET.parse(ruta_xml)
        root = tree.getroot()

        for obj in root.findall("object"):
            nombre_clase = obj.find("name").text.strip()
            clases[nombre_clase] += 1

    except Exception as e:
        print(f"Error en {archivo}: {e}")

print("\n===== RESUMEN DEL DATASET =====")
print(f"Archivos XML encontrados: {archivos_xml}")

for clase, cantidad in clases.items():
    print(f"{clase}: {cantidad}")

print(f"\nTotal de objetos: {sum(clases.values())}")