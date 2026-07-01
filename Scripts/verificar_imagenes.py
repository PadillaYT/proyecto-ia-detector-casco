import os

imagenes = set()
xmls = set()

for archivo in os.listdir("images"):
    nombre = os.path.splitext(archivo)[0]
    imagenes.add(nombre)

for archivo in os.listdir("annotations"):
    nombre = os.path.splitext(archivo)[0]
    xmls.add(nombre)

print("Imágenes:", len(imagenes))
print("XML:", len(xmls))

faltan_xml = imagenes - xmls
faltan_imagenes = xmls - imagenes

print("Imágenes sin XML:", len(faltan_xml))
print("XML sin imagen:", len(faltan_imagenes))