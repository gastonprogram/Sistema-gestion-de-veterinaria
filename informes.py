"""TURNOS POR PROFESIONAL"""
def desplegarTurnosPorProfesional(listTurnosProgramados, diccProfesionalesGuardados):
    for dni, profesional in diccProfesionalesGuardados.items():

        #verificar si el profesional esta activo
        if profesional["activo"] == True:
            #mostrar informacion clave de cada profesional para luego seleccionar a uno
            print(f"DNI: {dni}, Nombre: {profesional['nombreCompleto']}, Especialización: {profesional['especializacion']}.")
    
    documentoIdentidadProfesional = input("Ingrese el DNI del profesional para ver sus turnos: ")

    # Filtrar turnos por el especialista (DNI)
    turnosEspecialista = [turno for turno in listTurnosProgramados if turno['documentoIdentidadEspecialista'] == documentoIdentidadProfesional]
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
def desplegarTurnosPorMascota(listMascotasGuardadas, listTurnosProgramados):

    documentoIdentidadDueño = input("Ingrese el DNI del dueño para ver sus turnos: ")

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
        if indiceMascotaGeneral == turno["indiceMascota"]:
            print("-------------------------------------------------------------------------------------------------------------")
            print(f"Cliente DNI: {turno['documentoIdentidad']}, Mascota: {listMascotasGuardadas[indiceMascotaGeneral]['nombre']}, "
                            f"Fecha: {turno['fecha']}, Hora: {turno['horario']}, Motivo: {turno['motivo']}")
    return

def mostrarTurnosPorFecha(listTurnosProgramados, fechaInicio, fechaFin):
    print(f"Turnos entre {fechaInicio} y {fechaFin}:")
    for turno in listTurnosProgramados:
        if turno['fecha'] >= fechaInicio and turno['fecha'] <= fechaFin:
            print(f"Fecha: {turno['fecha']}, Horario: {turno['horario']}, Cliente DNI: {turno['documentoIdentidadCliente']}")

def mostrarTurnosPorFechaYHorarios(listTurnosProgramados, fecha, horarioInicio, horarioFin):
    print(f"Turnos para el {fecha} entre {horarioInicio} y {horarioFin}:")
    for turno in listTurnosProgramados:
        if turno['fecha'] == fecha:
            horaTurno = int(turno['horario'][:2])  # Obtener la hora del turno en formato HH
            if horarioInicio <= horaTurno < horarioFin:
                print(f"Horario: {turno['horario']}, Cliente DNI: {turno['documentoIdentidadCliente']}, Mascota Índice: {turno['indiceMascota']}, Especialista DNI: {turno['documentoIdentidadEspecialista']}, Motivo: {turno['motivo']}")

