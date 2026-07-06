import os

os.system("cls")

nombre = str(input("Indique su nombre:")).strip().upper()


peso = int(input("Indique su peso:"))
while not (peso > 0):
    print("Error, peso debe ser mayor a 0")
    peso = int(input("Indique su peso:"))

os.system("pause")
estatura = float(input("Indique su estatura:"))
while not (estatura > 0):
    print("Error, su estatura tiene que ser mayor a 0")
    estatura = str(input("Indique su estatura:"))

os.system("pause")
imc = peso / estatura

print(f"""
      =======Ticket========
      Hola {nombre}
      Estatura:{estatura}
      peso:{peso}
      IMC:{imc:.1d}""")
