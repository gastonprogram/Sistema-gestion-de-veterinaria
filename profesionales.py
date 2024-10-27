import re

#tomar informacion de un profesional nuevo
def informacionProfesionalNuevo(rutaArchivoProfesionalGuardados):

    """
     Solicita y valida la información de un nuevo profesional para agregarlo al sistema
     
     PARAMETROS:
     diccProfesionalesGuardados(dict): diccionario con los profesionales guardados:

     SALIDA:
        - documentoIdentidadProfesional (str): Número de DNI del profesional.
        - nombreCompleto (str): Nombre completo del profesional en formato título.
        - genero (str): Género del profesional.
        - especializacion (str): Especializacion del profesional.
        - fechaNacimiento (str): Fecha de nacimiento del profesional
        - domicilio (str): Domicilio del profesional. 
        - numeroTelefono (str): Número de teléfono del profesional.
        - horarioAtencion (str) : Rango de horario de atencion del profesional
        """
    
    print("=" * 60)
    print("Ingreso de información de un nuevo profesional".center(60))
    print("=" * 60)

    documentoIdentidadProfesional = input("DNI del profesional: ")
    archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")

    while True:
        for registro in archivoLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]
            
            # Si el DNI ya está registrado
            if documentoIdentidadProfesional == documentoIdentidadRegistro:
                print("El DNI del profesional ya se encuentra registrado.")

                while True:
                    decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                    
                    if decision == "1":
                        documentoIdentidadProfesional = input("DNI del profesional: ")
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
        nombreCompleto = input("Nombre completo: ")
    nombreCompleto = nombreCompleto.lower()
    nombreCompleto = nombreCompleto.title()
    
    genero = input("Genero (masculino/femenino): ")
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
def guardarInformacionProfesional(informacionProfesional,rutaArchivoProfesionalGuardados):


    """
    Almacena la información de un nuevo profesional en el diccionario de profesionales guardados.

    PARAMETROS:
    informacionProfesional(tupla): Tupla con la información del profesional en el siguiente orden:
        - documentoIdentidadProfesional (str): Número de DNI del profesional.
        - nombreCompleto (str): Nombre completo del profesional en formato título.
        - genero (str): Género del profesional.
        - especializacion (str): Especializacion del profesional.
        - fechaNacimiento (str): Fecha de nacimiento del profesional
        - domicilio (str): Domicilio del profesional. 
        - numeroTelefono (str): Número de teléfono del profesional.
        - horarioAtencion (str) : Rango de horario de atencion del profesional
    diccProfesionalesGuardados(dict): diccionario con los profesionales guardados


    SALIDA:
    None: La función no retorna ningún valor. """


    documentoIdentidadProfesional, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion = informacionProfesional
    
    archivoAñadir = open(rutaArchivoProfesionalGuardados, "a", encoding="utf-8")
    d = ";"
    archivoAñadir.write(f"{documentoIdentidadProfesional}{d}{nombreCompleto}{d}{genero}{d}{especializacion}{d}{fechaNacimiento}{d}{domicilio}{d}{numeroTelefono}{d}{horarioAtencion}{d}{True}" + "\n")

    print(f"Profesional {nombreCompleto} agregado con éxito!")
    return

#modificar informacion de un profesional ya creado
def modificarInformacionProfesional(rutaArchivoProfesionalGuardados):


    """
    Modifica la información de un profesional existente en el sistema.
     
     PARAMETROS:
     diccProfesionalesGuardados(dict): diccionario con los profesionales guardados:

     SALIDA:
        - documentoIdentidadProfesional (str): Número de DNI del profesional.
        - nombreCompleto (str): Nombre completo del profesional en formato título.
        - genero (str): Género del profesional.
        - especializacion (str): Especializacion del profesional.
        - fechaNacimiento (str): Fecha de nacimiento del profesional
        - domicilio (str): Domicilio del profesional. 
        - numeroTelefono (str): Número de teléfono del profesional.
        - horarioAtencion (str) : Rango de horario de atencion del profesional
        """
    
    print("=" * 60)
    print("Modificacion de información de un profesional".center(60))
    print("=" * 60)


    
    archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
    documentoIdentidadProfesional = input("DNI del profesional: ")
    while True:
        encontrado = False

        for registro in archivoLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]
            activo = campos[8]

            # Si el DNI está registrado
            if documentoIdentidadProfesional == documentoIdentidadRegistro and activo:
                encontrado = True
                break

        #si no se encuentra el dni del profesional
        if not encontrado:
            print("El DNI no se encuentra registrado.")
            while True:
                decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                
                if decision == "1":
                    documentoIdentidadProfesional = input("DNI del profesional: ")
                    archivoLeer.seek(0)
                    break
                elif decision == "2":
                    print("-" * 50)
                    print("Volviendo al menu...")
                    print("-" * 50)
                    return
                else:
                    print("Ha seleccionado una opcion incorrecta.")
        else:
            #se encontro el dni
            break


    print("=" * 60)
    print("Informacion del cliente".center(60))
    print("=" * 60)
    
    #mostrar la informacion actual del profesional
    archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")

    for linea in archivoLeer:
        campos = linea.strip().split(";")
        if campos[0] == documentoIdentidadProfesional:
            nombreActual = campos[1]
            generoActual = campos[2]
            especializacionActual = campos[3]
            fechaNacimientoActual = campos[4]
            domicilioActual = campos[5]
            telefonoActual = campos[6]
            horarioAtencionActual = campos[7]


    print(f"Nombre completo: {nombreActual}\nGenero: {generoActual}\nFecha de nacimiento: {especializacionActual}\nTelefono: {fechaNacimientoActual}\nDomicilio: {domicilioActual}\nTelefono: {telefonoActual}\nHorario de atencion: {horarioAtencionActual}")
    print("=" * 60)
    
    nombreCompleto = input("Nombre completo: ")
    genero = input("Genero (masculino/femenino): ")
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


