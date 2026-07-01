import os
import xml.etree.ElementTree as ET

# Clases del proyecto
CLASSES = {
    "With Helmet": 0,
    "Without Helmet": 1
}

ANNOTATIONS_DIR = "annotations"
LABELS_DIR = "labels"

os.makedirs(LABELS_DIR, exist_ok=True)

for xml_file in os.listdir(ANNOTATIONS_DIR):

    if not xml_file.endswith(".xml"):
        continue

    xml_path = os.path.join(ANNOTATIONS_DIR, xml_file)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    yolo_lines = []

    for obj in root.findall("object"):

        class_name = obj.find("name").text.strip()

        if class_name not in CLASSES:
            continue

        class_id = CLASSES[class_name]

        bbox = obj.find("bndbox")

        xmin = float(bbox.find("xmin").text)
        ymin = float(bbox.find("ymin").text)
        xmax = float(bbox.find("xmax").text)
        ymax = float(bbox.find("ymax").text)

        # Conversión a formato YOLO
        x_center = ((xmin + xmax) / 2) / width
        y_center = ((ymin + ymax) / 2) / height

        box_width = (xmax - xmin) / width
        box_height = (ymax - ymin) / height

        yolo_lines.append(
            f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}"
        )

    txt_name = os.path.splitext(xml_file)[0] + ".txt"
    txt_path = os.path.join(LABELS_DIR, txt_name)

    with open(txt_path, "w") as f:
        f.write("\n".join(yolo_lines))

print("Conversión completada.")
print(f"Archivos generados en: {LABELS_DIR}")