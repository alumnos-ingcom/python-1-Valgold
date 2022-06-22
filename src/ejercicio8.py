################
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero indicado es Primo.
"""

# Funciones// def - while - if - return - print - input 

def es_primo(numero):
    divisor = numero
    divisores = 0
    while divisor > 0:
        if numero % divisor == 0:
            divisores += 1
        divisor -= 1
    return divisores < 3
"""
se crea la funcion es_primo. esta a partir de una variable ingresada busca,mediante
un while, uno por uno los divisores del numero ingresado, partiendo de este hasta llegar al uno.
paralelamente va contando la cantidad de divisores en una variable
finalmente la funcion retorna False si el numero cuenta con mas de 2 divisores enteros
y True, si la funcion no lo hace, es decir si el numero es primo

"""

def principal():
    numero = int(input("ingrese un numero: "))
    print(es_primo(numero))
    """
    esta funcion solicita el valor a analizar al usuario, 
    llama a la funcion es_primo e imprime el resultado de la misma
    """

if __name__ == "__main__":
    principal()

"""
esta parte se encarga de ejecutar el programa principal
"""