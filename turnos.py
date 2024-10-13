import re

def informacionTurnoCliente(diccClientesGuardados, listMascotasGuardadas, diccProfesionalesGuardados, listTurnosProgramados):
    #solicitar el DNI del cliente
    documentoIdentidad = input("DNI del cliente: ")
    while documentoIdentidad not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        documentoIdentidad = input("DNI del cliente: ")
    
    #buscar las mascotas del cliente
    mascotasCliente = [m for m in listMascotasGuardadas if m["documentoIdentidadDueño"] == documentoIdentidad]

    #si no tiene ninguna terminar el flujo
    if not mascotasCliente:
        print("Este cliente no tiene mascotas registradas.")
        return None
    
    #si tiene mascotas, mostrarlas con su informacion clave e indice
    for i, mascota in enumerate(mascotasCliente):
        print(f"[{i}] Nombre: {mascota['nombre']}, Especie: {mascota['especie']}")

    #seleccionar la mascota del cliente
    indiceMascota = int(input("Seleccione la mascota: "))
    while indiceMascota > len(mascotasCliente) - 1 or indiceMascota < 0:
        indiceMascota = int(input("Seleccione la mascota: "))

    #buscar el indice real de la mascota dentro de la lista de mascotas
    mascotaSeleccionada = mascotasCliente[indiceMascota]
    indiceMascotaGeneral = listMascotasGuardadas.index(mascotaSeleccionada)


    for dni, profesional in diccProfesionalesGuardados.items():

        #verificar si el profesional esta activo
        if profesional["activo"] == True:

            #mostrar informacion clave de cada profesional para luego seleccionar a uno
            print(f"DNI: {dni}, Nombre: {profesional['nombreCompleto']}, Especialización: {profesional['especializacion']}, Horario de atencion: {profesional['horarioAtencion']}.")
    
    #seleccionar especialista
    documentoIdentidadEspecialista = input("Ingrese el DNI del especialista: ")

    #obtener y separar el horario del profesional 
    horarios = diccProfesionalesGuardados[documentoIdentidadEspecialista]["horarioAtencion"]
    horarioInicio = int(horarios[:2])  
    horarioFinal = int(horarios[8:10])  

    # Crear una lista con todos los horarios en formato HH:00 en del rango de atencion del especialista
    horariosDisponibles = [f"{hora:02d}:00" for hora in range(horarioInicio, horarioFinal)]


    #seleccionar la fecha
    fecha = input("Fecha (DD/MM/AAAA): ")
    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    while not re.match(patronFecha, fecha):
        print("El formato o la fecha es incorrecta.")
        fecha = input("Fecha (DD/MM/AAAA): ")


    # Filtrar los horarios que ya estan ocupados
    for turno in listTurnosProgramados:
        if turno['fecha'] == fecha and turno['documentoIdentidadEspecialista'] == documentoIdentidadEspecialista:
            if turno['horario'] in horariosDisponibles:
                horariosDisponibles.remove(turno['horario'])

    # Mostrar los horarios disponibles al usuario 
    print("Horarios disponibles:")
    for i, horario in enumerate(horariosDisponibles):
        print(f"[{i + 1}] {horario}")

    # Seleccionar un horario disponible con opción numerica
    seleccion = int(input("Seleccione una opción de horario: "))
    while seleccion < 1 or seleccion > len(horariosDisponibles):
        seleccion = int(input("Seleccione una opción válida: "))

    # Asignar el horario seleccionado
    horarioSeleccionado = horariosDisponibles[seleccion - 1]
            
        
    #ingresar el motivo del turno
    motivo = input("Motivo: ")

    return documentoIdentidad, indiceMascotaGeneral, documentoIdentidadEspecialista, fecha, horarioSeleccionado, motivo

def añadirTurnoCliente(informacionTurno, listTurnosProgramados):
    #desempaquetar la informacion del turno
    documentoIdentidad, indiceMascotaGeneral, documentoIdentidadEspecialista, fecha, horario, motivo = informacionTurno

    #agregar un turno a la lista con la informacion correspondiente
    listTurnosProgramados.append({
        "documentoIdentidadCliente": documentoIdentidad,
        "indiceMascota": indiceMascotaGeneral,
        "documentoIdentidadEspecialista": documentoIdentidadEspecialista,
        "fecha": fecha,
        "horario": horario,
        "motivo": motivo
        })
    
    print(f"Turno programado para el {fecha} a las {horario}.")

    return