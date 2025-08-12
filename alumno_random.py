
import random 

nombres = []

def encontrar_nombre (alumno):
    nombre=""
    for caracter in alumno:
        if caracter == "2":
            break
        nombre += caracter
    return nombre

alumnos = []
with open ("./alumnos.txt", "r") as archivo:
    alumnos = archivo.readlines()
    print(alumnos)

nombres = [encontrar_nombre(alumno) for alumno in alumnos]
print (nombres)  

alumno_escogido = random.choice (nombres)
print ("El alumno que tiene que pasar al frente es:" + alumno_escogido)















