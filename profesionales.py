import re
from utiles import *
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

    documentoIdentidadProfesional = verificarDocumento(rutaArchivoProfesionalGuardados, False)
    if documentoIdentidadProfesional == -1:
        return
    elif documentoIdentidadProfesional == False:
        return
        
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
    
    
    try:
        archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
        profesionalesGuardados = json.load(archivoLeer)
        archivoLeer.close()
        
        
        # almacenamos la informacion del profesional
        profesionalNuevo = {
            "nombreCompleto": nombreCompleto,
            "genero": genero,
            "especializacion": especializacion,
            "fechaNacimiento": fechaNacimiento,
            "domicilio": domicilio,
            "numeroTelefono" : numeroTelefono,
            "horarioAtencion": horarioAtencion,
            "activo" : True
        }

        # vinculamos el dni con la informacion del profesional
        profesionalesGuardados[documentoIdentidadProfesional] = profesionalNuevo

        # abrimos el archivo en modo escritura para guardar los cambios
        archivoEscribir = open(rutaArchivoProfesionalGuardados, "w", encoding = "utf-8")
        json.dump(profesionalesGuardados, archivoEscribir, indent = 4, ensure_ascii = False)
        archivoEscribir.close()
        
        print(f"Profesional {nombreCompleto} agregado con éxito!")
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        
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

    documentoIdentidadProfesional = verificarDocumento(rutaArchivoProfesionalGuardados, True)
    if documentoIdentidadProfesional == -1:
        return
    elif documentoIdentidadProfesional == False:
        return

    print("=" * 60)
    print("Informacion del profesional".center(60))
    print("=" * 60)
    
    #mostrar la informacion actual del profesional
    archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding = "utf-8")
    profesionalesGuardados = json.load(archivoLeer)
    archivoLeer.close()
    
    informacionActualprofesional = profesionalesGuardados[documentoIdentidadProfesional]
    
    print(f"Nombre completo: {informacionActualprofesional['nombreCompleto']}\nGenero: {informacionActualprofesional['genero']}\nFecha de nacimiento: {informacionActualprofesional['fechaNacimiento']}\nTelefono: {informacionActualprofesional['numeroTelefono']}\nDomicilio: {informacionActualprofesional['domicilio']}")
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

#eliminar profesional existente
def eliminarProfesional(rutaArchivoProfesionalGuardados):


    """
    Elimina/desactiva un  profesional existente en el sistema.
    
    PARAMETROS:
    diccProfesionalesGuardados(dict): diccionario con los profesionales guardados:

    SALIDA:
    None: La función no retorna ningún valor.
    """
    
    documentoIdentidadProfesional = verificarDocumento(rutaArchivoProfesionalGuardados, True)
    if documentoIdentidadProfesional == -1:
        return
    elif documentoIdentidadProfesional == False:
        return

    #mostrar la informacion actual del profesional
    print("=" * 60)
    print("Informacion del profesional".center(60))
    print("=" * 60)
    
    archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding = "utf-8")
    profesionalesGuardados = json.load(archivoLeer)
    archivoLeer.close()
    
    informacionActualprofesional = profesionalesGuardados[documentoIdentidadProfesional]
    
    print(f"Nombre completo: {informacionActualprofesional['nombreCompleto']}\nGenero: {informacionActualprofesional['genero']}\nFecha de nacimiento: {informacionActualprofesional['fechaNacimiento']}\nTelefono: {informacionActualprofesional['numeroTelefono']}\nDomicilio: {informacionActualprofesional['domicilio']}")
    print("=" * 60)

    while True:
        try:
            confirmarEliminacion = input("¿Está seguro que desea eliminar el profesional? (y/n): ").lower()
            
            if confirmarEliminacion == "y":
                
                profesionalesGuardados[documentoIdentidadProfesional]["activo"] = False

                archivoEscribir = open(rutaArchivoProfesionalGuardados, "w", encoding="utf-8")
                json.dump(profesionalesGuardados, archivoEscribir, ensure_ascii=False, indent=4)
                archivoEscribir.close()

                print("-" * 50)
                print("Se ha eliminado el profesional con éxito.")
                print("-" * 50)
                break  

            elif confirmarEliminacion == "n":
                print("-" * 50)
                print("Se ha elegido cancelar la operación.")
                print("-" * 50)
                break  
            
            else:
                print("Ha ingresado un valor incorrecto.")

        except Exception as e:
            print("Ocurrió un error durante el proceso:", e)
            print("Intente nuevamente.")
        
    return