import re
from datetime import datetime

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
        - documentoIdentidadEspecialista (str): Número de DNI del especialista.
        - fecha (str): fecha del turno en formato DD/MM/AAAA
        - horarioSeleccionado (str): horario del turno
        - motivo(str): motivo de la consulta
    """
    
    archivoClientesLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
    
    documentoIdentidadDueño = input("DNI del dueño: ")
    while True:
        encontrado = False

        for registro in archivoClientesLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]

            # Si el DNI está registrado
            if documentoIdentidadDueño == documentoIdentidadRegistro:
                encontrado = True
                break

        # Verificar si no se encontró el DNI después de recorrer el archivo
        if not encontrado:
            print("El DNI no se encuentra registrado.")
            while True:
                decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                
                if decision == "1":
                    documentoIdentidadDueño = input("DNI del dueño: ")
                    archivoClientesLeer.seek(0)  # Volver al inicio del archivo
                    break
                elif decision == "2":
                    print("-" * 50)
                    print("Volviendo al menu...")
                    print("-" * 50)
                    return
                else:
                    print("Ha seleccionado una opcion incorrecta.")
        else:
            # se encontro dni
            break

    
    archivoMascotasLeer = open(rutaArchivoMascotasGuardados, "r", encoding="utf-8")
    mascotasCliente = []

    for registro in archivoMascotasLeer:
        campos = registro.strip().split(";")
        if campos[1] == documentoIdentidadDueño:
            mascota = {
                "pk": int(campos[0]),
                "documentoIdentidadDueño": campos[1],
                "nombre": campos[2],
                "especie": campos[3],
                "razaAnimal": campos[4],
                "fechaNacimiento": campos[5],
                "pesoKilogramos": float(campos[6])
            }
            mascotasCliente.append(mascota)
    
    archivoMascotasLeer.close()

    if not mascotasCliente:
        print("Este cliente no tiene mascotas registradas.")
        return None
    
    for i, mascota in enumerate(mascotasCliente):
        print(f"[{i}] Nombre: {mascota['nombre']}, Especie: {mascota['especie']}")

    indiceMascotaCliente = int(input("Seleccione la mascota: "))
    while indiceMascotaCliente > len(mascotasCliente) - 1 or indiceMascotaCliente < 0:
        indiceMascotaCliente = int(input("Seleccione la mascota: "))

    mascotaSeleccionada = mascotasCliente[indiceMascotaCliente]


    archivoProfesionalesLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
    
    print("------------------------------------------------------------------------------------------------------------------")
    print("Informacion especialistas:")
    for linea in archivoProfesionalesLeer:
        campos = linea.strip().split(";")
        #verificar si el profesional esta activo
        if campos[8] == "True":
            
            #mostrar informacion clave de cada profesional para luego seleccionar a uno
            print(f"DNI: {campos[0]}, Nombre: {campos[1]}, Especialización: {campos[3]}, Horario de atencion: {campos[7]}.")
    print("------------------------------------------------------------------------------------------------------------------")
          


    #seleccionar especialista
    archivoProfesionalesLeer.seek(0)
    documentoIdentidadEspecialista = input("Ingrese el DNI del especialista: ")
    while True:
        encontrado = False  # Variable de control para salir del while si se encuentra el especialista

        for linea in archivoProfesionalesLeer:
            campos = linea.strip().split(";")
            if campos[0] == documentoIdentidadEspecialista and campos[8] == "True":
                encontrado = True  
                horarios = campos[7]
                break  

        if encontrado:
            break
        
        print("El DNI del especialista no se encuentra registrado.")
        documentoIdentidadEspecialista = input("Ingrese el DNI del especialista: ")
        archivoProfesionalesLeer.seek(0)

    archivoProfesionalesLeer.close()

    #obtener y separar el horario del profesional 
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
    archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
    for turno in archivoTurnosLeer:
        camposTurnos = turno.strip().split(";")
        if camposTurnos[4] == fecha and camposTurnos[3] == documentoIdentidadEspecialista:
            if camposTurnos[5] in horariosDisponibles:
                horariosDisponibles.remove(camposTurnos[5])

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

    return documentoIdentidadDueño, mascotaSeleccionada["pk"], documentoIdentidadEspecialista, fecha, horarioSeleccionado, motivo

def añadirTurnoCliente(informacionTurno, rutaArchivoTurnosProgramados):
    #desempaquetar la informacion del turno
    documentoIdentidadDueño, indiceMascotaSeleccionada, documentoIdentidadEspecialista, fecha, horario, motivo = informacionTurno

    ultimoID = -1
    archivoleer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
    for linea in archivoleer:
        ultimoID = int(linea.strip().split(";")[0])
    nuevoID = ultimoID + 1 if ultimoID >= 0 else 0
    archivoleer.close()

    archivoAñadir = open(rutaArchivoTurnosProgramados, "a", encoding="utf-8")
    archivoAñadir.write(f"{nuevoID};{documentoIdentidadDueño};{indiceMascotaSeleccionada};{documentoIdentidadEspecialista};{fecha};{horario};{motivo};{True}\n")
    archivoAñadir.close()

    print(f"Turno agregado con éxito!")
    return

def modificarTurnoCliente(rutaArchivoTurnosProgramados, rutaArchivoClientesGuardados, rutaArchivoProfesionalGuardados):
    
    
    archivoClientesLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
    
    documentoIdentidadDueño = input("DNI del dueño: ")
    while True:
        encontrado = False

        for registro in archivoClientesLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]

            # Si el DNI está registrado
            if documentoIdentidadDueño == documentoIdentidadRegistro:
                encontrado = True
                break

        # Verificar si no se encontró el DNI después de recorrer el archivo
        if not encontrado:
            print("El DNI no se encuentra registrado.")
            while True:
                decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                
                if decision == "1":
                    documentoIdentidadDueño = input("DNI del dueño: ")
                    archivoClientesLeer.seek(0)  # Volver al inicio del archivo
                    break
                elif decision == "2":
                    print("-" * 50)
                    print("Volviendo al menu...")
                    print("-" * 50)
                    return
                else:
                    print("Ha seleccionado una opcion incorrecta.")
        else:
            # se encontro dni
            break




    # Filtrar los turnos que sean del cliente, que no esten cancelados y que sean posteriores a la fecha actual

    fecha_actual = datetime.now()
    turnosCliente = []

    archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
    for linea in archivoTurnosLeer:
        campos = linea.strip().split(";")
        turno = {
            "pk": campos[0],
            "documentoIdentidadCliente": campos[1],
            "indiceMascota": campos[2],
            "documentoIdentidadEspecialista": campos[3],
            "fecha": campos[4],
            "horario": campos[5],
            "motivo": campos[6],
            "activo": campos[7] == "True"
        }

        if (
            turno["documentoIdentidadCliente"] == documentoIdentidadDueño and
            turno["activo"] and
            datetime.strptime(turno["fecha"], "%d/%m/%Y") >= fecha_actual
        ):
            turnosCliente.append(turno)

    archivoTurnosLeer.close()


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


    #fijar la informacion en caso de que no se modifique luego
    indiceGeneralTurno = turnoSeleccionado["pk"]
    documentoIdentidadCliente = turnoSeleccionado["documentoIdentidadCliente"]
    indiceMascota = turnoSeleccionado["indiceMascota"]
    fechaFinal = turnoSeleccionado["fecha"]
    especialistaFinal = turnoSeleccionado["documentoIdentidadEspecialista"]
    horarioFinal = turnoSeleccionado["horario"]
    motivoFinal = ["motivo"]

    

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

            archivoProfesionalesLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
            for linea in archivoProfesionalesLeer:
                campos = linea.strip().split(";")
                if campos[0] == turnoSeleccionado['documentoIdentidadEspecialista']:
                    horarios = campos[7]
            archivoProfesionalesLeer.close()


            horarioInicio = int(horarios[:2])
            horarioFin = int(horarios[8:10])

            horariosDisponibles = [f"{hora:02d}:00" for hora in range(horarioInicio, horarioFin)]

            
            #filtrar los horarios que ya estan ocupados
            archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
            for turno in archivoTurnosLeer:
                camposTurnos = turno.strip().split(";")
                if camposTurnos[4] == nuevaFecha and camposTurnos[3] == turnoSeleccionado['documentoIdentidadEspecialista']:
                    if camposTurnos[5] in horariosDisponibles:
                        horariosDisponibles.remove(camposTurnos[5])

            # Mostrar horarios disponibles
            print("Horarios disponibles:")
            for i, horario in enumerate(horariosDisponibles):
                print(f"[{i}] {horario}")
            
            seleccion = int(input("Seleccione un nuevo horario: "))
            while seleccion < 0 or seleccion > len(horariosDisponibles) - 1:
                seleccion = int(input("Seleccione una opción válida: "))



            #
            #      CCOOORREGIRRRR QUE NO GUARDE AL INSTANTE
            #
            fechaFinal = nuevaFecha
            horarioFinal = horariosDisponibles[seleccion]
            print("Fecha y horario modificado correctamente.")

        elif opcion == 2:

            archivoProfesionalesLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
            for linea in archivoProfesionalesLeer:
                campos = linea.strip().split(";")
                if campos[0] == turnoSeleccionado['documentoIdentidadEspecialista']:
                    horarios = campos[7]
            archivoProfesionalesLeer.close()

            horarioInicio = int(horarios[:2])
            horarioFin = int(horarios[8:10])
            horariosDisponibles = [f"{hora:02d}:00" for hora in range(horarioInicio, horarioFin)]

            #filtrar los horarios que ya estan ocupados
            archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
            for turno in archivoTurnosLeer:
                camposTurnos = turno.strip().split(";")
                if camposTurnos[4] == nuevaFecha and camposTurnos[3] == turnoSeleccionado['documentoIdentidadEspecialista']:
                    if camposTurnos[5] in horariosDisponibles:
                        horariosDisponibles.remove(camposTurnos[5])

            # Mostrar horarios disponibles
            print("Horarios disponibles:")
            for i, horario in enumerate(horariosDisponibles):
                print(f"[{i}] {horario}")
            
            seleccion = int(input("Seleccione un nuevo horario: "))
            while seleccion < 1 or seleccion > len(horariosDisponibles):
                seleccion = int(input("Seleccione una opción válida: "))

            #
            #      CCOOORREGIRRRR QUE NO GUARDE AL INSTANTE
            #
            horarioFinal = horariosDisponibles[seleccion]

            print("Horario modificado correctamente.")

        elif opcion == 3:


                    
            archivoProfesionalesLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
            
            print("------------------------------------------------------------------------------------------------------------------")
            print("Informacion especialistas:")
            for linea in archivoProfesionalesLeer:
                campos = linea.strip().split(";")
                #verificar si el profesional esta activo
                if campos[8] == "True":
                    
                    #mostrar informacion clave de cada profesional para luego seleccionar a uno
                    print(f"DNI: {campos[0]}, Nombre: {campos[1]}, Especialización: {campos[3]}, Horario de atencion: {campos[7]}.")
            print("------------------------------------------------------------------------------------------------------------------")
                


            #seleccionar especialista
            archivoProfesionalesLeer.seek(0)
            nuevoEspecialista = input("Ingrese el DNI del nuevo especialista: ")
            while True:
                encontrado = False  # Variable de control para salir del while si se encuentra el especialista

                for linea in archivoProfesionalesLeer:
                    campos = linea.strip().split(";")
                    if campos[0] == nuevoEspecialista and campos[8] == "True":
                        encontrado = True  
                        horarios = campos[7]
                        break  

                if encontrado:
                    break
                
                print("El DNI del especialista no se encuentra registrado.")
                nuevoEspecialista = input("Ingrese el DNI del nuevo especialista: ")
                archivoProfesionalesLeer.seek(0)

            archivoProfesionalesLeer.close()


            #
            #       CORREGIRRRRRRRRRRRRRR HAY QUE CAMBIAR FECHA Y TAMBIEN HORARIO
            #
            especialistaFinal = nuevoEspecialista

            print("Especialista modificado correctamente.")

        elif opcion == 4:
            nuevoMotivo = input("Ingrese el nuevo motivo: ")



            #
            #       CORREGIRRRRRRRRRRRRRR
            #
            motivoFinal = nuevoMotivo
            print("Motivo modificado correctamente.")

        elif opcion == 0:
            # Salir del bucle
            break

        else:
            print("Opción no válida. Intente de nuevo.")
    
    print("Modificaciones finalizadas.")


    return indiceGeneralTurno, documentoIdentidadCliente, indiceMascota, fechaFinal, especialistaFinal, horarioFinal, motivoFinal

def guardarTurnoModificado(informacionTurnoModificado, rutaArchivoTurnosProgramados):
    indiceGeneralTurno, documentoIdentidadCliente, indiceMascota, fecha, especialista, horario, motivo = informacionTurnoModificado

    archivoTurnosLeer = open(rutaArchivoTurnosProgramados, "r", encoding="utf-8")
    lineas = archivoTurnosLeer.readlines()
    archivoTurnosLeer.close()

    #reescribir el archivo con la información modificada
    archivoTurnosEscribir = open(rutaArchivoTurnosProgramados, "w", encoding="utf-8")
    for linea in lineas:
        campos = linea.strip().split(";")
        if indiceGeneralTurno == campos[0]:
            archivoTurnosEscribir.write(f"{indiceGeneralTurno};{documentoIdentidadCliente};{indiceMascota};{especialista};{fecha};{horario};{motivo};{True}\n")
        else:
            archivoTurnosEscribir.write(linea)
    archivoTurnosEscribir.close()
    

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