# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
terminar= ''
while terminar.upper() != "FIN":
    num_1 = int(input("Ingrese un número: "))
    num_2 = int(input("Ingrese otro número: "))
    operacion= str(input("Operación a realizar? (+,-,*,/,**):"))
    while operacion not in ['+','-','*','/','**']:
        print("Operación no reconocida")
        operacion= str(input("Operación a realizar? (+,-,*,/,**):"))
    if operacion == '+':
        print("Operación seleccionada: SUMA")
        suma = num_1 + num_2
        print("{} + {}= {}".format(num_1,num_2,suma))
    elif operacion == '-':
        print("Operación seleccionada: RESTA")
        resta = num_1 - num_2
        print("{} - {}= {}".format(num_1,num_2,resta))
    elif operacion == '*':
        print("Operación seleccionada: MULTIPLICACION")
        producto = num_1 * num_2
        print("{} * {}= {}".format(num_1,num_2,producto))
    elif operacion == '/':
        print("Operación seleccionada: DIVISION")
        if num_2 != 0:
            division = num_1 / num_2
            print("{} / {}= {}".format(num_1,num_2,division))
        else:
            print("No se puede dividir por CERO")
    else:
        print("Operación seleccionada: POTENCIA")
        if num_1 == 0 and num_2 == 0:
            print("0 ^ 0 NO SE PUEDE CALCULAR")
        else:
            potencia = num_1 ** num_2
            print("{} ^ {}= {}".format(num_1,num_2,potencia))
    terminar= str(input("Desea realizar otro cálculo? (Enter para otro cálculo -- Escriba FIN para FINALIZAR):"))

print("Fin del Programa! Saludos!")