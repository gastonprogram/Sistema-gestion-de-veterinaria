import re
import json
from utiles import *

#mostrar informacion de cada cliente
def mostrarInformacionClientes(rutaArchivoClientesGuardados):
    
    try:
        archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
        clientesGuardados = json.load(archivoLeer)
        
        for dni, datos in clientesGuardados.items():
            print(f"\nDNI: {dni}")
            print(f"Nombre Completo: {datos['nombreCompleto']}  |  Género: {datos['genero']}  |  Fecha de Nacimiento: {datos['fechaNacimiento']}")
            print(f"Teléfono: {datos['numeroTelefono']}  |  Domicilio: {datos['domicilio']}  |  Activo: {'Sí' if datos['activo'] else 'No'}")
            print("-" * 80)
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        return
    
    finally:
        try:
            archivoLeer.close()
            
        except:
            pass
    return

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
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        
    finally:
        
        try:
            #cerrar el archivo si se logro abrir
            archivoLeer.close()
        
        except:
            pass
        
        # almacenamos la informacion del cliente
        clienteNuevo = {
            "nombreCompleto": nombreCompleto,
            "genero": genero,
            "fechaNacimiento": fechaNacimiento,
            "numeroTelefono": numeroTelefono,
            "domicilio": domicilio,
            "activo" : True
        }

        # vinculamos el dni con la informacion del cliente
        clientesGuardados[documentoIdentidadCliente] = clienteNuevo
    
    try:
        # abrimos el archivo en modo escritura para guardar los cambios
        archivoEscribir = open(rutaArchivoClientesGuardados, "w", encoding="utf-8")
        json.dump(clientesGuardados, archivoEscribir, indent=4, ensure_ascii=False)
        
        
        print(f"Cliente {nombreCompleto} agregado con éxito!")
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return
        
    finally:
        
        try:
            #cerrar el archivo si se logro abrir
            archivoEscribir.close()
            
        except:
            pass
            
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
    try:
        archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding = "utf-8")
        clientesGuardados = json.load(archivoLeer)
        informacionActualCliente = clientesGuardados[documentoIdentidadCliente]
        
        print(f"Nombre completo: {informacionActualCliente['nombreCompleto']}\nGenero: {informacionActualCliente['genero']}\nFecha de nacimiento: {informacionActualCliente['fechaNacimiento']}\nTelefono: {informacionActualCliente['numeroTelefono']}\nDomicilio: {informacionActualCliente['domicilio']}")
        print("=" * 60)
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return
    
    finally:
        
        try:
            archivoLeer.close()
        except:
            pass
        
    

    #solicitar el nombre completo y verificar que sea correcto
    nombreCompleto = ingresarNombre()
    
    genero = elegirGenero()

    #solicitar la fecha de nacimiento y verificar que la fecha sea correcta
    fechaNacimiento = ingresarFechaNacimiento()

    #solicitar el numero de telefono y confirmar que sea correcto 
    numeroTelefono = ingresarNumeroTelefono()

    domicilio = input("Domicilio: ")

    return documentoIdentidadCliente, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio

#eliminar cliente existente
def eliminarCliente(rutaArchivoClientesGuardados, rutaArchivoMascotasGuardadas):


    """
    Elimina/desactiva un  profesional existente en el sistema.
    
    PARAMETROS:
    diccProfesionalesGuardados(dict): diccionario con los profesionales guardados:

    SALIDA:
    None: La función no retorna ningún valor.
    """
    
    documentoIdentidadCliente = verificarDocumento(rutaArchivoClientesGuardados, True)
    if documentoIdentidadCliente == -1:
        return
    elif documentoIdentidadCliente == False:
        return

    #mostrar la informacion actual del profesional
    print("=" * 60)
    print("Informacion del cliente".center(60))
    print("=" * 60)
    
    try:
        archivoClientesLeer = open(rutaArchivoClientesGuardados, "r", encoding = "utf-8")
        clientesGuardados = json.load(archivoClientesLeer)
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return
        
    finally:
        try:
            archivoClientesLeer.close()
            
        except:
            pass
    
    informacionActualCliente = clientesGuardados[documentoIdentidadCliente]
    
    print(f"Nombre completo: {informacionActualCliente['nombreCompleto']}\nGenero: {informacionActualCliente['genero']}\nFecha de nacimiento: {informacionActualCliente['fechaNacimiento']}\nTelefono: {informacionActualCliente['numeroTelefono']}\nDomicilio: {informacionActualCliente['domicilio']}")
    print("=" * 60)

    while True:
        try:
            confirmarEliminacion = input("¿Está seguro que desea eliminar el cliente? (y/n): ").lower()
            
            if confirmarEliminacion == "y":
                
                try:
                    
                    archivoMascotasLeer = open(rutaArchivoMascotasGuardadas, "r", encoding = "utf-8")
                    mascotasGuardadas = json.load(archivoMascotasLeer)
                    
                    clientesGuardados[documentoIdentidadCliente]["activo"] = False
                
                    for mascota in mascotasGuardadas:
                        if mascota["documentoIdentidadDueño"] == documentoIdentidadCliente:
                            mascota["activo"] = False
                    
                    archivoClientesEscribir = open(rutaArchivoClientesGuardados, "w", encoding="utf-8")
                    json.dump(clientesGuardados, archivoClientesEscribir, ensure_ascii=False, indent=4)
                    
                    archivoMascotasEscribir = open(rutaArchivoMascotasGuardadas, "w", encoding="utf-8")
                    json.dump(mascotasGuardadas, archivoMascotasEscribir, ensure_ascii=False, indent=4)
                    
                except FileNotFoundError:
                    print("El archivo no se encontro.")
                    return
                    
                finally:
                    try:
                        archivoClientesEscribir.close()
                        
                        archivoMascotasEscribir.close()
                        
                    except:
                        pass

                print("-" * 50)
                print("Se ha eliminado el cliente con éxito.")
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
            print("Ocurrio un error durante el proceso:", e)
            print("Intente nuevamente.")
        
    return