################
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo
entero retorne una tupla con dichos valores ordenados de 
menor a mayor. Y Viceversa
"""

# Funciones// def - if - while - print - input - return

def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos:
        if dos > tres:
            resultado = (uno, dos, tres)
        elif uno > tres:
            resultado = (uno, tres, dos)
        else:
            resultado = (tres, uno, dos)
    elif dos > uno:
        if uno > tres:
            resultado = (dos,uno,tres)
        elif dos > tres:
            resultado = (dos,tres,uno)
        else:
            resultado = (tres,dos,uno)
    else:
        resultado = (uno,dos,tres)
    return resultado

    """
    se crea la funcion de_mayor_a_menor, esta debe ser cargada con 3 datos numericos,
    los cuales seran analizados por una cadena de if`s para determinar la comparativa de valores de los mismos
    dependiendo de resultado, seran almacenados en orden dentro de una variable de tipo tuple llamada resultado, la cual se entrega
    como retorno de la funcion.   
    """

def ordenar_menor_a_mayor(uno, dos, tres):
    if uno < dos:
        if dos < tres:
            resultado = (uno, dos, tres)
        elif uno < tres:
            resultado = (uno, tres, dos)
        else:
            resultado = (tres, uno, dos)
    elif dos < uno:
        if uno < tres:
            resultado = (dos, uno, tres)
        elif dos < tres:
            resultado = (dos, tres, uno)
        else:
            resultado = (tres, dos, uno)
    else:
        resultado = (uno, dos, tres)
    return resultado
"""
la funcion de_menor_a_mayor funciona de forma muy similar a de_mayor_a_menor con la unica diferencia 
de que las comparativas en los if buscan determinar el menor de los valores en lugar del mayor, por lo que es
una suerte de funcion inversa de la anterior. su metodología de trabajo, por ende, es la misma
"""

def principal():
    numero_uno = int(input("ingrese un numero: "))
    numero_dos = int(input("ingrese otro numero: "))
    numero_tres = int(input("ingrese un ultimo numero: "))
    print(ordenar_mayor_a_menor(numero_uno,numero_dos,numero_tres))
    print(ordenar_menor_a_mayor(numero_uno,numero_dos,numero_tres))
    
    """
    La funcion principal solicita los tres numeros a ordenar, a continuacion las imprime ordenadas,
    primero, de mayor a menor. y luego de menor a mayor utilizando las respectivas funciones ya descritas.
    """


if __name__ == "__main__":
    principal()