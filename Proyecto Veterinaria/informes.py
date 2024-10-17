"""TURNOS POR PROFESIONAL"""
def desplegarTurnosPorProfesional(listTurnosProgramados, diccProfesionalesGuardados):

    """
    Muestra los turnos asignados a un profesional en especifico


    PARAMETROS:
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    diccProfesionalesGuardados(dict): diccionario que contiene diccionarios con informacion de profesionales
    


    SALIDA:
    None: La función no retorna ningún valor. """


    for dni, profesional in diccProfesionalesGuardados.items():

        #verificar si el profesional esta activo y mostrar informacion clave
        if profesional["activo"] == True:
            print(f"DNI: {dni}, Nombre: {profesional['nombreCompleto']}, Especialización: {profesional['especializacion']}.")
    
    documentoIdentidadProfesional = input("Ingrese el DNI del profesional para ver sus turnos: ")
    while documentoIdentidadProfesional not in diccProfesionalesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
        if decision == "1":
            documentoIdentidadProfesional = input("Ingrese el DNI del profesional para ver sus turnos: ")
        #terminar el flujo y volver al menu
        elif decision == "2":
            print("-" * 50)
            print("Volviendo al menu...")
            print("-" * 50)
            return
        else:
            print("Ha seleccionado una opcion incorrecta.")

    # Filtrar turnos por el especialista (DNI)
    turnosEspecialista = [turno for turno in listTurnosProgramados if turno['documentoIdentidadEspecialista'] == documentoIdentidadProfesional and turno["activo"] == True]
    if not turnosEspecialista:
        print(f"No se encontraron turnos para el profesional con DNI {documentoIdentidadProfesional}.")
        return
    else:
        print(f"Turnos para el profesional con DNI {documentoIdentidadProfesional}:")
        for cont, turno in enumerate(turnosEspecialista, 1):
            print(f"Turno : {cont}")
            print("-------------------------------------------------------------------------------------------------------------")
            print(f"Cliente DNI: {turno['documentoIdentidadCliente']}, Mascota: {turno['indiceMascota']}, "
                f"Fecha: {turno['fecha']}, Hora: {turno['horario']}, Motivo: {turno['motivo']}")
    return

"""TURNOS POR MASCOTA"""
def desplegarTurnosPorMascota(listMascotasGuardadas, listTurnosProgramados, diccClientesGuardados):



    """
    Muestra los turnos asignados a una mascota en especifico

    PARAMETROS:
    listMascotasGuardadas(list): lista que contiene diccionarios con informacion de mascotas
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    diccClientesGuardados(dict): diccionario que contiene diccionarios con informacion de clientes
    

    SALIDA:
    None: La función no retorna ningún valor. """


    documentoIdentidadDueño = input("Ingrese el DNI del dueño para ver sus turnos: ")
    while documentoIdentidadDueño not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
        if decision == "1":
            documentoIdentidadDueño = input("Ingrese el DNI del dueño para ver sus turnos: ")
        #terminar el flujo y volver al menu
        elif decision == "2":
            print("--------------------------------------------------------------------------------")
            print("Volviendo al menu...")
            print("--------------------------------------------------------------------------------")
            return
        else:
            print("Opción no válida.")
            print("="*50)

    # Filtrar mascota por el dueño (DNI)
    mascotasCliente = [mascota for mascota in listMascotasGuardadas if mascota['documentoIdentidadDueño'] == documentoIdentidadDueño]

    if not mascotasCliente:
        print("Este cliente no tiene mascotas registradas.")
        return
                
    for i, mascota in enumerate(mascotasCliente):
        print(f"[{i}] Nombre: {mascota['nombre']}, Tipo: {mascota['especie']}")

    indiceMascotaCliente = int(input("Seleccione la mascota: "))
    while indiceMascotaCliente > len(mascotasCliente) - 1 or indiceMascotaCliente < 0:
        indiceMascotaCliente = int(input("Seleccione la mascota: "))

    mascotaSeleccionada = mascotasCliente[indiceMascotaCliente]
    indiceMascotaGeneral = listMascotasGuardadas.index(mascotaSeleccionada)

    for turno in listTurnosProgramados:
        if turno["activo"] == True:
            if indiceMascotaGeneral == turno["indiceMascota"]:
                print("-------------------------------------------------------------------------------------------------------------")
                print(f"Cliente DNI: {turno['documentoIdentidadCliente']}, Mascota: {listMascotasGuardadas[indiceMascotaGeneral]['nombre']}, "
                                f"Fecha: {turno['fecha']}, Hora: {turno['horario']}, Motivo: {turno['motivo']}")
    return

def mostrarTurnosPorFecha(listTurnosProgramados, fechaInicio, fechaFin):

    """
    Muestra los turnos dentro de un rango de fechas especifico

    PARAMETROS:
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    fechaInicio(str): fecha de inicio en formato DD/MM/AAAA
    fechaFin(str): fecha de fin en formato DD/MM/AAAA
    

    SALIDA:
    None: La función no retorna ningún valor. """



    print(f"Turnos entre {fechaInicio} y {fechaFin}:")
    for turno in listTurnosProgramados:
        if turno["activo"] == True:
            if turno['fecha'] >= fechaInicio and turno['fecha'] <= fechaFin:
                print(f"Fecha: {turno['fecha']}, Horario: {turno['horario']}, Cliente DNI: {turno['documentoIdentidadCliente']}")
    return

def mostrarTurnosPorFechaYHorarios(listTurnosProgramados, fecha, horarioInicio, horarioFin):

    """
    Muestra los turnos en una fecha en especifico dentro de un rango de horarios

    PARAMETROS:
    listTurnosProgramados(list): lista que contiene diccionarios con informacion de turnos
    fecha(str): fecha de fin en formato DD/MM/AAAA
    horarioInicio(str): horario de inicio en formato HH:00
    horarioFin(str): horario de fin en formato HH:00
    

    SALIDA:
    None: La función no retorna ningún valor. """

    print(f"Turnos para el {fecha} entre {horarioInicio} y {horarioFin}:")
    for turno in listTurnosProgramados:
        if turno["activo"] == True:
            if turno['fecha'] == fecha:
                #obtener la hora del turno en formato HH
                horaTurno = int(turno['horario'][:2]) 
                if horarioInicio <= horaTurno < horarioFin:
                    print(f"Horario: {turno['horario']}, Cliente DNI: {turno['documentoIdentidadCliente']}, Mascota Índice: {turno['indiceMascota']}, Especialista DNI: {turno['documentoIdentidadEspecialista']}, Motivo: {turno['motivo']}")

    return