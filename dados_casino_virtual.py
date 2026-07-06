import os
import random

dado1 = 0
dado2 = 0
resultado = 0

os.system("cls")
print("""
      Bienvenido al casino virtual!!
      Para ganar los dados tienen que dar la suma
      de 11, si no, caeras en la ruina!!! JAJAAJA!!""")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Para tirar los dados presiona una tecla")
os.system("pause")

resultado = dado1 + dado2

os.system("cls")
if resultado == 11:
    print(f"""
          TENEMOS UN GANADOR!!!
          TUS DADOS FUERON: {dado1} y {dado2}""")
else:
    print(f"""
          Lo siento, caiste en la ruina
          la suma fue {resultado} 
          y tus dados fueron {dado1} y {dado2}""")
