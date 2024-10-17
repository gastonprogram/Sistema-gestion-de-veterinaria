import re
from datetime import datetime

def informacionTurnoCliente(diccClientesGuardados, listMascotasGuardadas, diccProfesionalesGuardados, listTurnosProgramados):


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
        - documentoIdentidadEspecialista (str): Número de DNI del especialista.
        - fecha (str): fecha del turno en formato DD/MM/AAAA
        - horarioSeleccionado (str): horario del turno
        - motivo(str): motivo de la consulta
    """
    

    #solicitar el DNI del cliente
    documentoIdentidadDueño = input("DNI del cliente: ")
    while documentoIdentidadDueño not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")

        if decision == "1":
            documentoIdentidadDueño = input("DNI del cliente: ")
        
        #terminar el flujo y volver al menu
        elif decision == "2":
            print("-" * 50)
            print("Volviendo al menu...")
            print("-" * 50)
            return
        
        else:
            print("Ha seleccionado una opcion incorrecta.")

    #buscar las mascotas del cliente
    mascotasCliente = [m for m in listMascotasGuardadas if m["documentoIdentidadDueño"] == documentoIdentidadDueño]

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

    print("------------------------------------------------------------------------------------------------------------------")
    print("Informacion especialistas:")
    for dni, profesional in diccProfesionalesGuardados.items():

        #verificar si el profesional esta activo
        if profesional["activo"] == True:

            #mostrar informacion clave de cada profesional para luego seleccionar a uno
            print(f"DNI: {dni}, Nombre: {profesional['nombreCompleto']}, Especialización: {profesional['especializacion']}, Horario de atencion: {profesional['horarioAtencion']}.")
    print("------------------------------------------------------------------------------------------------------------------")
    
    #seleccionar especialista
    documentoIdentidadEspecialista = input("Ingrese el DNI del especialista: ")
    while documentoIdentidadEspecialista not in diccProfesionalesGuardados.keys() or diccProfesionalesGuardados[documentoIdentidadEspecialista]["activo"] == False:
        print("El DNI del especialista no se encuentra registrado.")
        documentoIdentidadEspecialista = input("Ingrese el DNI del especialista: ")

    #obtener y separar el horario del profesional 
    horarios = diccProfesionalesGuardados[documentoIdentidadEspecialista]["horarioAtencion"]
    horarioInicio = int(horarios[:2])  
    horarioFinal = int(horarios[8:10])  

    #crear una lista con todos los horarios en formato HH:00 en el rango de atencion 
    horariosDisponibles = [f"{hora:02d}:00" for hora in range(horarioInicio, horarioFinal)]


    #seleccionar la fecha y verificar que este correcta
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
    for turno in listTurnosProgramados:
        if turno['fecha'] == fecha and turno['documentoIdentidadEspecialista'] == documentoIdentidadEspecialista:
            if turno['horario'] in horariosDisponibles:
                horariosDisponibles.remove(turno['horario'])

    #mostrar los horarios disponibles al usuario 
    print("Horarios disponibles:")
    for i, horario in enumerate(horariosDisponibles):
        print(f"[{i + 1}] {horario}")

    #seleccionar un horario disponible con opción numerica
    seleccion = int(input("Seleccione una opción de horario: "))
    while seleccion < 1 or seleccion > len(horariosDisponibles):
        seleccion = int(input("Seleccione una opción válida: "))

    #asignar el horario seleccionado
    horarioSeleccionado = horariosDisponibles[seleccion - 1]
            
        
    #ingresar el motivo del turno
    motivo = input("Motivo: ")

    return documentoIdentidadDueño, indiceMascotaGeneral, documentoIdentidadEspecialista, fecha, horarioSeleccionado, motivo

def añadirTurnoCliente(informacionTurno, listTurnosProgramados):
    #desempaquetar la informacion del turno
    documentoIdentidadDueño, indiceMascotaGeneral, documentoIdentidadEspecialista, fecha, horario, motivo = informacionTurno

    #agregar un turno a la lista con la informacion correspondiente
    listTurnosProgramados.append({
        "documentoIdentidadCliente": documentoIdentidadDueño,
        "indiceMascota": indiceMascotaGeneral,
        "documentoIdentidadEspecialista": documentoIdentidadEspecialista,
        "fecha": fecha,
        "horario": horario,
        "motivo": motivo,
        "activo" : True
        })
    
    print(f"Turno programado para el {fecha} a las {horario}.")

    return

def modificarTurnoCliente(listTurnosProgramados, diccClientesGuardados, diccProfesionalesGuardados):
    
    documentoIdentidadDueño = input("DNI del cliente: ")
    while documentoIdentidadDueño not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")

        if decision == "1":
            documentoIdentidadDueño = input("DNI del cliente: ")
        
        #terminar el flujo y volver al menu
        elif decision == "2":
            print("-" * 50)
            print("Volviendo al menu...")
            print("-" * 50)
            return
        
        else:
            print("Ha seleccionado una opcion incorrecta.")


    fecha_actual = datetime.now()

    # Filtrar los turnos que sean del cliente, que no esten cancelados y que sean posteriores a la fecha actual
    turnosCliente = [
    turno for turno in listTurnosProgramados 
    if turno['documentoIdentidadCliente'] == documentoIdentidadDueño 
    and turno["activo"] == True 
    and datetime.strptime(turno['fecha'], "%d/%m/%Y") >= fecha_actual
    ]

    if not turnosCliente:
        print("Este cliente no tiene turnos asignados.")
        return None

    # Mostrar los turnos del cliente
    print("Turnos del cliente:")
    for i, turno in enumerate(turnosCliente):
        print(f"[{i}] Fecha: {turno['fecha']}, Horario: {turno['horario']}, Especialista DNI: {turno['documentoIdentidadEspecialista']}, Motivo: {turno['motivo']}")

    # Seleccionar el turno a modificar
    indiceTurno = int(input("Seleccione el turno que desea modificar: "))
    while indiceTurno < 0 or indiceTurno >= len(turnosCliente):
        indiceTurno = int(input("Seleccione un índice válido: "))

    
    turnoSeleccionado = turnosCliente[indiceTurno]
    indiceGeneralTurno = listTurnosProgramados.index(turnoSeleccionado)

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
            
            patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
            
            #seleccionar la fecha y verificar que este correcta
            nuevaFecha = ""
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


            horarios = diccProfesionalesGuardados[turnoSeleccionado['documentoIdentidadEspecialista']]["horarioAtencion"]
            horarioInicio = int(horarios[:2])
            horarioFin = int(horarios[8:10])

            horariosDisponibles = [f"{hora:02d}:00" for hora in range(horarioInicio, horarioFin)]

            for turno in listTurnosProgramados:
                if turno['fecha'] == nuevaFecha and turno['documentoIdentidadEspecialista'] == turnoSeleccionado['documentoIdentidadEspecialista']:
                    print(turno['fecha'])
                    if turno['horario'] in horariosDisponibles:
                        print(turno['horario'])
                        horariosDisponibles.remove(turno['horario'])

            # Mostrar horarios disponibles
            print("Horarios disponibles:")
            for i, horario in enumerate(horariosDisponibles):
                print(f"[{i + 1}] {horario}")
            
            seleccion = int(input("Seleccione un nuevo horario: "))
            while seleccion < 1 or seleccion > len(horariosDisponibles):
                seleccion = int(input("Seleccione una opción válida: "))

            turnoSeleccionado['fecha'] = nuevaFecha
            turnoSeleccionado['horario'] = horariosDisponibles[seleccion - 1]
            print("Fecha y horario modificado correctamente.")

        elif opcion == 2:
            horarios = diccProfesionalesGuardados[turnoSeleccionado['documentoIdentidadEspecialista']]["horarioAtencion"]
            horarioInicio = int(horarios[:2])
            horarioFin = int(horarios[8:10])

            horariosDisponibles = [f"{hora:02d}:00" for hora in range(horarioInicio, horarioFin)]

            for turno in listTurnosProgramados:
                if turno['fecha'] == turnoSeleccionado['fecha'] and turno['documentoIdentidadEspecialista'] == turnoSeleccionado['documentoIdentidadEspecialista']:
                    if turno['horario'] in horariosDisponibles:
                        horariosDisponibles.remove(turno['horario'])

            # Mostrar horarios disponibles
            print("Horarios disponibles:")
            for i, horario in enumerate(horariosDisponibles):
                print(f"[{i + 1}] {horario}")
            
            seleccion = int(input("Seleccione un nuevo horario: "))
            while seleccion < 1 or seleccion > len(horariosDisponibles):
                seleccion = int(input("Seleccione una opción válida: "))

            turnoSeleccionado['horario'] = horariosDisponibles[seleccion - 1]
            print("Horario modificado correctamente.")

        elif opcion == 3:
            for dni, profesional in diccProfesionalesGuardados.items():
                if profesional["activo"]:
                    print(f"DNI: {dni}, Nombre: {profesional['nombreCompleto']}, Especialización: {profesional['especializacion']}, Horario: {profesional['horarioAtencion']}")

            nuevoEspecialista = input("Ingrese el DNI del nuevo especialista: ")
            turnoSeleccionado['documentoIdentidadEspecialista'] = nuevoEspecialista
            print("Especialista modificado correctamente.")

        elif opcion == 4:
            nuevoMotivo = input("Ingrese el nuevo motivo: ")
            turnoSeleccionado['motivo'] = nuevoMotivo
            print("Motivo modificado correctamente.")

        elif opcion == 0:
            # Salir del bucle
            break

        else:
            print("Opción no válida. Intente de nuevo.")
    
    print("Modificaciones finalizadas.")

    
    documentoIdentidadCliente = turnoSeleccionado['documentoIdentidadCliente']
    indiceMascota = turnoSeleccionado['indiceMascota']
    fechaFinal = turnoSeleccionado["fecha"]
    especialistaFinal = turnoSeleccionado["documentoIdentidadEspecialista"]
    horarioFinal = turnoSeleccionado["horario"]
    motivoFinal = turnoSeleccionado["motivo"]

    return indiceGeneralTurno, documentoIdentidadCliente, indiceMascota, fechaFinal, especialistaFinal, horarioFinal, motivoFinal

def guardarTurnoModificado(informacionTurnoModificado, listTurnosProgramados):
    indiceGeneralTurno, documentoIdentidadCliente, indiceMascota, fecha, especialista, horario, motivo = informacionTurnoModificado

    listTurnosProgramados[indiceGeneralTurno] = {
        "documentoIdentidadCliente": documentoIdentidadCliente,
        "indiceMascota": indiceMascota,
        "documentoIdentidadEspecialista": especialista,
        "fecha": fecha,
        "horario": horario,
        "motivo": motivo
    }

    print("--------------------------------------------------------------------------------------")
    print(f"Informacion del turno modificada con exito")
    print(f"Fecha: {fecha}, Horario: {horario}, Especialista DNI: {especialista}, Motivo: {motivo}")
    print("--------------------------------------------------------------------------------------")

    return

def cancelarTurnoCliente(listTurnosProgramados, diccClientesGuardados):

    documentoIdentidadCliente = input("DNI del cliente: ")
    while documentoIdentidadCliente not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
        if decision == "1":
            documentoIdentidadCliente = input("DNI del profesional: ")
        elif decision == "2":
            print("--------------------------------------------------------------------------------")
            print("Volviendo al menu...")
            print("--------------------------------------------------------------------------------")
            #terminar el flujo y volver al menu
            return
        else:
            print("Ha seleccionado una opcion incorrecta.")
    
    fecha_actual = datetime.now()

    # Filtrar los turnos que sean del cliente, que no esten cancelados y que sean posteriores a la fecha actual
    turnosCliente = [
    turno for turno in listTurnosProgramados 
    if turno['documentoIdentidadCliente'] == documentoIdentidadCliente 
    and turno["activo"] == True
    and datetime.strptime(turno['fecha'], "%d/%m/%Y") >= fecha_actual
    ]


    if not turnosCliente:
        print("Este cliente no tiene turnos asignados.")
        return None

    #mostrar los turnos del cliente
    print("Turnos del cliente:")
    for i, turno in enumerate(turnosCliente):
        print(f"[{i}] Fecha: {turno['fecha']}, Horario: {turno['horario']}, Especialista DNI: {turno['documentoIdentidadEspecialista']}, Motivo: {turno['motivo']}")

    #seleccionar el turno a cancelar
    indiceTurno = int(input("Seleccione el turno que desea cancelar: "))
    while indiceTurno < 0 or indiceTurno >= len(turnosCliente):
        indiceTurno = int(input("Seleccione un índice válido: "))

    turnoSeleccionado = turnosCliente[indiceTurno]
    indiceGeneralTurno = listTurnosProgramados.index(turnoSeleccionado)

    #confirmar si quieres cancelar el turno
    confirmarEliminacion = input("¿Está seguro que desea cancelar el turno (y/n)?: ").lower()
    while confirmarEliminacion not in ["y", "n"]:
        print("Valor incorrecto.")
        confirmarEliminacion = input("¿Está seguro que desea cancelar el turno (y/n)?: ").lower()

    if confirmarEliminacion == "y":
        listTurnosProgramados[indiceGeneralTurno]["activo"] = False
        print("Se ha cancelado el turno con éxito.")
    else:
        print("Operación cancelada.")