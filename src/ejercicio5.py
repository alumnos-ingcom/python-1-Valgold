################
# Valentin de Brito- @valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""

# Funciones// def - return - while - print - input - if

def division_lenta(dividendo, divisor):
    resultado = 0
    operador = dividendo
    while operador >= divisor:
        operador = operador - divisor
        resultado += 1
    resto = dividendo - (divisor * resultado)
    respuesta = (resultado,resto)
    return respuesta
"""
se crea la funcion division_lenta, la cual recibira dos numeros: dividendo y divisor.
Y se encargará de realizar la division entre ambos, a traves de restas sucesivas
para esto crea una variable resultado que como indica su nombre almacenará el cociente de la division
y mediante la funcion operador que se iguala al dividendo le restará, a operador, el valor de divisor de 
forma repetida hasta que estos sean iguales o bien operador sea mas pequeño.
Por cada una de estas restas la variable resultado irá incrementando su valor en 1
finalmente se obtiene el resto, medianteb la diferencia entre el dividendo y el producto del resultado con el divisor
finalmente ingresa los calores a una tupla y los entrega como retorno de la funcion 
"""
def principal():
    
    dividendo = int(input("ingrese el dividendo: "))
    divisor = int(input("ingrese el divisor: "))
    print(division_lenta(dividendo,divisor))
    
    """
    la funcion principal solicita el ingreso del dividendo y divisor (en ese orden) y los ingresa en la funcion 
    division_lenta.
    finalmente imprime la respuesta de esta.
    """
    pass

if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""