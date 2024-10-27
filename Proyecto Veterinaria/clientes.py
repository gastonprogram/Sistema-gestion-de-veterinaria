import re

#tomar informacion sobre un cliente nuevo
def informacionClienteNuevo(rutaArchivoClientesGuardados):
    """
     Solicita y valida la información de un nuevo cliente para agregarlo al sistema
     
     PARAMETROS:
     diccClientesGuardados(dict): diccionario con los clientes guardados:

     SALIDA:
        - documento (str): Número de DNI del cliente.
        - nombreCompleto (str): Nombre completo del cliente en formato título.
        - genero (str): Género del cliente.
        - fechaNacimiento (str): Fecha de nacimiento del cliente
        - numeroTelefono (str): Número de teléfono del cliente.
        - domicilio (str): Domicilio del cliente. """
    

    print("=" * 60)
    print("Ingreso de información del nuevo cliente".center(60))
    print("=" * 60)

    

    documentoIdentidadCliente = input("DNI del cliente: ")

    archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")

    while True:
        for registro in archivoLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]
            
            # Si el DNI ya está registrado
            if documentoIdentidadCliente == documentoIdentidadRegistro:
                print("El DNI ya se encuentra registrado.")

                while True:
                    decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                    
                    if decision == "1":
                        documentoIdentidadCliente = input("DNI del cliente: ")
                        archivoLeer.seek(0)  # Volver al inicio del archivo
                        break
                    
                    elif decision == "2":
                        print("-" * 50)
                        print("Volviendo al menu...")
                        print("-" * 50)
                        archivoLeer.close()  
                        return
                    
                    else:
                        print("Ha seleccionado una opcion incorrecta.")
                break
        else:
            # Si se recorrió todo el archivo y no se encontró el DNI
            archivoLeer.close()
            break


    #solicitar el nombre completo y verificar que sea correcto
    nombreCompleto = input("Nombre completo: ")
    patronNombre = "^[^\W\d_]+(\s[^\W\d_]+)*$"
    while not re.match(patronNombre, nombreCompleto) or len(nombreCompleto) > 60:
        print("El formato o longitud es incorrecto.")
    nombreCompleto = nombreCompleto.lower()
    nombreCompleto = nombreCompleto.title()
    

    genero = input("Genero (masculino/femenino): ")

    #solicitar la fecha de nacimiento y verificar que la fecha sea correcta
    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")

    #solicitar el numero de telefono y confirmar que sea correcto 
    numeroTelefono = input("Numero de telefono: ")
    patronNumeroTel = "^\+?(\d{1,4})?[-.\s]?(\(?\d{1,4}\)?)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    while not re.match(patronNumeroTel, numeroTelefono):
        print("El formato o el numero es incorrecto.")
        numeroTelefono = input("Numero de telefono: ")

    domicilio = input("Domicilio: ")
    
    return documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio

#guardar informacion cliente
def guardarCliente(informacionCliente, rutaArchivoClientesGuardados):

    """
    Almacena la información de un nuevo cliente en el diccionario de clientes guardados.


    PARAMETROS:
    informacionCliente(tupla): Tupla con la información del cliente en el siguiente orden:
        - documentoIdentidadCliente (str): Número de DNI del cliente.
        - nombreCompleto (str): Nombre completo del cliente.
        - genero (str): Género del cliente.
        - fechaNacimiento (str): Fecha de nacimiento del cliente
        - numeroTelefono (str): Número de teléfono del cliente.
        - domicilio (str): Domicilio del cliente.
    diccClientesGuardados: Diccionario con los clientes registrados

    SALIDA:
    None: La función no retorna ningún valor. """

    documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio = informacionCliente

    archivoAñadir = open(rutaArchivoClientesGuardados, "a", encoding="utf-8")

    d = ";"

    archivoAñadir.write(f"{documentoIdentidadCliente}{d}{nombreCompleto}{d}{genero}{d}{fechaNacimiento}{d}{numeroTelefono}{d}{domicilio}" + "\n")


    print(f"Cliente {nombreCompleto} agregado con éxito!")
    return

