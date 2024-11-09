import re
from datetime import datetime
from utiles import verificarDocumento
import json
from utiles import *



def mostrarInformacionTurnos(rutaArchivoTurnosProgramados):
    
    try:
        archivoLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
        turnosProgramados = json.load(archivoLeer)
        archivoLeer.close()
        
        for turno in turnosProgramados:
            print(f"\nCliente (DNI): {turno['documentoIdentidadCliente']}")
            print(f"Mascota (Índice): {turno['indiceMascota']}  |  Profesional (DNI): {turno['documentoIdentidadProfesional']}")
            print(f"Fecha: {turno['fecha']}  |  Horario: {turno['horario']}  |  Motivo: {turno['motivo']}  |  Estado: {'Activo' if turno['activo'] else 'Cancelado'}")
            print("-" * 60)
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
    
    finally:
        try:
            archivoLeer.close()
            
        except:
            pass



def informacionTurnoCliente(rutaArchivoClientesGuardados, rutaArchivoMascotasGuardados, rutaArchivoProfesionalGuardados, rutaArchivoTurnosProgramados):


    """
    Solicita y valida la información de un nuevo turno para agregarlo al sistema

    PARAMETROS:
    diccClientesGuardados(dict): diccionario que contiene diccionarios con informacion de clientes
    listMascotasGuardadas(list): lista que contiene diccionarios con informacion de mascotas
    diccProfesionalesGuardados(dict): diccionario con los profesionales guardados:
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    

    SALIDA:
        - documentoIdentidadDueño (str): Número de DNI del dueño de la mascota.
        - indiceMascotaGeneral (int): indice de la mascota asignada al turno 
        - documentoIdentidadProfesional (str): Número de DNI del especialista.
        - fecha (str): fecha del turno en formato DD/MM/AAAA
        - horarioSeleccionado (str): horario del turno
        - motivo(str): motivo de la consulta
    """

    documentoIdentidadCliente = verificarDocumento(rutaArchivoClientesGuardados, True)
    if documentoIdentidadCliente == -1:
        return
    elif documentoIdentidadCliente == False:
        return
    
    archivoMascotasLeer = open(rutaArchivoMascotasGuardados, "r", encoding = "utf-8")
    mascotasGuardadas = json.load(archivoMascotasLeer)
    archivoMascotasLeer.close()
    
    mascotasCliente = [m for m in mascotasGuardadas if m["documentoIdentidadDueño"] == documentoIdentidadCliente]

    if not mascotasCliente:
        print("Este cliente no tiene mascotas registradas.")
        return None
    
    for i, mascota in enumerate(mascotasCliente):
        print(f"[{i}] Nombre: {mascota['nombre']}, Especie: {mascota['especie']}")

    while True:
        try:
            indiceMascotaCliente = int(input("Seleccione la mascota: "))
            
            if indiceMascotaCliente < 0:
                print("El indice no puede ser negativo. Por favor, intenta de nuevo.")
            elif indiceMascotaCliente >= len(mascotasCliente):
                print(f"El índice debe estar entre 0 y {len(mascotasCliente) - 1}. Por favor, intenta de nuevo.")
            else:
                break  
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    mascotaSeleccionada = mascotasCliente[indiceMascotaCliente]
    indiceMascotaGeneral = mascotasGuardadas.index(mascotaSeleccionada)


    archivoProfesionalesLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
    profesionalesGuardados = json.load(archivoProfesionalesLeer)
    archivoProfesionalesLeer.close()
    
    # Filtrar profesionales activos
    profesionalesActivos = [(dni, profesional) for dni, profesional in profesionalesGuardados.items() if profesional['activo']]

    print("------------------------------------------------------------------------------------------------------------------")
    print("Información de especialistas:")
    for i, (dni, profesional) in enumerate(profesionalesActivos):
        # Mostrar información clave de cada profesional para seleccionar por índice
        print(f"[{i}] DNI: {dni}, Nombre: {profesional['nombreCompleto']}, Especialización: {profesional['especializacion']}, Horario de atención: {profesional['horarioAtencion']}.")
    print("------------------------------------------------------------------------------------------------------------------")

    # Seleccionar especialista por índice
    while True:
        try:
            indiceProfesional = int(input("Seleccione el profesional: "))
            
            if indiceProfesional < 0:
                print("El indice no puede ser negativo. Por favor, intenta de nuevo.")
            elif indiceProfesional >= len(profesionalesActivos):
                print(f"El indice debe estar entre 0 y {len(profesionalesActivos) - 1}. Por favor, intenta de nuevo.")
            else:
                break  # indice valido
        except ValueError:
            print("Entrada no valida. Por favor, ingrese un número.")

    # acceder al profesional seleccionado
    documentoIdentidadProfesional, profesionalSeleccionado = profesionalesActivos[indiceProfesional]
    horarios = profesionalSeleccionado['horarioAtencion']
    print(f"Has seleccionado a: {profesionalSeleccionado['nombreCompleto']}, Horario de atención: {horarios}")
    
    
    # obtener y separar el horario del profesional 
    horarioInicio = int(horarios[:2])  
    horarioFinal = int(horarios[8:10])  

    # crear una lista con todos los horarios en formato HH:00 en el rango de atencion 
    horariosDisponibles = [f"{hora:02d}:00" for hora in range(horarioInicio, horarioFinal)]


    # seleccionar la fecha y verificar que este correcta
    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    while True:
        fecha = input("Fecha (DD/MM/AAAA): ")
        
        if re.match(patronFecha, fecha):
            fecha_ingresada = datetime.strptime(fecha, "%d/%m/%Y")

            #fecha actual
            fecha_actual = datetime.now()

            if fecha_ingresada > fecha_actual:
                break
            else:
                print("La fecha ingresada es anterior a la fecha actual. Intente de nuevo.")
        else:
            print("El formato o la fecha es incorrecta. Intente de nuevo")

    #filtrar los horarios que ya estan ocupados
    archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding = "utf-8")
    turnosProgramados = json.load(archivoTurnosLeer)
    archivoTurnosLeer.close()
    for turno in turnosProgramados:
        if turno['fecha'] == fecha and turno['documentoIdentidadProfesional'] == documentoIdentidadProfesional:
            if turno['horario'] in horariosDisponibles:
                horariosDisponibles.remove(turno['horario'])


    #mostrar los horarios disponibles al usuario 
    print("Horarios disponibles:")
    for i, horario in enumerate(horariosDisponibles):
        print(f"[{i}] {horario}")

    # Seleccionar un horario disponible con opción numérica
    while True:
        try:
            seleccion = int(input("Seleccione una opción de horario: "))
            
            if seleccion < 0:
                print("El índice no puede ser negativo. Por favor, intenta de nuevo.")
            elif seleccion >= len(horariosDisponibles):
                print(f"El índice debe estar entre 0 y {len(horariosDisponibles) - 1}. Por favor, intenta de nuevo.")
            else:
                break  # Índice válido
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    # Asignar el horario seleccionado
    horarioSeleccionado = horariosDisponibles[seleccion]
            
        
    #ingresar el motivo del turno
    motivo = input("Motivo: ")

    return documentoIdentidadCliente, indiceMascotaGeneral, documentoIdentidadProfesional, fecha, horarioSeleccionado, motivo

