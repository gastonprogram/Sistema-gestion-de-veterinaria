from clientes import *
from utiles import *


def mostrarInformacionMascotas(rutaArchivoMascotasGuardadas):
    
    try:
        archivoLeer = open(rutaArchivoMascotasGuardadas, "r", encoding="utf-8")
        mascotasGuardadas = json.load(archivoLeer)
        archivoLeer.close()
        
        for mascota in mascotasGuardadas:
            print(f"\nDueño (DNI): {mascota['documentoIdentidadDueño']}")
            print(f"Nombre: {mascota['nombre']}  |  Especie: {mascota['especie']}  |  Raza: {mascota['raza']}")
            print(f"Fecha de Nacimiento: {mascota['fechaNacimiento']}  |  Peso: {mascota['pesoKilogramos']} kg")
            print("-" * 50)
            
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
    
    finally:
        try:
            archivoLeer.close()
            
        except:
            pass



#tomar informacion de mascota nueva
def informacionMascotaNueva(rutaArchivoClientesGuardados):

    """
        Solicita y valida la información de una nueva mascota para agregarla al sistema.


        PARAMETROS:
        diccClientesGuardados: diccionario con los clientes guardados:


        SALIDA:
        - nombre (str): Nombre de la mascota.
        - especie (str): Especie de la mascota.
        - raza (str): Raza de la mascota.
        - fechaNacimiento (str): Fecha de nacimiento de mascota 
        - pesoKilogramos (int): Peso de la mascota en kilogramos.

    """

    documentoIdentidadDueño = verificarDocumento(rutaArchivoClientesGuardados, True)
    if documentoIdentidadDueño == -1:
        return
    elif documentoIdentidadDueño == False:
        return
        
    #solicitar el nombre de la mascota y verificar sea correcto
    nombre = input("Nombre del animal: ")
    patronNombre = "^[^\W\d_]+(\s[^\W\d_]+)*$"
    while not re.match(patronNombre, nombre) or len(nombre) > 60:
        print("El formato o longitud es incorrecto.")
        nombre = input("Nombre del animal: ")

    especie = input("Especie: ")
    raza = input("Raza: ")

    #solicitar la fecha de nacimiento y verificar que la fecha sea correcta
    fechaNacimiento = ingresarFechaNacimiento()
    
    
    pesoKilogramos = float(input("Peso en kilogramos: "))
    return documentoIdentidadDueño, nombre, especie, raza, fechaNacimiento, pesoKilogramos

#guardar informacion mascota
def guardarMascotaNueva(informacionMascota, rutaArchivoMascotasGuardados):

    """
    Almacena la información de una nueva mascota en la lista de diccionarios de mascotas guardadas.

    PARAMETROS:
    informacionMascota: Tupla con la información de la mascota
    listMascotasGuardadas: lista con informacion sobre las mascotas

    SALIDA:
    None: La función no retorna ningún valor
    """
    documentoIdentidadDueño, nombre, especie, raza, fechaNacimiento, pesoKilogramos = informacionMascota

    try:
        archivoLeer = open(rutaArchivoMascotasGuardados, "r", encoding="utf-8")
        mascotasGuardadas = json.load(archivoLeer)
        archivoLeer.close()

        
        mascotasGuardadas.append({
            "documentoIdentidadDueño": documentoIdentidadDueño,
            "nombre": nombre,
            "especie": especie,
            "raza": raza,
            "fechaNacimiento": fechaNacimiento,
            "pesoKilogramos": pesoKilogramos
        })

        # guardar los cambios en el archivo
        archivoEscribir = open(rutaArchivoMascotasGuardados, "w", encoding="utf-8")
        json.dump(mascotasGuardadas, archivoEscribir, ensure_ascii=False, indent=4)
        archivoEscribir.close()
        
        print(f"Mascota {nombre} agregada con éxito!")
        
    except FileNotFoundError:
        print("El archivo no fue encontrado")
        
    return


