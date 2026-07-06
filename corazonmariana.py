from vpython import *
import numpy as np

# Configuración
scene.title = "Corazon 3D para Mariana"
scene.background = color.black

nombre = "MARIANA"
puntos = 60  # Más puntos para que se vea mejor
objetos = []

for i in range(puntos):
    t = (i / puntos) * 2 * np.pi
    # Ecuación del corazón
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    char = nombre[i % len(nombre)]
    lbl = label(
        pos=vector(x * 0.5, y * 0.5, 0),
        text=char,
        color=color.red,
        box=False,
        line=False,
    )
    objetos.append({"obj": lbl, "x": x * 0.5, "y": y * 0.5})

ang = 0
while True:
    rate(60)
    ang += 0.03
    for item in objetos:
        # Rotación 3D real
        new_x = item["x"] * cos(ang)
        new_z = item["x"] * sin(ang)
        item["obj"].pos = vector(new_x, item["y"], new_z)
