import firebase_admin, sys, re
from firebase_admin import credentials,db

#Funciones necesarias:
def add_contact():
    name = input("Introduce el nombre del contacto: ").lower()
    surname = input("Introduce el apellido: ").lower()
    phone_number = phone_number_valide()
    address = input("Introduce la dirección: ").lower()
    mail = mail_valide()
    
    ref.push({
        'Nombre':name,
        'Apellido': surname,
        'Numero_de_telefono': phone_number,
        'Direccion' : address,
        'Correo_electronico' : mail
    })

def find_contact(print = True):
    name = input('Escribe nombre del contacto que quieras buscar: ')
    contactos = ref.order_by_child('Nombre').equal_to(name).get()
    if(print):
        print_contacts(contactos.values())
    else:
        return contactos

def delete_contact():
    contactos = find_contact(False)
    for contacto in contactos:
        contacto = ref.child(contacto)
        contact = contacto.get()
        print('---------------------------------------------------')
        print('Nombre: ', contact['Nombre'])
        print('Apellido: ', contact['Apellido'])
        print('Numero de telefono: ', contact['Numero_de_telefono'])
        print('Direccion: ', contact['Direccion'])
        print('Correo electronico: ', contact['Correo_electronico'])
        print('---------------------------------------------------')
        delete = input('Quieres borrar este contacto? (s/n(siguiente)): ')
        while(delete != 's' and delete != 'n'):
            delete = input('Quieres borrar este contacto? (s/n(siguiente)): ')
        if(delete == 's'):
            contacto.delete()
            return

def modify_contact():
    contactos = find_contact(False)
    for contacto in contactos:
        contacto = ref.child(contacto)
        contact = contacto.get()
        print('---------------------------------------------------')
        print('Nombre: ', contact['Nombre'])
        print('Apellido: ', contact['Apellido'])
        print('Numero de telefono: ', contact['Numero_de_telefono'])
        print('Direccion: ', contact['Direccion'])
        print('Correo electronico: ', contact['Correo_electronico'])
        print('---------------------------------------------------')
        modify = input('Quieres modificar este contacto? (s/n(siguiente)): ')
        while(modify != 's' and modify != 'n'):
            modify = input('Quieres modificar este contacto? (s/n(siguiente)): ')
        if(modify == 's'):
            contact = {
                'Nombre':contact['Nombre'],
                'Apellido': contact['Apellido'],
                'Numero_de_telefono': contact['Numero_de_telefono'],
                'Direccion' : contact['Direccion'],
                'Correo_electronico' : contact['Correo_electronico']
            }

            opcion = int(edit_option_valide())
            if(opcion == 3):
                contact['Numero_de_telefono'] = phone_number_valide(edit=True)
            elif(opcion == 5):
                contact['Correo_electronico'] = mail_valide(edit=True)
            else:
                for campo in contact.keys():
                    if(opcion == list(contact.keys()).index(campo)+1):
                        contact[campo] = input('Introduce nuevo/a '+campo.replace('_',' ').lower()+': ').lower()
                        break
            contacto.update(contact)
            return

def all_contacts():
    try:
        contactos = ref.get().values()
    except:
        print('No hay contactos en la base de datos')
    else:
        print_contacts(contactos)

def print_contacts(contacts):
    for contact in contacts:
        print('---------------------------------------------------')
        print('Nombre: ', contact['Nombre'].title())
        print('Apellido: ', contact['Apellido'].title())
        print('Numero de telefono: ', contact['Numero_de_telefono'])
        print('Direccion: ', contact['Direccion'].title())
        print('Correo electronico: ', contact['Correo_electronico'])
        print('---------------------------------------------------')

def phone_number_valide(edit = False):
    if(edit):
        number = input("Introduce el número de teléfono: ")
    else:
        number = input("Introduce nuevo número de teléfono: ")
    filter = re.compile('^\d{9}$')
    number = re.findall(filter,number)
    while(len(number) != 1):
        number = input('Formato de numero no válido, introduce otro (9 numeros): ')
        filter = re.compile('^\d{9}$')
        number = re.findall(filter,number)
    return number[0]

def mail_valide(edit = False):
    if(edit):
        mail = input("Introduce nuevo correo electrónico: ")
    else:
        mail = input("Introduce el correo electrónico: ")
    filter = re.compile('.+@.+\.com|.+@.+\.es')
    mail = re.findall(filter,mail)
    while(len(mail) != 1):
        mail = input('Formato de email no válido, introduce otro (xxx@xxx.com/es): ')
        filter = re.compile('.+@.+\.com|.+@.+\.es')
        mail = re.findall(filter,mail)
    return mail[0]

def edit_option_valide(error = False):
    if(error):
        print('ERROR!! Introduce una opcion valida\nQue campo quieres modificar?\n')
    else:
        print('Que campo quieres modificar?\n')
    opcion = input('1: Nombre\n'
                +'2: Apellido\n'
                +'3: Numero de telefono\n'
                +'4: Direccion\n'
                +'5: Correo electronico\n')
    if(opcion not in ['1','2','3','4','5'] or not opcion.isdigit()):
        return edit_option_valide(error=True)
    else:
        return opcion

def out():
    sys.exit()

#Firebase:
credenciales = credentials.Certificate('credenciales.json')
firebase_admin.initialize_app(credential=credenciales, options={"databaseURL" : "https://agenda-1720b-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference('contactos')
#menu
switcher = {
    1: add_contact,
    2: delete_contact,
    3: modify_contact,
    4: find_contact,
    5: all_contacts,
    6: out
}
#menu = int(input("Seleccione las opciones:\n1: Añadir contacto \n2: Borrar contacto \n3: Modificar contacto \n4: Muestra todos los contactos \n5: Salir"))
#switcher[menu]()

while (True):
    try:
        menu = int(input("\nSeleccione las opciones:\n1: Añadir contacto \n2: Borrar contacto \n3: Modificar contacto \n4: Busca contacto \n5: Muestra todos los contactos \n6: Salir\n-> Introduce una opción: "))
        switcher[menu]()
    except Exception as e:
        print("Error, asegurate de haber introducido los datos correctos.")
