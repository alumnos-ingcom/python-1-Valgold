################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero es multiplo de otro,
utilizando sumas y restas.
"""

# Funciones// def - print - while - return - if - input


def es_multiplo(numero, multiplo):
    sum = 0
    while sum < multiplo:
        sum = sum + numero
    
    return sum == multiplo
"""
se crea la funcion es_multiplo a la quen se le ingresan dos variables: numero y multiplo
esta se encargara de determinar si el segundo es multiplo del primero
para esto sumara a una variable sum el primer numero ingresado hasta alcanzar un valor igual o mayor al de multiplo
una vez hecho esto se compara la igualdad de sum y multiplo
si esta se comprueba la funcion retorna True, ya que multiplo es multiplo de numero
caso contrario retornará False 
"""
def principal():
    numero = int(input("ingrese un numero: "))
    multiplo = int(input("ingrese un numero para verificar si es multiplo del anterior: "))
    print(es_multiplo(numero, multiplo))
"""
la funcion principal solicitará el ingreso de las variables numero y multoplo al usuario.
luego las cargara en la funcion es_multiplo e imprimirá el resultado de la misma
"""

if __name__ == "__main__":
    principal()
"""
esta parte del programa Se encarga de ejecutar la funcion principal
"""