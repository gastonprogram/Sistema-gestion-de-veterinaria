import re
import json
from utiles import *

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


    documentoIdentidadCliente = verificarDocumento(rutaArchivoClientesGuardados, False)
    if documentoIdentidadCliente == -1:
        return
    elif documentoIdentidadCliente == False:
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
    
    try:
        archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
        clientesGuardados = json.load(archivoLeer)
        archivoLeer.close()
        
        
        # almacenamos la informacion del cliente
        clienteNuevo = {
            "nombreCompleto": nombreCompleto,
            "genero": genero,
            "fechaNacimiento": fechaNacimiento,
            "numeroTelefono": numeroTelefono,
            "domicilio": domicilio
        }

        # vinculamos el dni con la informacion del cliente
        clientesGuardados[documentoIdentidadCliente] = clienteNuevo

        # abrimos el archivo en modo escritura para guardar los cambios
        archivoEscribir = open(rutaArchivoClientesGuardados, "w", encoding="utf-8")
        json.dump(clientesGuardados, archivoEscribir, indent=4, ensure_ascii=False)
        archivoEscribir.close()
        
        
        
        print(f"Cliente {nombreCompleto} agregado con éxito!")
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        
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

    
    documentoIdentidadCliente = verificarDocumento(rutaArchivoClientesGuardados, True)
    if documentoIdentidadCliente == -1:
        return
    elif documentoIdentidadCliente == False:
        return
        

    print("=" * 60)
    print("Informacion del cliente".center(60))
    print("=" * 60)
    
    #mostrar la informacion actual del cliente
    
    archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding = "utf-8")
    clientesGuardados = json.load(archivoLeer)
    informacionActualCliente = clientesGuardados[documentoIdentidadCliente]
    
    print(f"Nombre completo: {informacionActualCliente['nombreCompleto']}\nGenero: {informacionActualCliente['genero']}\nFecha de nacimiento: {informacionActualCliente['fechaNacimiento']}\nTelefono: {informacionActualCliente['numeroTelefono']}\nDomicilio: {informacionActualCliente['domicilio']}")
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
