def hola():
    print('hola')

def adios():
    print('adios')

def pregunta():
    print('Cómo estas?')


mapa = {
    1:hola,
    2:adios,
    3:pregunta
}

opcion = int(input('Dime la opcion:\n1: Saludar\n2: Despedirse\n3: Pregunta\n'))
mapa[opcion]()