def guardarProfesionalModificado(informacionProfesional, rutaArchivoProfesionalGuardados):
    """
    Modifica la información de un cliente específico en el archivo.
    
    PARAMETROS:
    - informacionCliente (tuple): Una tupla que contiene el DNI del cliente y los datos actualizados.
    - rutaArchivoClientesGuardados (str): Ruta del archivo donde están guardados los clientes.
    """
    
    documentoIdentidadProfesional, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion = informacionProfesional
    d = ";"
    nuevaLinea = f"{documentoIdentidadProfesional}{d}{nombreCompleto}{d}{genero}{d}{especializacion}{d}{fechaNacimiento}{d}{domicilio}{d}{numeroTelefono}{d}{horarioAtencion}{d}{True}\n"

    # Leer todas las líneas del archivo
    archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
    lineas = archivoLeer.readlines()
    print(lineas)
    archivoLeer.close()

    # Reescribir el archivo con las modificaciones
    archivoEscribir = open(rutaArchivoProfesionalGuardados, "w", encoding="utf-8")
    for linea in lineas:
        dniRegistro = linea.strip().split(";")[0]
        
        # Comparar el DNI obtenido con el DNI del cliente
        if dniRegistro == documentoIdentidadProfesional:
            archivoEscribir.write(nuevaLinea)
        else:
            archivoEscribir.write(linea)  # Mantiene las demás líneas sin cambios
    archivoEscribir.close()

    print(f"Profesional {nombreCompleto} modificado con éxito.")
    return


#eliminar profesional existente
def eliminarProfesional(rutaArchivoProfesionalGuardados):


    """
    Elimina/desactiva un  profesional existente en el sistema.
     
    PARAMETROS:
    diccProfesionalesGuardados(dict): diccionario con los profesionales guardados:

    SALIDA:
    None: La función no retorna ningún valor.
    """
    

    archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
    documentoIdentidadProfesional = input("DNI del profesional: ")
    while True:
        encontrado = False

        for registro in archivoLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]

                # Si el DNI está registrado
            if documentoIdentidadProfesional == documentoIdentidadRegistro and campos[8] == "True":
                    encontrado = True
                    nombreCompleto = campos[1]
                    genero = campos[2]
                    especializacion = campos[3]
                    fechaNacimiento = campos[4]
                    domicilio = campos[5]
                    numeroTelefono = campos[6]
                    horarioAtencion = campos[7]
                    break

        #si no se encuentra el dni del profesional
        if not encontrado:
            print("El DNI no se encuentra registrado.")
            while True:
                decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                
                if decision == "1":
                    documentoIdentidadProfesional = input("DNI del profesional: ")
                    archivoLeer.seek(0)
                    break
                elif decision == "2":
                    print("-" * 50)
                    print("Volviendo al menu...")
                    print("-" * 50)
                    archivoLeer.close()
                    return
                else:
                    print("Ha seleccionado una opcion incorrecta.")
        else:
            #se encontro el dni
            archivoLeer.close()
            break


    print(f"DNI: {documentoIdentidadProfesional}, Nombre: {nombreCompleto}")

    confirmarEliminacion = input("¿Está seguro que desea eliminar el profesional? (y/n): ").lower()
    
    while confirmarEliminacion != "y" and confirmarEliminacion != "n":
        print("Ha ingresado un valor incorrecto.")
        confirmarEliminacion = input("¿Está seguro que desea eliminar el profesional? (y/n): ").lower()
    
    if confirmarEliminacion == "y":

        archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
        lineas = archivoLeer.readlines()
        archivoLeer.close()

        archivoEscribir = open(rutaArchivoProfesionalGuardados, "w", encoding="utf-8")
        for linea in lineas:
            campos = linea.strip().split(";")
            if campos[0] == documentoIdentidadProfesional:
                archivoEscribir.write(f"{documentoIdentidadProfesional};{nombreCompleto};{genero};{especializacion};{fechaNacimiento};{domicilio};{numeroTelefono};{horarioAtencion};{False}\n")
            else:
                archivoEscribir.write(linea)
        archivoEscribir.close()

        print("-" * 50)
        print("Se ha eliminado el profesional con éxito.")
        print("-" * 50)

    elif confirmarEliminacion == "n":
        print("-" * 50)
        print("Se ha elegido cancelar la operación.")
        print("-" * 50)
    
    return