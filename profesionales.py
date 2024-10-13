import re

#tomar informacion de un profesional nuevo
def informacionProfesionalNuevo(diccProfesionalesGuardados):
    documentoIdentidadProfesional = input("DNI del profesional: ")

    while documentoIdentidadProfesional in diccProfesionalesGuardados:
        print("El DNI del profesional ya se encuentra registrado.")
        decision = input("Ingrese: [1] Ingresar otro DNI, [2] Regresar al menu\n:")
        if decision == "1":
            documentoIdentidadProfesional = input("DNI del profesional: ")
        elif decision == "2":
            print("--------------------------------------------------------------------------------")
            print("Volviendo al menu...")
            print("--------------------------------------------------------------------------------")
            #terminar el flujo y volver al menu
            return
        else:
            print("Ha seleccionado una opcion incorrecta.")

    nombreCompleto = input("Nombre completo: ")
    genero = input("Genero: ")
    especializacion = input("Especializacion: ")

    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    
    #confirmar que la fecha sea correcta
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    
    domicilio = input("Domicilio: ")

    numeroTelefono = input("Numero de telefono: ")
    patronNumeroTel = "^\+?(\d{1,4})?[-.\s]?(\(?\d{1,4}\)?)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"

    #confirmar que el numero de telefono sea correcto
    while not re.match(patronNumeroTel, numeroTelefono):
        print("El formato o el numero es incorrecto.")
        numeroTelefono = input("Numero de telefono: ")


    horarioAtencion = input("Horario de atencion (HH:00 - HH:00): ")
    patronHorarioAtencion = "^(0[0-9]|1[0-9]|2[0-3]):00\s-\s(0[0-9]|1[0-9]|2[0-3]):00$"
    #confirmar que el numero de telefono sea correcto
    while not re.match(patronHorarioAtencion, horarioAtencion):
        print("El formato u hora es incorrecto.")
        horarioAtencion = input("Horario de atencion (HH:00 - HH:00): ")

    return documentoIdentidadProfesional, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion

#guardar la informacion de un profesional
def guardarInformacionProfesional(informacionProfesional,diccProfesionalesGuardados):
    documentoIdentidadProfesional, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion = informacionProfesional
    
    diccProfesionalesGuardados[documentoIdentidadProfesional] = {
        "nombreCompleto": nombreCompleto,
        "genero": genero,
        "especializacion": especializacion,
        "fechaNacimiento": fechaNacimiento,
        "domicilio": domicilio,
        "numeroTelefono" : numeroTelefono,
        "horarioAtencion": horarioAtencion,
        "activo" : True
    }
    print(f"Profesional {nombreCompleto} agregado con éxito!")

    return

#modificar informacion de un profesional ya creado
def modificarInformacionProfesional(diccProfesionalesGuardados):

    documentoIdentidadProfesional = input("DNI del profesional: ")
    while documentoIdentidadProfesional not in diccProfesionalesGuardados.keys():
        print("El DNI no se encuentra registrado.")

        decision = input("Ingrese: [1] Ingresar otro DNI, [2] Agregar un nuevo profesional, [3] Regresar al menu\n:")
        if decision == "1":
            documentoIdentidadProfesional = input("DNI del profesional: ")

        elif decision == "2":
            #agregar un nuevo profesional
            informacionProfesional = informacionProfesionalNuevo(diccProfesionalesGuardados)
            if informacionProfesional:
                guardarInformacionProfesional(informacionProfesional, diccProfesionalesGuardados)
            print("Nuevo profesional agregado exitosamente.")
            return 
        
        elif decision == "3":
            print("--------------------------------------------------------------------------------")
            print("Volviendo al menu...")
            print("--------------------------------------------------------------------------------")
            #terminar el flujo y volver al menu
            return
        
        else:
            print("Ha seleccionado una opcion incorrecta.")

    informacionActualProfesional = diccProfesionalesGuardados[documentoIdentidadProfesional]
    for k, v in informacionActualProfesional.items():
        print(f"{k}: {v}")
    
    nombreCompleto = input("Nombre completo: ")
    genero = input("Genero: ")
    especializacion = input("Especializacion: ")

    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    
    #confirmar que la fecha sea correcta
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    
    domicilio = input("Domicilio: ")

    numeroTelefono = input("Numero de telefono: ")
    patronNumeroTel = "^\+?(\d{1,4})?[-.\s]?(\(?\d{1,4}\)?)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    #confirmar que el numero de telefono sea correcto
    while not re.match(patronNumeroTel, numeroTelefono):
        print("El formato o el numero es incorrecto.")
        numeroTelefono = input("Numero de telefono: ")

    horarioAtencion = input("Horario de atencion (HH:00 - HH:00): ")
    patronHorarioAtencion = "^(0[0-9]|1[0-9]|2[0-3]):00\s-\s(0[0-9]|1[0-9]|2[0-3]):00$"
    #confirmar que el numero de telefono sea correcto
    while not re.match(patronHorarioAtencion, horarioAtencion):
        print("El formato u hora es incorrecto.")
        horarioAtencion = input("Horario de atencion (HH:00 - HH:00): ")

    return documentoIdentidadProfesional, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion

#eliminar profesional existente
def eliminarProfesional(diccProfesionalesGuardados):
    documentoIdentidadProfesional = input("DNI del profesional: ")
    while documentoIdentidadProfesional not in diccProfesionalesGuardados.keys():
        print("El DNI no se encuentra registrado en la lista de profesionales.")
        decision = input("Ingrese: [1] Ingresar otro DNI, [2] Regresar al menu\n:")
        if decision == "1":
            documentoIdentidadProfesional = input("DNI del profesional: ")
        elif decision == "2":
            print("--------------------------------------------------------------------------------")
            print("Volviendo al menu...")
            print("--------------------------------------------------------------------------------")
            #terminar el flujo y volver al menu
            return
        else:
            print("Ha seleccionado una opcion incorrecta.")


    print(f"DNI: {documentoIdentidadProfesional}\n Nombre:{diccProfesionalesGuardados[documentoIdentidadProfesional]['nombre']}")
    confirmarEliminacion = input("Esta seguro que desea eliminar el profesional (y/n): ")
    while confirmarEliminacion.lower != "y" or confirmarEliminacion.lower != "n":
        print("Ha ingresado un valor incorrecto.")
        confirmarEliminacion = input("Esta seguro que desea eliminar el profesional (y/n): ")
    if confirmarEliminacion.lower == "y":
        diccProfesionalesGuardados[documentoIdentidadProfesional]["activo"] = False
        print("Se ha eliminado el profesional con exito.")
    elif confirmarEliminacion.lower == "n":
        print("Se ha elegido cancelar la operacion.")
    
    return