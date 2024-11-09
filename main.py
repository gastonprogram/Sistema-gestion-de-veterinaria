#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

from clientes import *
from profesionales import *
from mascotas import *
from turnos import *
from informes import *
from colorama import Fore, Style, init
# Inicializar colorama
init(autoreset=True)



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

def main():

    #-------------------------------------------------
    # Inicialización de variables
    #-------------------------------------------------
    
    archivoClientesGuardadosRuta = r"clientes_guardados.json"
    archivoMascotasGuardadasRuta = r"mascotas_guardadas.json"
    archivoProfesionalesGuardadosRuta = r"profesionales_guardados.json"
    archivoTurnosProgramadosRuta = r"turnos_programados.json"


    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------

    while True:
        print()
        print(Fore.CYAN + "="*40)
        print(Fore.YELLOW + "            MENÚ SISTEMA")
        print(Fore.CYAN + "="*40)
        print(Fore.BLUE + "[1]"  + " Gestionar Clientes")
        print(Fore.GREEN + "[2]"  + " Gestionar Mascotas")
        print(Fore.RED + "[3]"  + " Gestionar Profesionales")
        print(Fore.WHITE + "[4]"  + " Gestionar Turnos")
        print(Fore.MAGENTA + "[5]"  + " Informes")

        print(Fore.CYAN + "="*40)
        print(Fore.CYAN + "[0]"  + " Salir del programa")
        print()
            
        opcion_principal = input("Seleccione una opción: ")
        print(" ")
        if opcion_principal == "1":  # Submenú de Clientes
            while True:
                print(Fore.CYAN + "="*40)
                print(Fore.BLUE + "            MENÚ CLIENTES")
                print(Fore.CYAN + "="*40)

                print(Fore.BLUE + "[1]" + Style.RESET_ALL + " Listar Clientes")
                print(Fore.BLUE + "[2]" + Style.RESET_ALL + " Agregar Cliente")
                print(Fore.BLUE + "[3]" + Style.RESET_ALL + " Modificar Cliente")
                
                print(Fore.CYAN + "="*40)
                print(Fore.CYAN + "[0]"  + " Volver al menu principal")

                print(" ")
                opcion_clientes = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
                print(" ")
                
                if opcion_clientes == "1": # listar clientes
                    
                    mostrarInformacionClientes(archivoClientesGuardadosRuta)
                
                elif opcion_clientes == "2":  # agregar cliente

                    # solicitar informacion para crear un nuevo cliente
                    informacionCliente = informacionClienteNuevo(archivoClientesGuardadosRuta)

                    #guardar la informacion del nuevo cliente en el diccionario
                    if informacionCliente:
                        guardarCliente(informacionCliente, archivoClientesGuardadosRuta)

                elif opcion_clientes == "3": # modificar cliente

                    # solicitar informacion para modificar un cliente
                    informacionClienteModificar = modificarInformacionCliente(archivoClientesGuardadosRuta)
                    
                    #guardar la informacion del cliente a modificar en el diccionario
                    if informacionClienteModificar:
                        guardarCliente(informacionClienteModificar, archivoClientesGuardadosRuta)

                elif opcion_clientes == "0":  # Volver al menú principal
                    break
        
        elif opcion_principal == "2":  # Submenú de Mascotas
            while True:
                print(Fore.CYAN + "="*40)
                print(Fore.GREEN + "            MENÚ MASCOTAS")
                print(Fore.CYAN + "="*40)

                print(Fore.GREEN + "[1]" + Style.RESET_ALL + " Listar Mascotas")
                print(Fore.GREEN + "[2]" + Style.RESET_ALL + " Agregar Mascota")
                print(Fore.GREEN + "[3]" + Style.RESET_ALL + " Modificar Mascota")
                
                print(Fore.CYAN + "="*40)
                print(Fore.CYAN + "[0]" + " Volver al menu principal")
                print(" ")
                opcion_mascotas = input(Fore.YELLOW + "Seleccione una opción: " )
                print(" ")


                if opcion_mascotas == "1":
                    
                    mostrarInformacionMascotas(archivoMascotasGuardadasRuta)
                    
                elif opcion_mascotas == "2":

                    # solicitar informacion para añadir una nueva mascota
                    infoMascotaNueva = informacionMascotaNueva(archivoClientesGuardadosRuta)

                    # guardar la informacion de la nueva mascota en la lista
                    if infoMascotaNueva:
                        guardarMascotaNueva(infoMascotaNueva, archivoMascotasGuardadasRuta)

                elif opcion_mascotas == "3":
                    
                    # solicitar informacion para modificar una mascota  existente
                    infoMascotaModificar = modificarInformacionMascotaExistente(archivoClientesGuardadosRuta, archivoMascotasGuardadasRuta)
                    
                    #guardar la informacion modificada sobre la mascota en la lista
                    if infoMascotaModificar:
                        guardarMascotaModificada(infoMascotaModificar, archivoMascotasGuardadasRuta)

                
                elif opcion_mascotas == "0":  # Volver al menú principal
                    break
        
        elif opcion_principal == "3":  # Submenú de Profesionales
            while True:
                print(Fore.CYAN + "="*40)
                print(Fore.RED + "            MENÚ PROFESIONALES")
                print(Fore.CYAN + "="*40)

                print(Fore.RED + "[1]" + Style.RESET_ALL + " Listar Profesionales")
                print(Fore.RED + "[2]" + Style.RESET_ALL + " Agregar Profesional")
                print(Fore.RED + "[3]" + Style.RESET_ALL + " Modificar Profesional")
                print(Fore.RED + "[4]" + Style.RESET_ALL + " Eliminar Profesional")
                print(" ")
                print(Fore.CYAN + "="*40)
                print(Fore.CYAN + "[0]"  + " Volver al menu principal")
                print(" ")
                opcion_profesionales = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
                print()

                if opcion_profesionales == "1":
                    
                    mostrarInformacionProfesional(archivoProfesionalesGuardadosRuta)
                    

                elif opcion_profesionales == "2": #añadir profesional

                    # solicitar informacion para añadir un nuevo profesional
                    infoNuevoProfesional = informacionProfesionalNuevo(archivoProfesionalesGuardadosRuta)
                    
                    #guardar la informaicon del profesional en el diccionario
                    if infoNuevoProfesional:
                        guardarInformacionProfesional(infoNuevoProfesional, archivoProfesionalesGuardadosRuta)

                elif opcion_profesionales == "3": #modificar profesional

                    #solicitar informacion para modificar un profesional existente
                    infoProfesionalModificar = modificarInformacionProfesional(archivoProfesionalesGuardadosRuta)
                    
                    #guardar la informacion del profesional a modificar en el diccionario
                    if infoProfesionalModificar:
                        guardarInformacionProfesional(infoProfesionalModificar, archivoProfesionalesGuardadosRuta)


                elif opcion_profesionales == "4": #eliminar profesional

                    # se elimina el profesional elegido del diccionario
                    eliminarProfesional(archivoProfesionalesGuardadosRuta)
                        
                elif opcion_profesionales == "0":  # Volver al menú principal
                    break
        
        elif opcion_principal == "4":  # Submenú de Turnos
            while True:
                
                print(Fore.CYAN + "="*40)
                print(Fore.WHITE + "            MENÚ TURNOS")
                print(Fore.CYAN + "="*40)

                print(Fore.WHITE + "[1]" + Style.RESET_ALL + " Listar Turnos")
                print(Fore.WHITE + "[2]" + Style.RESET_ALL + " Programar Turno")
                print(Fore.WHITE + "[3]" + Style.RESET_ALL + " Modificar Turno")
                print(Fore.WHITE + "[4]" + Style.RESET_ALL + " Cancelar Turno")
                print(" ")
                print(Fore.CYAN + "="*40)
                print(Fore.CYAN + "[0]" + " Volver al menu principal")
                print()
                opcion_turnos = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
                print()

                if opcion_turnos == "1":
                    
                    mostrarInformacionTurnos(archivoTurnosProgramadosRuta)

                elif opcion_turnos == "2": #programar turno nuevo
                    
                    #solicitar informacion para añadir un nuevo turno
                    infoTurnoNuevo = informacionTurnoCliente(archivoClientesGuardadosRuta, archivoMascotasGuardadasRuta, archivoProfesionalesGuardadosRuta, archivoTurnosProgramadosRuta)
                    
                    # añadir el turno con la informacion en la lista
                    if infoTurnoNuevo:
                        añadirTurnoCliente(infoTurnoNuevo, archivoTurnosProgramadosRuta)


                elif opcion_turnos == "3": #modificar turno

                    #solicitar informacion para modificar un turno
                    modificarTurnoCliente(archivoTurnosProgramadosRuta, archivoClientesGuardadosRuta, archivoProfesionalesGuardadosRuta)


                elif opcion_turnos == "4": # cancelar turno

                    cancelarTurnoCliente(archivoTurnosProgramadosRuta, archivoClientesGuardadosRuta)

                elif opcion_turnos == "0":  # Volver al menú principal
                    break

        elif opcion_principal == "5":  # Submenú de informes
            while True:
                print(Fore.CYAN + "="*40)
                print(Fore.MAGENTA + "            MENÚ INFORMES")
                print(Fore.CYAN + "="*40)
                print(Fore.MAGENTA +"[1]" + Style.RESET_ALL + " Turnos por profesional")
                print(Fore.MAGENTA +"[2]" + Style.RESET_ALL + " Turnos por mascota")
                print(Fore.MAGENTA +"[3]" + Style.RESET_ALL + " Turnos en un rango de dias")
                print(Fore.MAGENTA +"[4]" + Style.RESET_ALL + " Turnos en un rango de horas")
                print(" ")
                print(Fore.CYAN + "="*40)
                print(Fore.CYAN + "[0]" + " Volver al menu principal")
                print()
                opcion_informes = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
                print()

                if opcion_informes == "1":

                    #mostrar turnos en los que se encuentra un profesional en especifico 
                    desplegarTurnosPorProfesional(archivoTurnosProgramadosRuta, archivoProfesionalesGuardadosRuta)

                elif opcion_informes == "2":
                    #mostrar los turnos en los que se encuentra una mascota en especifica
                    desplegarTurnosPorMascota(archivoMascotasGuardadasRuta, archivoTurnosProgramadosRuta, archivoClientesGuardadosRuta)

                elif opcion_informes == "3":

                    
                    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
                    fechaInicio = input("Fecha de inicio (DD/MM/AAAA): ")
                    while not re.match(patronFecha, fechaInicio):
                        print("El formato o la fecha es incorrecta.")
                        fechaInicio = input("Fecha de inicio (DD/MM/AAAA): ")

                    fechaFinal = input("Fecha de fin (DD/MM/AAAA): ")
                    while not re.match(patronFecha, fechaFinal):
                        print("El formato o la fecha es incorrecta.")
                        fechaFinal = input("Fecha de fin (DD/MM/AAAA): ")


                    mostrarTurnosPorFecha(archivoTurnosProgramadosRuta, fechaInicio, fechaFinal)
                
                
                elif opcion_informes == "4":

                    fecha = input("Fecha (DD/MM/AAAA): ")
                    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
                    while not re.match(patronFecha, fecha):
                        print("El formato o la fecha es incorrecta.")
                        fecha = input("Fecha (DD/MM/AAAA): ")

                    patronHorario = "^(0[0-9]|1[0-9]|2[0-3]):00$"

                    horarioInicio = input("Horario de inicio (HH:00): ")
                    while not re.match(patronHorario, horarioInicio):
                        print("El formato o la fecha es incorrecta.")
                        horarioInicio = input("Horario de inicio (HH:00): ")
                    horarioFinal = input("Horario final (HH:00): ")
                    while not re.match(patronHorario, horarioFinal):
                        print("El formato o la fecha es incorrecta.")
                        horarioFinal = input("Horario final (HH:00): ")

                    horaInicioRecortado = horarioInicio[:2]
                    horaFinalRecortado = horarioFinal[:2]

                    mostrarTurnosPorFechaYHorarios(archivoTurnosProgramadosRuta, fecha, horaInicioRecortado, horaFinalRecortado)
                
                elif opcion_informes == "0":  # Volver al menú principal
                    break
            
        elif opcion_principal == "0":
            print(Fore.CYAN +"Saliendo del sistema...")
            
            break

        else:
            print(Fore.RED +"Opción inválida. Intente de nuevo.")

        
        opcion_principal = ""

# Punto de entrada al programa
main()
