import re

#tomar informacion sobre un cliente nuevo
def informacionClienteNuevo(diccClientesGuardados):

    #solicitar informacion 
    documentoIdentidadCliente = input("DNI del cliente: ")

    while documentoIdentidadCliente in diccClientesGuardados:
        print("El DNI ya se encuentra registrado.")
        decision = input("Ingrese: [1] Ingresar otro DNI, [2] Regresar al menu.")
        if decision == "1":
            documentoIdentidadCliente = input("DNI del cliente: ")
        elif decision == "2":
            print("--------------------------------------------------------------------------------")
            print("Volviendo al menu...")
            print("--------------------------------------------------------------------------------")
            #terminar el flujo y volver al menu
            return
            

    nombreCompleto = input("Nombre completo: ")
    genero = input("Genero: ")

    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    
    #confirmar que la fecha sea correcta
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")

    numeroTelefono = input("Numero de telefono: ")
    patronNumeroTel = "^\+?(\d{1,4})?[-.\s]?(\(?\d{1,4}\)?)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"

    #confirmar que el numero de telefono sea correcto
    while not re.match(patronNumeroTel, numeroTelefono):
        print("El formato o el numero es incorrecto.")
        numeroTelefono = input("Numero de telefono: ")


    domicilio = input("Domicilio: ")
    return documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio

#guardar informacion cliente
def guardarCliente(informacionCliente, diccClientesGuardados):
    documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio = informacionCliente
    diccClientesGuardados[documentoIdentidadCliente] = {
        "nombreCompleto": nombreCompleto,
        "genero": genero,
        "fechaNacimiento": fechaNacimiento,
        "numeroTelefono" : numeroTelefono,
        "domicilio": domicilio,
    }
    return

#modificar cliente existente
def modificarInformacionCliente(diccClientesGuardados):

    #solicitar dni del cliente a modificar
    documentoIdentidadCliente = input("DNI del cliente: ")
    while documentoIdentidadCliente not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        documentoIdentidadCliente = input("DNI del cliente: ")

    #mostrar la informacion actual del cliente
    informacionActualCliente = diccClientesGuardados[documentoIdentidadCliente]
    for k, v in informacionActualCliente.items():
        print(f"{k}: {v}")
    
    nombreCompleto = input("Nombre completo: ")
    genero = input("Genero: ")

    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    
    #confirmar que la fecha sea correcta
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")

    numeroTelefono = input("Numero de telefono: ")
    patronNumeroTel = "^\+?(\d{1,4})?[-.\s]?(\(?\d{1,4}\)?)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"

    #confirmar que el numero de telefono sea correcto
    while not re.match(patronNumeroTel, numeroTelefono):
        print("El formato o el numero es incorrecto.")
        numeroTelefono = input("Numero de telefono: ")

    domicilio = input("Domicilio: ")

    return documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio

