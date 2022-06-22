################
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una palabra o frase
ingresada se trata de un palindromo. Palíndromo, es si se lee
igual de derecha a izquierda que de izquierda a derecha.
"""

# Funciones// tuple - def - return - while - if - print - input

def es_palindromo(texto):
    i = 0
    coincidencias = 0
    while i <= (len(texto) // 2):
        if texto[i] == texto[ - (1+i)]:
            coincidencias += 1
        i += 1
    return coincidencias > (len(texto) // 2)
"""
la funcion es_palindromo recive una cadena de texto y sen encarga de determinar, como indica su nombre, si esta 
es un palindromo.
Para la analiza caracter por caracter mediante un bucle while
comparando el primer valor con el ultimo, el segundo con el anteultimo y asi sucesivamente
hasta llegar a la mitad de la palabra
la cantidad de coincidencias se van almacenando en una variable que lleva ese nombre
y es comparada con la mitad de la extencion del texto
si estas coicidencias superan a la extencion la funcion retorna True. Caso contrario
la palabra no es un palindromo, por lo que retorna Talse 
"""



def principal():
    texto = str(input("ingrese una cadena de texto: "))
    print(es_palindromo(texto))
    """
    esta funcion solicita el ingreso de la palabra que se inserta en la funcion es_palidromo
    finalmente se imprime el resultado de la misma
    """

if __name__ == "__main__":
    principal()
    """
    en esta parte del codigo se llama a la funcion principal
    """