from clientes import *


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


    archivoLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
    
    documentoIdentidadDueño = input("DNI del dueño: ")
    while True:
        encontrado = False

        for registro in archivoLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]

            # Si el DNI está registrado
            if documentoIdentidadDueño == documentoIdentidadRegistro:
                encontrado = True
                break

        # Verificar si no se encontró el DNI después de recorrer el archivo
        if not encontrado:
            print("El DNI no se encuentra registrado (no puede añadir una mascota sin un dueño).")
            while True:
                decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                
                if decision == "1":
                    documentoIdentidadDueño = input("DNI del dueño: ")
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
            # se encontro dni
            break


    #solicitar el nombre de la mascota y verificar sea correcto
    nombre = input("Nombre del animal: ")
    patronNombre = "^[^\W\d_]+(\s[^\W\d_]+)*$"
    while not re.match(patronNombre, nombre) or len(nombre) > 60:
        print("El formato o longitud es incorrecto.")
        nombre = input("Nombre del animal: ")

    especie = input("Especie: ")
    raza = input("Raza: ")

    #solicitar la fecha de nacimiento y verificar que la fecha sea correcta
    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    
    
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
    documentoIdentidadCliente, nombre, especie, raza, fechaNacimiento, pesoKilogramos = informacionMascota

    ultimoID = -1
    archivoleer = open(rutaArchivoMascotasGuardados, "r", encoding="utf-8")
    for linea in archivoleer:
        ultimoID = int(linea.strip().split(";")[0])
    nuevoID = ultimoID + 1 if ultimoID >= 0 else 0
    archivoleer.close()

    archivoAñadir = open(rutaArchivoMascotasGuardados, "a", encoding="utf-8")
    d = ";"
    archivoAñadir.write(f"{nuevoID}{d}{documentoIdentidadCliente}{d}{nombre}{d}{especie}{d}{raza}{d}{fechaNacimiento}{d}{pesoKilogramos}" + "\n")
    archivoAñadir.close()
    print(f"Mascota {nombre} agregada con éxito!")
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

    archivoClienteLeer = open(rutaArchivoClientesGuardados, "r", encoding="utf-8")
    
    documentoIdentidadDueño = input("DNI del dueño: ")
    while True:
        encontrado = False

        for registro in archivoClienteLeer:
            campos = registro.strip().split(";")
            documentoIdentidadRegistro = campos[0]

            # Si el DNI está registrado
            if documentoIdentidadDueño == documentoIdentidadRegistro:
                encontrado = True
                break

        # Verificar si no se encontró el DNI después de recorrer el archivo
        if not encontrado:
            print("El DNI no se encuentra registrado (no puede añadir una mascota sin un dueño).")
            while True:
                decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")
                
                if decision == "1":
                    documentoIdentidadDueño = input("DNI del dueño: ")
                    archivoClienteLeer.seek(0)  # Volver al inicio del archivo
                    break
                elif decision == "2":
                    print("-" * 50)
                    print("Volviendo al menu...")
                    print("-" * 50)
                    return
                else:
                    print("Ha seleccionado una opcion incorrecta.")
        else:
            # se encontro dni
            break

    archivoMascotasLeer = open(rutaArchivoMascotasGuardados, "r", encoding="utf-8")
    mascotasCliente = []

    for registro in archivoMascotasLeer:
        campos = registro.strip().split(";")
        if campos[1] == documentoIdentidadDueño:
            mascota = {
                "pk": int(campos[0]),
                "documentoIdentidadDueño": campos[1],
                "nombre": campos[2],
                "especie": campos[3],
                "razaAnimal": campos[4],
                "fechaNacimiento": campos[5],
                "pesoKilogramos": float(campos[6])
            }
            mascotasCliente.append(mascota)
    
    archivoMascotasLeer.close()

    if not mascotasCliente:
        print("Este cliente no tiene mascotas registradas.")
        return None
    
    for i, mascota in enumerate(mascotasCliente):
        print(f"[{i}] Nombre: {mascota['nombre']}, Especie: {mascota['especie']}")

    indiceMascotaCliente = int(input("Seleccione la mascota: "))
    while indiceMascotaCliente > len(mascotasCliente) - 1 or indiceMascotaCliente < 0:
        indiceMascotaCliente = int(input("Seleccione la mascota: "))

    
    mascotaSeleccionada = mascotasCliente[indiceMascotaCliente]
    
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

    
    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")

    pesoKilogramos = float(input("Peso en kilogramos: "))


    return mascotaSeleccionada["pk"], documentoIdentidadDueño, nombre, especie, raza, fechaNacimiento, pesoKilogramos

#guardar informacion modificada de una mascota existente
def guardarMascotaModificada(informacionMascota, rutaArchivoMascotasGuardados):
    indiceMascotaSeleccionada, documentoIdentidadDueño, nombre, especie, razaAnimal, fechaNacimiento, pesoKilogramos = informacionMascota

    archivoMascotas = open(rutaArchivoMascotasGuardados, "r", encoding="utf-8")
    lineas = archivoMascotas.readlines()
    archivoMascotas.close()

    #reescribir el archivo con la información modificada
    archivoMascotasEscribir = open(rutaArchivoMascotasGuardados, "w", encoding="utf-8")
    for linea in lineas:
        campos = linea.strip().split(";")
        if campos[1] == documentoIdentidadDueño and int(campos[0]) == indiceMascotaSeleccionada:
            archivoMascotasEscribir.write(f"{indiceMascotaSeleccionada};{documentoIdentidadDueño};{nombre};{especie};{razaAnimal};{fechaNacimiento};{pesoKilogramos}\n")
        else:
            archivoMascotasEscribir.write(linea)
    archivoMascotasEscribir.close()
    
    print(f"Mascota {nombre} modificada con éxito!")
    return
