import firebase_admin, sys
from firebase_admin import credentials,db

def añadePersona(ref): #Añade una persona a la DB, coge los datos:
    nombre = input("Introduzca un nombre: ")
    apellido = input("Introduzca un apellido: ")
    telefono = input("Introduzca un telefono: ")
    edad = input("Introduzca un edad: ")
    ref.push({"nombre":nombre,"apellido":apellido,"telefono":telefono,"edad":edad}) #Hace un push para registrar el elemento en forma de JSON


def borraPersona(ref): #Borra una persona a la DB:
    apellido = input("Introduzca el apellido del contacto a borrar: ") #Recoge el apellido
    resultado = ref.order_by_child('apellido').equal_to(apellido).get() #Genera una lista ordenada por apellido igual al introducido

    encontrado = False
    for key in resultado: #Por cada contacto de la lista de resultados
        
        if(not encontrado): #Si el elemento a borrar todavia no se ha encontrado
            elemento = ref.child(key)
            elementoMostrado = elemento.get() #Recoges el elemento y lo muestras
            print("\n", "Nombre: ", elementoMostrado["nombre"], "\tApellido: ", elementoMostrado["apellido"], "\tTelefono: ", elementoMostrado["telefono"], "\tEdad: ", elementoMostrado["edad"])
            confirmacion = input("\nEstas seguro de querer borrar? (s/n): ")

            if(confirmacion.lower()=='s'): #Si es el elemento que desea borrar 
                elemento.delete() #Se borra
                encontrado = True #Se pone el encontrado a True para que no te muestre mas elementos


def modificaPersona(ref): #Modifica una persona a la DB:
    apellido = input("Introduzca el apellido del contacto a modificar: ") #Recoge el apellido
    resultado = ref.order_by_child('apellido').equal_to(apellido).get() #Genera una lista ordenada por apellido igual al introducido

    encontrado = False
    for key in resultado:#Por cada contacto de la lista de resultados

        if(not encontrado): #Si el elemento a modificar todavia no se ha encontrado
            elemento = ref.child(key)
            elementoMostrado = elemento.get() #Recoges el elemento y lo muestras
            print("\n", "Nombre: ", elementoMostrado["nombre"], "\tApellido: ", elementoMostrado["apellido"], "\tTelefono: ", elementoMostrado["telefono"], "\tEdad: ", elementoMostrado["edad"])
            confirmacion = input("\nEstas seguro de querer modificar? (s/n): ")

            if(confirmacion.lower()=='s'): #Si es el elemento que desea modificar recoge los datos para la modificacion:
                nombre = input("Introduzca un nombre: ")
                apellido = input("Introduzca un apellido: ")
                telefono = input("Introduzca un telefono: ")
                edad = input("Introduzca un edad: ")
                elemento.update({"nombre":nombre,"apellido":apellido,"telefono":telefono,"edad":edad}) #Lo modifica
                encontrado = True #Se pone el encontrado a True para que no te muestre mas elementos


def buscaPersona(ref): #Muestra las personas con el apellido introducido de la DB:
    apellido = input("Introduzca el apellido del contacto a buscar: ") #Recoge el apellido
    resultado = ref.order_by_child('apellido').equal_to(apellido).get() #Genera una lista ordenada por apellido igual al introducido

    for key in resultado: #Por cada contacto de la lista de resultados
        elemento = ref.child(key)
        elementoMostrado = elemento.get() #Recoges el elemento y lo muestras
        print("\n", "Nombre: ", elementoMostrado["nombre"], "\tApellido: ", elementoMostrado["apellido"], "\tTelefono: ", elementoMostrado["telefono"], "\tEdad: ", elementoMostrado["edad"])


def muestraTodos(ref): #Muestra las personas de la DB:
    resultado = ref.get()

    for key in resultado: #Por cada contacto de la lista de resultados
        elemento = ref.child(key)
        elementoMostrado = elemento.get() #Recoges el elemento y lo muestras
        print("\n", "Nombre: ", elementoMostrado["nombre"], "\tApellido: ", elementoMostrado["apellido"], "\tTelefono: ", elementoMostrado["telefono"], "\tEdad: ", elementoMostrado["edad"])


def salir(ref): #Sale
    sys.exit()

credenciales = credentials.Certificate("fir-py-9f3fb-firebase-adminsdk-u15iy-7cad0111c8.json")
firebase_admin.initialize_app( credential=credenciales, options={"databaseURL" : "https://fir-py-9f3fb-default-rtdb.europe-west1.firebasedatabase.app/"})


switcher = {1:añadePersona,2:borraPersona,3:modificaPersona,4:buscaPersona,5:muestraTodos,6:salir}
ref = db.reference("contactos")

while(True): #Siempre
    try:
        opcion = int(input("\n\tMENU\n1: Añade Persona\n2: Borra Persona\n3: Modifica Persona\n4: Busca Persona\n5: Muestra Todos\n6: Salir\n"))
        switcher[opcion](ref)
    except Exception as e:
        print("\n¡¡ERROR!!")