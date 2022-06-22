################
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""

# Funciones// def - if - return - input - print
def compara(numero, otro_numero):
    if numero + numero > numero + otro_numero:
        resultado = 1
    elif numero+numero<numero+otro_numero:
        resultado = -1
    else: 
        resultado = 0

    return resultado
"""
se define la funcion def a la que se le entregaran dos valores numericos, 
esta se encargará de determinar  cual de los dos es mayor
primero compara si la suma del primer nuemro consigo mismo es mayor a la suma de este numero con el segundo ingresado.
Caso afirmativo la funcion devolvera un 1 a traves de resultado
caso contrario devolverá -1
si ambas sumas devuelven el mismo valor, se determina que ambos numeros son iguales. en este caso retonará 0
"""
def principal():
    numero = int(input("ingrese un numero"))
    otro_numero = int(input("ingrese otro numero"))
    print(compara(numero,otro_numero))
"""
La funcion principal se encarga de pedir los valores a entregar a la funcion compara
Finalmente imprime el resultado de esta funcion sinedo: 
                                                        -1 en el caso numero<otro_numero
                                                        1 en el caso numero>otro_numero
                                                        0 en caso de igualdad
"""
if __name__ == "__main__":
    principal()
"""
llama a la funcion que ejecuta el programa principal
"""