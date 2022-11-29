import firebase_admin, sys
from firebase_admin import credentials,db

#Funciones necesarias:
def add_contact():
    name = input("Introduce el nombre del contacto: ")
    surname = input("Introduce el apellido: ")
    phone_number = input("Introduce el número de teléfono: ")
    address = input("Introduce la dirección: ")
    mail = input("Indroduce el correo electrónico: ")
    
    ref.push({
        'Nombre':name,
        'Apellido': surname,
        'Numero_de_telefono': phone_number,
        'Direccion' : address,
        'Correo_electronico' : mail
    })

def delete_contact():
    remove_contact = input("Introduce el nombre del contacto que quieres borrar: ")

def modify_contact():
    #Elige la opción que quieres modificar.
    pass

def all_contacts():
    try:
        contactos = ref.get().values()
    except:
        print("Error, porfavor introducir algún contacto.")
        return
    for contact in contactos:
        print('\n---------------------------------------------------')
        print('Nombre: ', contact['Nombre'])
        print('Apellido: ', contact['Apellido'])
        print('Numero de telefono: ', contact['Numero_de_telefono'])
        print('Direccion: ', contact['Direccion'])
        print('Correo electronico: ', contact['Correo_electronico'])
        print('---------------------------------------------------\n')

def out():
    sys.exit()

#Firebase:
credenciales = credentials.Certificate('agenda-1720b-firebase-adminsdk-nbaiz-0e38f4eba0.json')
firebase_admin.initialize_app(credential=credenciales, options={"databaseURL" : "https://agenda-1720b-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference('contactos')

#menu
switcher = {
    1: add_contact,
    2: delete_contact,
    3: modify_contact,
    4: all_contacts,
    5: out
}

#Bucle
while (True):
    try:
        menu = int(input("Seleccione las opciones:\n1: Añadir contacto \n2: Borrar contacto \n3: Modificar contacto \n4: Muestra todos los contactos \n5: Salir\n"))
        switcher[menu]()
    except Exception as e:
        print("Error, asegurate de haber introducido los datos correctos.")
