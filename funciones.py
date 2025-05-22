#Funciones de la agenda

import re

def menuAgendaContactos():
    print("Agenda ")
    print("(1). Crea una agenda. ")
    print("(2). Mostrar agenda. ")
    print("(3). Agregar un contacto. ")
    print("(4). Buscar contacto por nombre. ")
    print("(5). Editar contacto. ")
    print("(6). Eliminar contacto. ")
    print("(7). Importar de un archivo a otro. ")
    print("(8). Exportar a otro archvo. ")
    print("(9). Datos ordenados alfabeticamente. ")


# 1 Funcion de crear Agenda
def crearAgenda () :
    agenda = open ("agendaContactos.txt", "w")
    agenda.close()

# 2 Funcion agregar contactos varios
def agregarContacto () :
    nombre = input("Introduce tu nombre: ")
    telefono = input("Introudce tu telfono: ")
    correo = input("Introduce tu correo: ")
    nombre = nombre

    if not validarDatos(correo):
        print("Datos inválidos. Intenta nuevamente.")
        return
    
    contacto_encontrado = False

    with open("agendaContactos.txt", "r") as agenda:
        lineas = agenda.readlines()

    with open("agendaContactos.txt", "w") as agenda:
        for linea in lineas:
            if nombre not in linea:
                agenda.write(linea)
            else:
                contacto_encontrado = True

    if contacto_encontrado:
        print("El contacto ha sido eliminado.")

    with open("agendaContactos.txt", "a") as agenda:
        agenda.write(f"Nombre: {nombre}, Telefono: {telefono}, Correo:{correo}\n")

    print("El contacto se agrego correctamente")

# 3 MOstra agendas
def mostrarAgenda():
    try:
        with open("agendaContactos.txt", "r") as agenda:
            content = agenda.read()
            print(content)
    except FileNotFoundError:
        print("El archivo 'agendaContactos.txt' no existe.")

#Buscador de contactos
def buscarContacto():
    nombre = input("Introduce el nombre a buscar o patron a buscar: ").lower()
    encontrado = False

    with open("agendaContactos.txt", "r") as agenda:
        lineas = agenda.readlines()
        for linea in lineas:
            if nombre in linea.lower():
                print("Datos del contacto encontrado:")
                print(linea.strip())
                encontrado = True

    if not encontrado:
        print("No se encontró ningún contacto con ese nombre.")


#Editor de contactos
def editarContacto():
    nombre = input("El nombre del contacto existente es: ")
    nuevoNombre = input("Introduce el nuevo nombre: ")
    nuevoTelefono = input("Introduce el nuevo teléfono: ")
    nuevoCorreo = input("Introduce el nuevo correo: ")

    with open("agendaContactos.txt", "r") as agenda:
        lineas = agenda.readlines()

    contacto_encontrado = False


    with open("agendaContactos.txt", "w") as agenda:
        for linea in lineas:
            if nombre in linea:
                agenda.write(f"{nuevoNombre},{nuevoTelefono},{nuevoCorreo}\n")
                contacto_encontrado = True
            else:
                agenda.write(linea)

    if contacto_encontrado:
        print("El contacto ha sido actualizado")
    else:
        print("No se encontró el contacto para actualizarlo")

#Borrador de contactos 
def borrarContactos():
    nombre = input("Nombre del contacto a borrar: ")
    contacto_encontrado = False

    with open("agendaContactos.txt", "r") as agenda:
        lineas = agenda.readlines()

    with open("agendaContactos.txt", "w") as agenda:
        for linea in lineas:
            if nombre not in linea:
                agenda.write(linea)
            else:
                contacto_encontrado = True

    if contacto_encontrado:
        print("El contacto ha sido eliminado.")
    else:
        print("Contacto no encontrado.")

#Ordenador los datos

def ordenarArchivo():
    with open("agendaContactos.txt", "r") as archivo:
        lineas = archivo.readlines()

    lineas_ordenadas = sorted([linea.strip() for linea in lineas])

    with open("agendaContactos.txt", "w") as archivo:
        for linea in lineas_ordenadas:
            archivo.write(linea + "\n")

    print("Archivo ordenado alfabéticamente.")

    with open("agendaContactos.txt", "r") as agenda:
        content = agenda.read()
        print(content)
    

#importar datos
def importarArchivos():
    importFile = input("Introduce el nombre del archivo a importar: ")
    with open(importFile,'r') as primerArchivo, open('agendaContactos.txt','a') as segundoArchivo:
        for line in primerArchivo:
             segundoArchivo.write(line)

#Exportar datos
def exportarArchivos () :
    exportFile = input("Introduce el nombre del archivo que quieres crear para exportar: ")
    agenda = open (exportFile, "w")
    agenda.close()

    with open("agendaContactos.txt",'r') as primerArchivo, open(exportFile,'w') as segundoArchivo:
        for line in primerArchivo:
            segundoArchivo.write(line)

#Validar datos
def validarDatos(correo):
    patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    if not re.match(patron_correo, correo):
        print("Correo no válido.")
        return False
    
    return True

