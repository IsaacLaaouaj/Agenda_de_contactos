def hola():
    print('hola')

def adios():
    print('adios')


mapa = {
    1:hola,
    2:adios
}

opcion = int(input('Dime la opcion:\n1: Saludar\n2: Despedirse\n'))
mapa[opcion]()