#solicitar informacion para modificar una mascota existente
def modificarInformacionMascotaExistente(rutaArchivoClientesGuardados, rutaArchivoMascotasGuardados):
    
    """Modifica la información de una mascota existente en el sistema.


    PARAMETROS:
    diccClientesGuardados (dict): Diccionario con los clientes registrados. 
    listMascotasGuardadas (list): Lista de diccionarios que contienen la información de las mascotas registradas.
    

    SALIDA:    
        - documentoIdentidadDueño (str): Número de DNI del dueño de la mascota.
        - indiceMascotaGeneral (int): Índice de la mascota en la lista general de mascotas.
        - nombre (str): Nombre de la mascota.
        - especie (str): Especie de la mascota.
        - raza (str): Raza de la mascota.
        - fechaNacimiento (str): Fecha de nacimiento de la mascota
        - pesoKilogramos (float): Peso de la mascota en kilogramos.
    """

    documentoIdentidadDueño = verificarDocumento(rutaArchivoClientesGuardados, True)
    if documentoIdentidadDueño == -1:
        return
    elif documentoIdentidadDueño == False:
        return
    
    
    
    archivoMascotasLeer = open(rutaArchivoMascotasGuardados, "r", encoding = "utf-8")
    mascotasGuardadas = json.load(archivoMascotasLeer)
    archivoMascotasLeer.close()
    
    mascotasCliente = [m for m in mascotasGuardadas if m["documentoIdentidadDueño"] == documentoIdentidadDueño]


    if not mascotasCliente:
        print("Este cliente no tiene mascotas registradas.")
        return None
    
    for i, mascota in enumerate(mascotasCliente):
        print(f"[{i}] Nombre: {mascota['nombre']}, Especie: {mascota['especie']}")

    while True:
        try:
            indiceMascotaCliente = int(input("Seleccione la mascota: "))
            
            if indiceMascotaCliente < 0:
                print("El indice no puede ser negativo. Por favor, intenta de nuevo.")
            elif indiceMascotaCliente >= len(mascotasCliente):
                print(f"El índice debe estar entre 0 y {len(mascotasCliente) - 1}. Por favor, intenta de nuevo.")
            else:
                break  
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    mascotaSeleccionada = mascotasCliente[indiceMascotaCliente]
    indiceMascotaGeneral = mascotasGuardadas.index(mascotaSeleccionada)
    
    print("=" * 60)
    print("Información de la mascota".center(60))
    print("=" * 60)
    
    # Mostrar la información actual de la mascota
    for k, v in mascotaSeleccionada.items():
        print(f"{k}: {v}")
    print("=" * 60)
    
    nombre = input("Nombre del animal: ")
    patronNombre = "^[^\W\d_]+(\s[^\W\d_]+)*$"
    while not re.match(patronNombre, nombre) or len(nombre) > 60:
        print("El formato o longitud es incorrecto.")
        nombre = input("Nombre del animal: ")


    especie = input("Especie: ")
    
    raza = input("Raza: ")

    
    fechaNacimiento = ingresarFechaNacimiento()

    pesoKilogramos = float(input("Peso en kilogramos: "))

    return indiceMascotaGeneral, documentoIdentidadDueño, nombre, especie, raza, fechaNacimiento, pesoKilogramos

#guardar informacion modificada de una mascota existente
def guardarMascotaModificada(informacionMascota, rutaArchivoMascotasGuardados):
    indiceMascotaSeleccionada, documentoIdentidadDueño, nombre, especie, raza, fechaNacimiento, pesoKilogramos = informacionMascota
    
    
    archivoMascotasLeer = open(rutaArchivoMascotasGuardados, "r", encoding = "utf-8")
    mascotasGuardadas = json.load(archivoMascotasLeer)
    archivoMascotasLeer.close()
    
    mascotasGuardadas[indiceMascotaSeleccionada] = {
            "documentoIdentidadDueño": documentoIdentidadDueño,
            "nombre": nombre,
            "especie": especie,
            "raza": raza,
            "fechaNacimiento": fechaNacimiento,
            "pesoKilogramos": pesoKilogramos
        }
    
    
    # guardar los cambios en el archivo
    archivoEscribir = open(rutaArchivoMascotasGuardados, "w", encoding="utf-8")
    json.dump(mascotasGuardadas, archivoEscribir, ensure_ascii=False, indent=4)
    archivoEscribir.close()
    
    print(f"Mascota {nombre} modificada con éxito!")
    return
