import firebase_admin
from firebase_admin import credentials,db
def add_contact():
    name = input("Introduce el nombre del contacto: ")
    surname = input("Introduce el apellido: ")
    phone_number = input("Introduce el número de teléfono: ")
    adress = input("Introduce la dirección: ")
    mail = input("Indroduce el correo electrónico: ")

def delete_contact():
    remove_contact = input("Introduce el contacto que quieres borrar: ")

switcher = {
    1: add_contact,
    2: delete_contact
}
menu = input("Seleccione las opciones:\n1: Añadir contacto \n2: Borrar contactos")

credenciales = credentials.Certificate('agenda-1720b-firebase-adminsdk-nbaiz-0e38f4eba0.json')
firebase_admin.initialize_app(credenciales)