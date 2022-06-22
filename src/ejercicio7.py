################
# Valentin de Brito - @Valgold
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos. 
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
"""

# Funciones// def - return - if - print - input 

def sexadecimal_a_decimal(horas, minutos, segundos):
    resultado = horas * 3600 + minutos * 60 + segundos
    return resultado

    """
    La funcion sexadecimal_a_decimal recive tres valores, las horas, minutos y segundos
    y mediante una formula simple convierte a los tres en un unico valor en la unidad mas pequeña
    y lo retorna mediante la variable resultado
    """
def decimal_a_sexadecimal(numero):
    minutos = numero // 60
    numero = numero - minutos * 60
    horas = minutos // 60
    minutos = minutos - horas * 60
    resultado = (horas, minutos, numero)
    return resultado

    """
    La funcion decimal_a_sexadecimal es una funcion con el objetivo inverso a la anterior
    esta recibe una unica variable, que se interpreta como un valor en segundos, al cual se convierte a segundos
    a traves de una division entera. Tras restarle la conversion a minutos al valor inicial se repite el proceso
    esta vez partiendo de los minutos aplicando los mismos pasos que con los segundos, para obtener asi las horas o grados
    todas estas variables se almacenan en una tupla llamada resultado
    y se convienrten en el retorno de la funcion 
    """

def principal():
    horas = int(input("ingrese las horas: "))
    minutos = int(input("ingrese las minutos: "))
    segundos = int(input("ingrese los segundos: "))
    segundos_totales = sexadecimal_a_decimal(horas,minutos,segundos)
    print(segundos_totales)
    print(decimal_a_sexadecimal(segundos_totales))
    """
    la funcion main le solicita al usuario el ingreso de las horas, minutos y segundos para insertarlos en la funcion
    sexadecimal_a_decimal,e imprime el resultado.
    a este lo ingresa en la funcion decimal_a_sexadecimal que realiza el proceso inverso, de esta forma se obtienen
    nuevamente los valores ingresados en forma de tupla
    """
    pass

if __name__ == "__main__":
    principal()

    """
    esta parte del programa se encarga de ejecutar la funcion principal
    """