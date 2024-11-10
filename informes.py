import json
from utiles import *


"""TURNOS POR PROFESIONAL"""
def desplegarTurnosPorProfesional(rutaArchivoTurnosProgramados, rutaArchivoProfesionalGuardados):

    """
    Muestra los turnos asignados a un profesional en especifico


    PARAMETROS:
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    diccProfesionalesGuardados(dict): diccionario que contiene diccionarios con informacion de profesionales
    


    SALIDA:
    None: La función no retorna ningún valor. """

    try:
        
        archivoProfesionalesLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
        profesionalesGuardados = json.load(archivoProfesionalesLeer)
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        return
                    
    finally:
        try:
            archivoProfesionalesLeer.close()
        except:
            pass

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
    documentoIdentidadProfesional = profesionalesActivos[indiceProfesional][0]


    try:
        archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
        turnosProgramados = json.load(archivoTurnosLeer)
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        return
                    
    finally:
        try:
            archivoTurnosLeer.close()
        except:
            pass


    # Filtrar turnos por el especialista (DNI)
    turnosProfesional = [turno for turno in turnosProgramados if turno['documentoIdentidadEspecialista'] == documentoIdentidadProfesional and turno["activo"] == True]
    if not turnosProfesional:
        print(f"No se encontraron turnos para el profesional con DNI {documentoIdentidadProfesional}.")
        return
    else:
        print(f"Turnos para el profesional con DNI {documentoIdentidadProfesional}:")
        for cont, turno in enumerate(turnosProfesional, 1):
            print(f"Turno : {cont}")
            print("-------------------------------------------------------------------------------------------------------------")
            print(f"Cliente DNI: {turno['documentoIdentidadCliente']}, Mascota: {turno['indiceMascota']}, "
                f"Fecha: {turno['fecha']}, Hora: {turno['horario']}, Motivo: {turno['motivo']}")
    return

"""TURNOS POR MASCOTA"""
def desplegarTurnosPorMascota(rutaArchivoMascotasGuardados, rutaArchivoTurnosProgramados, rutaArchivoClientesGuardados):



    """
    Muestra los turnos asignados a una mascota en especifico

    PARAMETROS:
    listMascotasGuardadas(list): lista que contiene diccionarios con informacion de mascotas
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    diccClientesGuardados(dict): diccionario que contiene diccionarios con informacion de clientes
    

    SALIDA:
    None: La función no retorna ningún valor. """


    documentoIdentidadDueño = verificarDocumento(rutaArchivoClientesGuardados, True)
    if documentoIdentidadDueño == -1:
        return
    elif documentoIdentidadDueño == False:
        return
    
    
    try:
        
        archivoMascotasLeer = open(rutaArchivoMascotasGuardados, "r", encoding = "utf-8")
        mascotasGuardadas = json.load(archivoMascotasLeer)
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        return
                    
    finally:
        try:
            archivoMascotasLeer.close()
        except:
            pass
    
    
    mascotasCliente = [m for m in mascotasGuardadas if m["documentoIdentidadDueño"] == documentoIdentidadDueño]


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
    
    try:
        archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
        turnosProgramados = json.load(archivoTurnosLeer)
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        return
                    
    finally:
        try:
            archivoTurnosLeer.close()
        except:
            pass
    

    for turno in turnosProgramados:
        if turno["activo"] == True:
            if indiceMascotaGeneral == turno["indiceMascota"]:
                print("-------------------------------------------------------------------------------------------------------------")
                print(f"Cliente DNI: {turno['documentoIdentidadCliente']}, Mascota: {mascotasGuardadas[indiceMascotaGeneral]['nombre']}, "
                                f"Fecha: {turno['fecha']}, Hora: {turno['horario']}, Motivo: {turno['motivo']}")
    return

def mostrarTurnosPorFecha(rutaArchivoTurnosProgramados, fechaInicio, fechaFin):

    """
    Muestra los turnos dentro de un rango de fechas especifico

    PARAMETROS:
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    fechaInicio(str): fecha de inicio en formato DD/MM/AAAA
    fechaFin(str): fecha de fin en formato DD/MM/AAAA
    

    SALIDA:
    None: La función no retorna ningún valor. """

    try:
        archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
        turnosProgramados = json.load(archivoTurnosLeer)
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        return
                    
    finally:
        try:
            archivoTurnosLeer.close()
        except:
            pass

    print(f"Turnos entre {fechaInicio} y {fechaFin}:")
    
    fechaInicio = datetime.strptime(fechaInicio, "%d/%m/%Y")
    fechaFin = datetime.strptime(fechaFin, "%d/%m/%Y")
    
    for turno in turnosProgramados:
        if turno["activo"] == True:
            fechaTurno = datetime.strptime(turno["fecha"], "%d/%m/%Y")
            if fechaInicio <= fechaTurno <= fechaFin:
                print(f"\nCliente (DNI): {turno['documentoIdentidadCliente']}")
                print(f"Mascota (Índice): {turno['indiceMascota']}  |  Profesional (DNI): {turno['documentoIdentidadProfesional']}")
                print(f"Fecha: {turno['fecha']}  |  Horario: {turno['horario']}  |  Motivo: {turno['motivo']}  |  Estado: {'Activo' if turno['activo'] else 'Cancelado'}")
                print("-" * 60)
                
    return

def mostrarTurnosPorFechaYHorarios(rutaArchivoTurnosProgramados, fecha, horarioInicio, horarioFin):

    """
    Muestra los turnos en una fecha en especifico dentro de un rango de horarios

    PARAMETROS:
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    fecha(str): fecha de fin en formato DD/MM/AAAA
    horarioInicio(str): horario de inicio en formato HH:00
    horarioFin(str): horario de fin en formato HH:00
    

    SALIDA:
    None: La función no retorna ningún valor. """
    
    try:
        
        archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
        turnosProgramados = json.load(archivoTurnosLeer)
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        return
                    
    finally:
        try:
            archivoTurnosLeer.close()
        except:
            pass


    print(f"Turnos para el {fecha} entre {horarioInicio} y {horarioFin}:")
    for turno in turnosProgramados:
        if turno["activo"] == True:
            if turno['fecha'] == fecha:
                #obtener la hora del turno en formato HH
                horaTurno = int(turno['horario'][:2]) 
                if int(horarioInicio) <= horaTurno < int(horarioFin):
                    print(f"\nCliente (DNI): {turno['documentoIdentidadCliente']}")
                    print(f"Mascota (Índice): {turno['indiceMascota']}  |  Profesional (DNI): {turno['documentoIdentidadProfesional']}")
                    print(f"Fecha: {turno['fecha']}  |  Horario: {turno['horario']}  |  Motivo: {turno['motivo']}  |  Estado: {'Activo' if turno['activo'] else 'Cancelado'}")
                    print("-" * 60)
    return