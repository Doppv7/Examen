import os
import random

ganador = 0
nombre = ""

os.system("cls")
print("""
      ==================================
      Bienvenidos al sorteo del nootbook
      los posibles ganadores son
      1.Benjamin
      2.Yohan
      3.Jeison
      4.Pablo
      5.Francisco
      ==================================
      """)
os.system("pause")

ganador = random.randint(1, 5)

if ganador == 1:
    nombre = "Benjamin"
elif ganador == 2:
    nombre = "Yohan"
elif ganador == 3:
    nombre = "Jeison"
elif ganador == 4:
    nombre = "Pablo"
elif ganador == 5:
    nombre = "Francisco"


print(f"""
      ===================================
      EL GANADOR DEL NOOTBOOK ES!!!!
               {nombre}                  """)
os.system("pause")
