# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Similar al ejercicio de "calificaciones":

Debe caluclar el promedio de todas las notas que se encuentra
almacenadas en una lista llamada "notas" que ya
hemos definido al comienzo del archivo

Luego transformar la califiación en una letra
según la siguiente escala:
- Si el puntaje es mayor igual a 90 --> imprimir A
- Si el puntaje es mayor igual a 80 --> imprimir B
- Si el puntaje es mayor igual a 70 --> imprimir C
- Si el puntaje es mayor igual a 60 --> imprimir D
- Si el puntaje es menor a  60      --> imprimir F

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0

cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria
for nota in notas:
    if nota >= 0:
        sumatoria = sumatoria + nota
        cantidad_notas += 1
    else:
        cantidad_ausentes += 1
# Terminado el bucle calcule el promedio como
# promedio = sumatoria / cantidad_notas
# PROMEDIO TENIENDO EN CUENTA SOLO LAS NOTAS OBTENIDAS SIN CONTEMPLAR LOS AUSENTES 
promedio = sumatoria/cantidad_notas
print("La nota promedio obtenida es:",promedio)
# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

if promedio <= 100 and promedio >=90:
    print(promedio,"--> Obtuvo una A")
elif promedio >= 80 and promedio < 90:
    print(promedio,"--> Obtuvo una B")
elif promedio >= 70 and promedio <80:
    print(promedio,"--> Obtuvo una C")
elif promedio >= 60 and promedio < 70:
    print(promedio,"--> Obtuvo una D")
elif promedio > 0 and promedio < 60:
    print(promedio,"--> Obtuvo una F")
else:
    print("Promedio INCORRECTO, no hay calificación asociada")
# Imprima en pantalla al cantidad de ausentes
print("El alumno estuvo ausente en",cantidad_ausentes,"ocasiones")


