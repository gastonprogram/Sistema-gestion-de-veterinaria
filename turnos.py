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

    #guardar el horario de atenecion del profesional elegido y mostrarlo
    horarios = diccProfesionalesGuardados[documentoIdentidadEspecialista]["horarioAtencion"]
    horarioInicio = horarios[:2]
    horarioFinal = horarios[8:10]
    print(f"Horario de atencion entre {horarioInicio} - {horarioFinal}")

    #seleccionar la fecha
    fecha = input("Fecha (DD/MM/AAAA): ")
    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    #confirmar que la fecha sea correcta
    while not re.match(patronFecha, fecha):
        print("El formato o la fecha es incorrecta.")
        fecha = input("Fecha de Nacimiento (DD/MM/AAAA): ")

    #seleccionar un horario dentro del rango de atencion
    horario = input("Horario (HH:00): ")
    horariosInicio = int(horario[:2])
    horariosfinal = int(horario[3:])
    patronHorario = "^(0[0-9]|1[0-9]|2[0-3]):00$"


    # CORREGIRRRRRRRRRRRRRRRRRRRRRRRR
    while (horariosInicio < int(horarioInicio) or horariosfinal >= int(horarioFinal)) or not re.match(patronHorario, horario):
        print("Ingrese el horario del turno dentro del rango y patron definido.")
        horario = input("Horario (HH:00): ")
        horariosInicio = int(horario[:2])
        horariosfinal = int(horario[3:])


    #verificar si ese horario esta disponible
    for turno in listTurnosProgramados:
        print(turno)
        print("--------------------------")
        #si ese horario esta ocupado terminar el flujo
        while turno['fecha'] == fecha and turno['horario'] == horario and turno['documentoIdentidadEspecialista'] == documentoIdentidadEspecialista:
            
            print("----------------------")
            print("El turno esta ocupado.")
            print("----------------------")

            
            decision = input("Ingrese: [1] Ingresar otra fecha y hora, [2] Regresar al menu\n:")
            if decision == "1":

                #seleccionar la fecha
                fecha = input("Fecha (DD/MM/AAAA): ")
                patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
                #confirmar que la fecha sea correcta
                while not re.match(patronFecha, fecha):
                    print("El formato o la fecha es incorrecta.")
                    fecha = input("Fecha de Nacimiento (DD/MM/AAAA): ")

                #seleccionar un horario dentro del rango de atencion
                horario = input("Horario (HH:00): ")
                horariosInicio = int(horario[:2])
                horariosfinal = int(horario[3:])
                patronHorario = "^(0[0-9]|1[0-9]|2[0-3]):00$"


            elif decision == "2":
                print("--------------------------------------------------------------------------------")
                print("Volviendo al menu...")
                print("--------------------------------------------------------------------------------")
                #terminar el flujo y volver al menu
                return
            
            
        
    #ingresar el motivo del turno
    motivo = input("Motivo: ")

    return documentoIdentidad, indiceMascotaGeneral, documentoIdentidadEspecialista, fecha, horario, motivo

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