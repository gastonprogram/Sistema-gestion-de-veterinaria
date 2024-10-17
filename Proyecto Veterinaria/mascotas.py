from clientes import *


#tomar informacion de mascota nueva
def informacionMascotaNueva(diccClientesGuardados):

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


    #solicitar el DNI del dueño
    documentoIdentidadDueño = input("DNI del dueño: ")
    while documentoIdentidadDueño not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado (no puede añadir una mascota sin un dueño).")

        #elegir ingresasr otro DNI, agregar un nuevo cliente, o regresar al menu
        decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")

        #buscar otro cliente/dueño
        if decision == "1":
            documentoIdentidadDueño = input("DNI del dueño: ")
        
        #volver al menu
        elif decision == "2":
            print("-" * 50)
            print("Volviendo al menu...")
            print("-" * 50)
            return
        else:
            print("Ha seleccionado una opcion incorrecta.")

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
def guardarMascotaNueva(informacionMascota, listMascotasGuardadas):

    """
    Almacena la información de una nueva mascota en la lista de diccionarios de mascotas guardadas.

    PARAMETROS:
    informacionMascota: Tupla con la información de la mascota
    listMascotasGuardadas: lista con informacion sobre las mascotas

    SALIDA:
    None: La función no retorna ningún valor
    """


    documentoIdentidadDueño, nombre, especie, razaAnimal, fechaNacimiento, pesoKilogramos = informacionMascota
    listMascotasGuardadas.append({
        "documentoIdentidadDueño": documentoIdentidadDueño,
        "nombre": nombre,
        "especie": especie,
        "razaAnimal": razaAnimal,
        "fechaNacimiento": fechaNacimiento,
        "pesoKilogramos": pesoKilogramos
    })
    print(f"Mascota {nombre} agregada con éxito!")
    return

#solicitar informacion para modificar una mascota existente
def modificarInformacionMascotaExistente(diccClientesGuardados, listMascotasGuardadas):
    
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


    documentoIdentidadDueño = input("DNI del dueño: ")
    while documentoIdentidadDueño not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")

        #elegir ingresasr otro DNI, agregar una nueva mascota, agregar un nuevo cliente, o regresar al menu
        decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menu\nElegir una opcion: ")

        #buscar otro cliente
        if decision == "1":
            documentoIdentidadDueño = input("DNI del dueño: ")
        
        #volver al menu
        elif decision == "2":
            print("-" * 50)
            print("Volviendo al menu...")
            print("-" * 50)
            return
        else:
            print("Ha seleccionado una opcion incorrecta.")

    mascotasCliente = [m for m in listMascotasGuardadas if m["documentoIdentidadDueño"] == documentoIdentidadDueño]
    
    if not mascotasCliente:
        print("Este cliente no tiene mascotas registradas.")
        return None
    
    for i, mascota in enumerate(mascotasCliente):
        print(f"[{i}] Nombre: {mascota['nombre']}, Especie: {mascota['especie']}")

    indiceMascotaCliente = int(input("Seleccione la mascota: "))
    while indiceMascotaCliente > len(mascotasCliente) - 1 or indiceMascotaCliente < 0:
        indiceMascotaCliente = int(input("Seleccione la mascota: "))

    mascotaSeleccionada = mascotasCliente[indiceMascotaCliente]
    indiceMascotaGeneral = listMascotasGuardadas.index(mascotaSeleccionada)

    print("=" * 60)
    print("Informacion de la mascota".center(60))
    print("=" * 60)
    #mostrar la informacion actual de la mascota
    informacionActualMascota = listMascotasGuardadas[indiceMascotaGeneral]

    for k, v in informacionActualMascota.items():
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
    return documentoIdentidadDueño, indiceMascotaGeneral, nombre, especie, raza, fechaNacimiento, pesoKilogramos

#guardar informacion modificada de una mascota existente
def guardarMascotaModificada(informacionMascota, listMascotasGuardadas):
    documentoIdentidadDueño, indiceMascota, nombre, especie, razaAnimal, fechaNacimiento, pesoKilogramos = informacionMascota
    listMascotasGuardadas[indiceMascota] = {
        "documentoIdentidadDueño": documentoIdentidadDueño,
        "nombre": nombre,
        "especie": especie,
        "razaAnimal": razaAnimal,
        "fechaNacimiento": fechaNacimiento,
        "pesoKilogramos": pesoKilogramos
    }
    print(f"Mascota {nombre} modificada con éxito!")
    return