def añadirTurnoCliente(informacionTurno, rutaArchivoTurnosProgramados):
    #desempaquetar la informacion del turno
    documentoIdentidadDueño, indiceMascotaSeleccionada, documentoIdentidadProfesional, fecha, horario, motivo = informacionTurno

    try:
        archivoLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
        turnosGuardados = json.load(archivoLeer)
        archivoLeer.close()

        
        turnosGuardados.append({
            "documentoIdentidadCliente": documentoIdentidadDueño,
            "indiceMascota": indiceMascotaSeleccionada,
            "documentoIdentidadProfesional": documentoIdentidadProfesional,
            "fecha": fecha,
            "horario": horario,
            "motivo": motivo,
            "activo": True
        })

        # guardar los cambios en el archivo
        archivoEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
        json.dump(turnosGuardados, archivoEscribir, indent=4)
        archivoEscribir.close()
        
        print(f"Turno agregado con éxito!")
        
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    return


def modificarTurnoCliente(rutaArchivoTurnosProgramados, rutaArchivoClientesGuardados, rutaArchivoProfesionalGuardados):
    
    
    documentoIdentidadCliente = verificarDocumento(rutaArchivoClientesGuardados, True)
    if documentoIdentidadCliente == -1:
        return
    elif documentoIdentidadCliente == False:
        return

    # Filtrar los turnos que sean del cliente, que no esten cancelados y que sean posteriores a la fecha actual

    fecha_actual = datetime.now()
    turnosCliente = []

    archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
    turnosGuardados = json.load(archivoTurnosLeer)
    archivoTurnosLeer.close()
    
    turnosCliente = [
    turno for turno in turnosGuardados 
    if turno['documentoIdentidadCliente'] == documentoIdentidadCliente 
    and turno["activo"] == True 
    and datetime.strptime(turno['fecha'], "%d/%m/%Y") >= fecha_actual
    ]

    if not turnosCliente:
        print("Este cliente no tiene turnos asignados.")
        return None

    # Mostrar los turnos del cliente
    print("Turnos del cliente:")
    for i, turno in enumerate(turnosCliente):
        print(f"[{i}] Fecha: {turno['fecha']}, Horario: {turno['horario']}, Especialista DNI: {turno['documentoIdentidadProfesional']}, Motivo: {turno['motivo']}")

        
    # Seleccionar turno por índice
    while True:
        try:
            indiceTurno = int(input("Seleccione el turno que desea modificar: "))
            
            if indiceTurno < 0:
                print("El indice no puede ser negativo. Por favor, intenta de nuevo.")
            elif indiceTurno >= len(turnosCliente):
                print(f"El indice debe estar entre 0 y {len(turnosCliente) - 1}. Por favor, intenta de nuevo.")
            else:
                break  # indice valido
        except ValueError:
            print("Entrada no valida. Por favor, ingrese un número.")

    turnoSeleccionado = turnosCliente[indiceTurno]
    
    """
    indiceGeneralTurno = turnosGuardados.index(turnoSeleccionado)
    
    
    indiceMascota = turnoSeleccionado['indiceMascota']
    """



    #menu de modificaciones
    while True:
        print("\n¿Qué desea modificar?")
        print("[1] Fecha")
        print("[2] Horario")
        print("[3] Especialista")
        print("[4] Motivo")
        print("[0] Terminar")
        opcion = int(input("Seleccione una opción: "))

        # Modificar el campo seleccionado
        if opcion == 1:
            
            
            #modificar fecha
            nuevaFecha = ingresarFecha()
            turnoSeleccionado['fecha'] = nuevaFecha
            
            archivoTurnosEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
            json.dump(turnosGuardados, archivoTurnosEscribir, indent = 4, ensure_ascii = False)
            archivoTurnosEscribir.close()
            
            
            #modificar horario
            archivoLeerProfesionales = open(rutaArchivoProfesionalGuardados, "r", encoding = "utf-8")
            profesionalesGuardados = json.load(archivoLeerProfesionales)
            archivoLeerProfesionales.close()

            nuevoHorario = seleccionarHorario(turnosGuardados, turnoSeleccionado, profesionalesGuardados)
            turnoSeleccionado['horario'] = nuevoHorario
            
            archivoTurnosEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
            json.dump(turnosGuardados, archivoTurnosEscribir, indent = 4, ensure_ascii = False)
            archivoTurnosEscribir.close()
            
            print("Fecha y horario modificado correctamente.")

        elif opcion == 2:

            #modificar horario
            archivoLeerProfesionales = open(rutaArchivoProfesionalGuardados, "r", encoding = "utf-8")
            profesionalesGuardados = json.load(archivoLeerProfesionales)
            archivoLeerProfesionales.close()

            nuevoHorario = seleccionarHorario(turnosGuardados, turnoSeleccionado, profesionalesGuardados)
            turnoSeleccionado['horario'] = nuevoHorario
            
            archivoTurnosEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
            json.dump(turnosGuardados, archivoTurnosEscribir, indent = 4, ensure_ascii = False)
            archivoTurnosEscribir.close()
                        
            print("Horario modificado correctamente.")


        elif opcion == 3:

            #modificar profesional
            archivoProfesionalesLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
            profesionalesGuardados = json.load(archivoProfesionalesLeer)
            archivoProfesionalesLeer.close()
            
            # filtrar profesionales activos
            profesionalesActivos = [(dni, profesional) for dni, profesional in profesionalesGuardados.items() if profesional['activo']]
            print(profesionalesActivos)

            print("------------------------------------------------------------------------------------------------------------------")
            print("Información de especialistas:")
            for i, (dni, profesional) in enumerate(profesionalesActivos):
                # Mostrar información clave de cada profesional para seleccionar por índice
                print(f"[{i}] DNI: {dni}, Nombre: {profesional['nombreCompleto']}, Especialización: {profesional['especializacion']}, Horario de atención: {profesional['horarioAtencion']}.")
            print("------------------------------------------------------------------------------------------------------------------")

            # seleccionar profesional por índice
            while True:
                try:
                    indiceProfesional = int(input("Seleccione el profesional: "))
                    
                    if indiceProfesional < 0:
                        print("El indice no puede ser negativo. Por favor, intenta de nuevo.")
                    elif indiceProfesional >= len(profesionalesActivos):
                        print(f"El indice debe estar entre 0 y {len(profesionalesActivos) - 1}. Por favor, intenta de nuevo.")
                    else:
                        break  # indice valido
                except ValueError:
                    print("Entrada no valida. Por favor, ingrese un número.")
                    
            documentoIdentidadProfesional = profesionalesActivos[indiceProfesional][0]
            print(documentoIdentidadProfesional)
            turnoSeleccionado['documentoIdentidadProfesional'] = documentoIdentidadProfesional
            
            archivoTurnosEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
            json.dump(turnosGuardados, archivoTurnosEscribir, indent = 4, ensure_ascii = False)
            archivoTurnosEscribir.close()  

            """
            patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
            
            #seleccionar la fecha y verificar que este correcta
            while True:
                nuevaFecha = input("Ingrese la nueva fecha (DD/MM/AAAA): ")
                
                if re.match(patronFecha, nuevaFecha):
                    fecha_ingresada = datetime.strptime(nuevaFecha, "%d/%m/%Y")
                    #fecha actual
                    fecha_actual = datetime.now()

                    if fecha_ingresada > fecha_actual:
                        break
                    else:
                        print("La fecha ingresada es anterior a la fecha actual. Intente de nuevo.")
                else:
                    print("El formato o la fecha es incorrecta. Intente de nuevo")
                    """
                    
            nuevaFecha = ingresarFecha()
            turnoSeleccionado['fecha'] = nuevaFecha
            
            """
            archivoTurnosEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
            json.dump(turnosGuardados, archivoTurnosEscribir, indent = 4, ensure_ascii = False)
            archivoTurnosEscribir.close() 

            archivoLeerProfesionales = open(rutaArchivoProfesionalGuardados, "r", encoding = "utf-8")
            profesionalesGuardados = json.load(archivoLeerProfesionales)
            archivoLeerProfesionales.close()

            horarios = profesionalSeleccionado['horarioAtencion']
            horarioInicio = int(horarios[:2])
            horarioFin = int(horarios[8:10])

            horariosDisponibles = [f"{hora:02d}:00" for hora in range(horarioInicio, horarioFin)]

            for turno in turnosGuardados:
                if turno['fecha'] == nuevaFecha and turno['documentoIdentidadProfesional'] == turnoSeleccionado['documentoIdentidadProfesional']:
                    print(turno['fecha'])
                    if turno['horario'] in horariosDisponibles:
                        print(turno['horario'])
                        horariosDisponibles.remove(turno['horario'])

            # Mostrar horarios disponibles
            print("Horarios disponibles:")
            for i, horario in enumerate(horariosDisponibles):
                print(f"[{i}] {horario}")
            
            seleccion = int(input("Seleccione un nuevo horario: "))
            while seleccion < 0 or seleccion >= len(horariosDisponibles):
                seleccion = int(input("Seleccione una opción válida: "))"""

            
            nuevoHorario = seleccionarHorario(turnosGuardados, turnoSeleccionado, profesionalesGuardados)
            turnoSeleccionado['horario'] = nuevoHorario
            
            archivoTurnosEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
            json.dump(turnosGuardados, archivoTurnosEscribir, indent = 4, ensure_ascii = False)
            archivoTurnosEscribir.close()  
            
            print("Especialista modificado correctamente.")

        elif opcion == 4:
            nuevoMotivo = input("Ingrese el nuevo motivo: ")

            turnoSeleccionado['motivo'] = nuevoMotivo
            
            archivoTurnosEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
            json.dump(turnosGuardados, archivoTurnosEscribir, indent = 4, ensure_ascii = False)
            archivoTurnosEscribir.close()  
            
            print("Motivo modificado correctamente.")

        elif opcion == 0:
            # Salir del bucle
            break

        else:
            print("Opción no válida. Intente de nuevo.")
    
    print("--------------------------------------------------------------------------------------")
    print(f"Informacion del turno modificada con exito")
    print(f"Fecha: {turnoSeleccionado['fecha']}, Horario: {turnoSeleccionado['horario']}, Especialista DNI: {turnoSeleccionado['documentoIdentidadProfesional']}, Motivo: {turnoSeleccionado['motivo']}")
    print("--------------------------------------------------------------------------------------")


    return 


