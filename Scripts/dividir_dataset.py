import os
import random
import shutil

random.seed(42)

IMAGES_DIR = "images"
LABELS_DIR = "labels"

DATASET_DIR = "dataset"

TRAIN_RATIO = 0.7
VALID_RATIO = 0.2
TEST_RATIO = 0.1

for split in ["train", "valid", "test"]:
    os.makedirs(os.path.join(DATASET_DIR, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(DATASET_DIR, split, "labels"), exist_ok=True)

imagenes = [
    f for f in os.listdir(IMAGES_DIR)
    if f.endswith(".png")
]

random.shuffle(imagenes)

total = len(imagenes)

train_end = int(total * TRAIN_RATIO)
valid_end = train_end + int(total * VALID_RATIO)

train_files = imagenes[:train_end]
valid_files = imagenes[train_end:valid_end]
test_files = imagenes[valid_end:]

def copiar_archivos(lista, split):

    for imagen in lista:

        nombre = os.path.splitext(imagen)[0]

        label = nombre + ".txt"

        shutil.copy(
            os.path.join(IMAGES_DIR, imagen),
            os.path.join(DATASET_DIR, split, "images", imagen)
        )

        shutil.copy(
            os.path.join(LABELS_DIR, label),
            os.path.join(DATASET_DIR, split, "labels", label)
        )

copiar_archivos(train_files, "train")
copiar_archivos(valid_files, "valid")
copiar_archivos(test_files, "test")

print("Dataset dividido correctamente")
print(f"Train: {len(train_files)}")
print(f"Valid: {len(valid_files)}")
print(f"Test: {len(test_files)}")