#modificar cliente existente
def modificarInformacionCliente(rutaArchivoClientesGuardados):

    """
     Modifica la información de un cliente existente en el sistema.


     
     PARAMETROS:
     diccClientesGuardados: diccionario con los clientes guardados:


     SALIDA:
        - documento (str): Número de DNI del cliente.
        - nombreCompleto (str): Nombre completo del cliente en formato título.
        - genero (str): Género del cliente.
        - fechaNacimiento (str): Fecha de nacimiento del cliente
        - numeroTelefono (str): Número de teléfono del cliente.
        - domicilio (str): Domicilio del cliente."""
    
    print("=" * 60)
    print("Modificacion de información de un cliente".center(60))
    print("=" * 60)


    archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
    
    documentoIdentidadCliente = input("DNI del cliente: ")
    while True:
        encontrado = False

        for registro in archivoLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]

            # Si el DNI está registrado
            if documentoIdentidadCliente == documentoIdentidadRegistro:
                encontrado = True
                break

        # Verificar si no se encontró el DNI después de recorrer el archivo
        if not encontrado:
            print("El DNI no se encuentra registrado.")
            while True:
                decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                
                if decision == "1":
                    documentoIdentidadCliente = input("DNI del cliente: ")
                    archivoLeer.seek(0)  # Volver al inicio del archivo
                    break
                elif decision == "2":
                    print("-" * 50)
                    print("Volviendo al menu...")
                    print("-" * 50)
                    return
                else:
                    print("Ha seleccionado una opcion incorrecta.")
        else:
            # Si se encontró el DNI, salir del ciclo principal
            break

    print("=" * 60)
    print("Informacion del cliente".center(60))
    print("=" * 60)
    
    #mostrar la informacion actual del cliente
    archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")

    for linea in archivoLeer:
        campos = linea.strip().split(";")
        if campos[0] == documentoIdentidadCliente:
            nombreActual = campos[1]
            generoActual = campos[2]
            fechaNacimientoActual = campos[3]
            telefonoActual = campos[4]
            domicilioActual = campos[5]


    print(f"Nombre completo: {nombreActual}\nGenero: {generoActual}\nFecha de nacimiento: {fechaNacimientoActual}\nTelefono: {telefonoActual}\nDomicilio: {domicilioActual}")
    print("=" * 60)
    

    #solicitar el nombre completo y verificar que sea correcto
    nombreCompleto = input("Nombre completo: ")
    patronNombre = "^[^\W\d_]+(\s[^\W\d_]+)*$"
    while not re.match(patronNombre, nombreCompleto) or len(nombreCompleto) > 60:
        print("El formato o longitud es incorrecto.")
    nombreCompleto = nombreCompleto.lower()
    nombreCompleto = nombreCompleto.title()
    
    genero = input("Genero (masculino/femenino): ")

    #solicitar la fecha de nacimiento y verificar que la fecha sea correcta
    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")

    #solicitar el numero de telefono y confirmar que sea correcto 
    numeroTelefono = input("Numero de telefono: ")
    patronNumeroTel = "^\+?(\d{1,4})?[-.\s]?(\(?\d{1,4}\)?)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    while not re.match(patronNumeroTel, numeroTelefono):
        print("El formato o el numero es incorrecto.")
        numeroTelefono = input("Numero de telefono: ")

    domicilio = input("Domicilio: ")

    return documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio

def guardarClienteModificado(informacionCliente, rutaArchivoClientesGuardados):
    """
    Modifica la información de un cliente específico en el archivo.
    
    PARAMETROS:
    - informacionCliente (tuple): Una tupla que contiene el DNI del cliente y los datos actualizados.
    - rutaArchivoClientesGuardados (str): Ruta del archivo donde están guardados los clientes.
    """
    
    documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio = informacionCliente
    d = ";"
    nuevaLinea = f"{documentoIdentidadCliente}{d}{nombreCompleto}{d}{genero}{d}{fechaNacimiento}{d}{numeroTelefono}{d}{domicilio}+\n"

    # Leer todas las líneas del archivo
    archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
    lineas = archivoLeer.readlines()
    archivoLeer.close()

    # Reescribir el archivo con las modificaciones
    archivoEscribir = open(rutaArchivoClientesGuardados, "w", encoding="utf-8")
    for linea in lineas:
        dniRegistro = linea.strip().split(";")[0]
        
        # Comparar el DNI obtenido con el DNI del cliente
        if dniRegistro == documentoIdentidadCliente:
            archivoEscribir.write(nuevaLinea)
        else:
            archivoEscribir.write(linea)  # Mantiene las demás líneas sin cambios

    archivoEscribir.close()
    print(f"Cliente {nombreCompleto} modificado con éxito.")
    return