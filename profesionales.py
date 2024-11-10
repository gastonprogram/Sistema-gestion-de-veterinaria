import re
from utiles import *
#tomar informacion de un profesional nuevo



def mostrarInformacionProfesional(rutaArchivoProfesionalGuardados):
    
    try:
        archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding="utf-8")
        profesionalesGuardados = json.load(archivoLeer)
        archivoLeer.close()
        
        
        for dni, datos in profesionalesGuardados.items():
            print(f"\nID Profesional: {dni}")
            print(f"Nombre Completo: {datos['nombreCompleto']}  |  Género: {datos['genero']}  |  Especialización: {datos['especializacion']}")
            print(f"Fecha de Nacimiento: {datos['fechaNacimiento']}  |  Teléfono: {datos['numeroTelefono']}  |  Domicilio: {datos['domicilio']}")
            print(f"Horario de Atención: {datos['horarioAtencion']}  |  Activo: {'Sí' if datos['activo'] else 'No'}")
            print("-" * 50)
            
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        return

    finally:
        try:
            #cerrar el archivo si se abrio
            archivoLeer.close()
            
        except:
            pass

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

    #solicitar el DNI y verificar que sea correcto
    documentoIdentidadProfesional = verificarDocumento(rutaArchivoProfesionalGuardados, False)
    if documentoIdentidadProfesional == -1:
        return
    elif documentoIdentidadProfesional == False:
        return
        
    #solicitar el nombre completo y verificar que sea correcto
    nombreCompleto = ingresarNombre()
    
    #solicitar el genero y verificar que sea correcto
    genero = elegirGenero()
    
    especializacion = input("Especializacion: ")

    fechaNacimiento = ingresarFechaNacimiento()
    
    domicilio = input("Domicilio: ")

    numeroTelefono = ingresarNumeroTelefono()


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
    
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return
    
    finally:
        try:
            archivoLeer.close()
        except:
            pass
        
        
        
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

    try:
        # abrimos el archivo en modo escritura para guardar los cambios
        archivoEscribir = open(rutaArchivoProfesionalGuardados, "w", encoding = "utf-8")
        json.dump(profesionalesGuardados, archivoEscribir, indent = 4, ensure_ascii = False)
        
        print(f"Profesional {nombreCompleto} agregado con éxito!")
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return
        
    finally:
        try:
            archivoEscribir.close()
        except:
            pass
        
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
    
    try:
        
        archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding = "utf-8")
        profesionalesGuardados = json.load(archivoLeer)
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return
        
    finally:
        
        try:
            archivoLeer.close()
            
        except:
            pass
    
    informacionActualprofesional = profesionalesGuardados[documentoIdentidadProfesional]
    
    print(f"Nombre completo: {informacionActualprofesional['nombreCompleto']}\nGenero: {informacionActualprofesional['genero']}\nFecha de nacimiento: {informacionActualprofesional['fechaNacimiento']}\nTelefono: {informacionActualprofesional['numeroTelefono']}\nDomicilio: {informacionActualprofesional['domicilio']}")
    print("=" * 60)
    
    
    nombreCompleto = ingresarNombre()
    
    genero = elegirGenero()

    especializacion = input("Especializacion: ")

    fechaNacimiento = ingresarFechaNacimiento()
    
    domicilio = input("Domicilio: ")

    numeroTelefono = ingresarNumeroTelefono()

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
    
    try:
        archivoLeer = open(rutaArchivoProfesionalGuardados, "r", encoding = "utf-8")
        profesionalesGuardados = json.load(archivoLeer)
        
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return
        
    finally:
        try:
            archivoLeer.close()
            
        except:
            pass
    
    informacionActualprofesional = profesionalesGuardados[documentoIdentidadProfesional]
    
    print(f"Nombre completo: {informacionActualprofesional['nombreCompleto']}\nGenero: {informacionActualprofesional['genero']}\nFecha de nacimiento: {informacionActualprofesional['fechaNacimiento']}\nTelefono: {informacionActualprofesional['numeroTelefono']}\nDomicilio: {informacionActualprofesional['domicilio']}")
    print("=" * 60)

    while True:
        try:
            confirmarEliminacion = input("¿Está seguro que desea eliminar el profesional? (y/n): ").lower()
            
            if confirmarEliminacion == "y":
                
                try:
                    profesionalesGuardados[documentoIdentidadProfesional]["activo"] = False
                    
                    archivoEscribir = open(rutaArchivoProfesionalGuardados, "w", encoding="utf-8")
                    json.dump(profesionalesGuardados, archivoEscribir, ensure_ascii=False, indent=4)
                    archivoEscribir.close()
                    
                except FileNotFoundError:
                    print("El archivo no se encontro.")
                    return
                    
                finally:
                    try:
                        archivoEscribir.close()
                        
                    except:
                        pass

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