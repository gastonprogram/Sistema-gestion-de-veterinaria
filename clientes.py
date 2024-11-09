import re
import json
from utiles import *




#mostrar informacion de cada cliente
def mostrarInformacionClientes(rutaArchivoClientesGuardados):
    
    try:
        archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
        clientesGuardados = json.load(archivoLeer)
        archivoLeer.close()
        
        for dni, datos in clientesGuardados.items():
            print(f"\nDNI: {dni}")
            print(f"Nombre Completo: {datos['nombreCompleto']}  |  Género: {datos['genero']}  |  Fecha de Nacimiento: {datos['fechaNacimiento']}")
            print(f"Teléfono: {datos['numeroTelefono']}  |  Domicilio: {datos['domicilio']}")
            print("-" * 50)
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
    
    finally:
        try:
            archivoLeer.close()
            
        except:
            pass



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
    nombreCompleto = ingresarNombre()
    

    
    #solicitar el genero y verificar que sea correcto
    genero = elegirGenero()


    #solicitar la fecha de nacimiento y verificar que la fecha sea correcta
    fechaNacimiento = ingresarFechaNacimiento()

    #solicitar el numero de telefono y confirmar que sea correcto 
    numeroTelefono = ingresarNumeroTelefono()

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
    nombreCompleto = ingresarNombre()
    
    genero = elegirGenero()

    #solicitar la fecha de nacimiento y verificar que la fecha sea correcta
    fechaNacimiento = ingresarFechaNacimiento()

    #solicitar el numero de telefono y confirmar que sea correcto 
    numeroTelefono = ingresarNumeroTelefono()

    domicilio = input("Domicilio: ")

    return documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio
