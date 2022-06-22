################
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""

# Funciones// tuple - def - return - while - if - print - input

def factores_primos(numero):
    divisor = 2
    i = 0
    factores = []
    numerito = numero
    while divisor * divisor < numero:
        if numerito % divisor == 0:
            numerito = numerito // divisor
            factores = factores + [divisor]
            divisor = 1
        divisor += 1
    if numerito != 1:
        factores = factores + [numerito]
    tupla_de_factores=tuple(factores)
    return tupla_de_factores
"""
la funcion factores_primos se encarga, como indica su nombre, de encontrar los factores primos de un 
numero que se le ingresa a traves de una variable que lleva el mismo nombre
a partir de aqui la funcion prueba distintos divisores de menor a mayor partiendo desde el 2, de forma de que cada vez
que encuentra un divisor divide a la variable numerito que lleva al numero ingresado
de esta forma la funsion se asegura de encontrar unicamente fatores primos y no entregar en el resultado factores que tengan divisores primos
este proceso se repite hasta probar un divisor, que multiplicado por si mismo de lugar al numero ya que este es el ultimo caso posible
de encontrar un divisor
a cada uno de los factoresd encontrados, lo almacena en la lista factores y en caso de que este sea distinto de uno, tambien almacena
a la variable numerito.
cuando el proceso termina devuelve una tupla conformada por la lista anteriormente mencionada.
"""

def principal():
    numero = int(input("Ingrese un numero entero positivo: "))
    print(factores_primos(numero))
    
    """
    la funcion principal unicamente se encarga de solicitar el numero a analizar y de llamar a la funcion
    factores_primos
    finalmente imprime el resultado de esta
    """

if __name__ == "__main__":
    principal()

    """
    esta parte del programa llama a la funcion principal
    """