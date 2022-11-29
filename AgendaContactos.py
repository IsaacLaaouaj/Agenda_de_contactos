import firebase_admin
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
        'Número de teléfono': phone_number,
        'Direccion' : address,
        'Correo electronico' : mail
    })

def delete_contact():
    remove_contact = input("Introduce el nombre del contacto que quieres borrar: ")

def modify_contact():
    #Elige la opción que quieres modificar.
    pass
def all_contacts():
    for contact in ref.get().values():
        print('Nombre: ',contact['Nombre'])
    


#Firebase:
credenciales = credentials.Certificate('agenda-1720b-firebase-adminsdk-nbaiz-0e38f4eba0.json')
firebase_admin.initialize_app(credential=credenciales, options={"databaseURL" : "https://agenda-1720b-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference('contactos')

#menu
switcher = {
    1: add_contact,
    2: delete_contact,
    3: modify_contact,
    4: all_contacts
}
menu = int(input("Seleccione las opciones:\n1: Añadir contacto \n2: Borrar contacto"))  
switcher[menu]()