def cancelarTurnoCliente(rutaArchivoTurnosProgramados, rutaArchivoClientesGuardados):

    
    documentoIdentidadCliente = verificarDocumento(rutaArchivoClientesGuardados, True)
    if documentoIdentidadCliente == -1:
        return
    elif documentoIdentidadCliente == False:
        return
    
    
    fecha_actual = datetime.now()
    turnosCliente = []

    archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
    turnosGuardados = json.load(archivoTurnosLeer)
    archivoTurnosLeer.close()
    
    turnosCliente = [
    turno for turno in turnosGuardados 
    if turno['documentoIdentidadCliente'] == documentoIdentidadCliente 
    and turno["activo"] == True 
    and datetime.strptime(turno['fecha'], "%d/%m/%Y") >= fecha_actual
    ]

    if not turnosCliente:
        print("Este cliente no tiene turnos asignados.")
        return 

    # Mostrar los turnos del cliente
    print("Turnos del cliente:")
    for i, turno in enumerate(turnosCliente):
        print(f"[{i}] Fecha: {turno['fecha']}, Horario: {turno['horario']}, Especialista DNI: {turno['documentoIdentidadProfesional']}, Motivo: {turno['motivo']}")

        
    # Seleccionar turno por índice
    while True:
        try:
            indiceTurno = int(input("Seleccione el turno que desea modificar: "))
            
            if indiceTurno < 0:
                print("El indice no puede ser negativo. Por favor, intenta de nuevo.")
            elif indiceTurno >= len(turnosCliente):
                print(f"El indice debe estar entre 0 y {len(turnosCliente) - 1}. Por favor, intenta de nuevo.")
            else:
                break  # indice valido
        except ValueError:
            print("Entrada no valida. Por favor, ingrese un número.")

    turnoSeleccionado = turnosCliente[indiceTurno]
    indiceGeneralTurno = turnosGuardados.index(turnoSeleccionado)
    
    while True:
        try:
            confirmarEliminacion = input("¿Está seguro que desea eliminar el profesional? (y/n): ").lower()
            
            if confirmarEliminacion == "y":
                
                turnosGuardados[indiceGeneralTurno]["activo"] = False

                archivoEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
                json.dump(turnosGuardados, archivoEscribir, ensure_ascii=False, indent=4)
                archivoEscribir.close()

                print("-" * 50)
                print("Se ha cancelado el turno con éxito.")
                print("-" * 50)
                break  

            elif confirmarEliminacion == "n":
                print("-" * 50)
                print("Se ha elegido cancelar la operación.")
                print("-" * 50)
                break  
            
            else:
                print("Ha ingresado un valor incorrecto.")

        except Exception as e:
            print("Ocurrió un error durante el proceso:", e)
            print("Intente nuevamente.")

    return