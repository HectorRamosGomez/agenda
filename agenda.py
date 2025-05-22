#Main de la agenda

import funciones

print(funciones.menuAgendaContactos())
opcion = int(input("> "))

while opcion != 10:
    match opcion:
        case 1: 
            funciones.crearAgenda()
        case 2:
            funciones.mostrarAgenda()
        case 3:
            funciones.agregarContacto()
        case 4:
            funciones.buscarContacto()
        case 5:
            funciones.editarContacto()
        case 6:
            funciones.borrarContactos()
        case 7:
            funciones.importarArchivos()
        case 8:
            funciones.exportarArchivos()
        case 9:
            funciones.ordenarArchivo()
        case _: 
            print("Opción no válida. Intenta de nuevo.")

    print(funciones.menuAgendaContactos())
    try:
        opcion = int(input("> "))
    except ValueError:
        print("Entrada no válida. Saliendo del programa.")
        break

print("Programa finalizado.")