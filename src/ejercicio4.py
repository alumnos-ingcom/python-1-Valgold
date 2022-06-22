################
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros
sin hacer la operación de manera directa. Esto quiere decir que 
para hacer la suma entre 4 y 3, las operaciones resultantes
deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

# Funciones// def - if - while - print - input - return
def suma_lenta(numero, otro_numero):
    sumas = 0
    if otro_numero < 0:
        while sumas > otro_numero:
            numero = numero - 1
            sumas = sumas - 1
    else:
        while sumas < otro_numero:
            numero = numero + 1
            sumas = sumas + 1        
    return numero
    """
    Se crea la funcion suma_lenta, a la que se le daran dos valores numericos
    esta se encarga de sumarle 1 al primer numero hasta alcanzar la suma entre este y el segundo
    en caso de que el segundo numero sea negativo se seguira el mismo proceso pero restando de uno en uno
    """

def principal():
    num1 = int(input("ingrese un numero: "))
    num2 = int(input("ingrese otro numero: "))
    print(suma_lenta(num1, num2))
    
    """
    La funcion principal solicita al usuario los dos numeros que alimentaran a la funcion de suma lenta
    finalmente imprime el resultado que devuelve dicha funcion
    """

if __name__ == "__main__":
    principal()
    """
    llama a la funcion que ejecuta el programa pricipal
    """