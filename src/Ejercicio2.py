################
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Numeros Positivos y Negativos
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""

# Funciones// def - return - if - print - input 

def signo(numero):
    sum = numero + numero

    if(sum > numero):
        resultado = "es positivo"
    elif sum < numero:
        resultado = "es negativo"
    else:
        resultado = "es cero"

    return resultado
    pass
"""
se crea la funcion signo, a la que se le entrega un valor numerico
esta  realiza una suma de este numero con si mismo y la almacena en una nueva variable llamada sum
compara el resultado con el numero inicial, si esta suma es mayor determina que el numero es positivo
caso contrario seria negativo
y en el caso restante en que ambas variables sean iguales se determina que el valor ingresado era cero 
"""
def principal():
    numero = int(input("Ingrese un numero: "))
    print(signo)
"""
se crea la funcion principal
esta se encarga de solicitar el ingreso del valor que se le asignara a variable numero
A traves de la funcion signo se determina si este valor ingresado es positivo,negativo o cero
"""
if __name__ == "__main__":
    signo()
"""
esta parte se encarga de ejecutar el programa principal
"""