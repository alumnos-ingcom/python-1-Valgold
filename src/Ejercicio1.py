###############
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir las funciones para convertir la temperatura en grados centigrados
en fahrenheit como un número decimal, utilice esta formula para calcular 
los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

# Funciones// def- return - print - input

def convertir_a_fahrenheit(centigrados):
    fahrenheit = centigrados*1.8 + 32
    return fahrenheit
    """
    Se crea la funcion convertir_a_fahrenheit y se le alimenta con la variable qe contiene los grados centigrados
    esta funcion aplica la formula de conversion de centigrados a fahrenheit y la carga en la variable que lleva este mombre
    finalmente a traves de la esta variable devuelve la temperatura convertida
    """

def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit - 32)/1.8
    return centigrados
    """
    se crea la funcion convertir_a_centigrados a la que se le carga la variable fahrenheit con la temperatura en esta unidad
    al igual que la funcion anterior aplica la formula de conversion (aunque en este caso es la inversa) y se carga en centigrados
    a traves de esta variable se devuelve la temperatura con la conversion solicitada 
    """

    pass
def principal():
    centigrados = int(input("Ingrese una temperatura en grados centigrados: "))
    fahrenheit = int(input("Ingrese una temperatura en grados fahrenheit: "))
    centigrados = convertir_a_fahrenheit(centigrados)
    fahrenheit = convertir_a_centigrados(fahrenheit)
    print(centigrados)
    print(fahrenheit)
"""
en la funcion principal se especifican los pasos de interaccion con el usuario
en esta se solicita una temperatura en centigrados y otra en fahrenheit
se llama a las respectivas funciones de conversion
y finalmente se imprimen los valores convertidos donde centigrados ahora contiene la temperatura en fahrenheit
y farenheit la conversion a centigrados
aunque esto ultimo podria ser un poco contraintuitivo se hace asi para evitar emplear variables nuevas de transicion de datos
"""

if __name__ == "__main__":
    principal()
"""
se llama a la funcion que contiene el programa principal
"""