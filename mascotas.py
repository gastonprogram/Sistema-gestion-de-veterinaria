from clientes import *


#tomar informacion de mascota nueva
def informacionMascotaNueva(diccClientesGuardados):
    #solicitar el DNI del dueño
    documentoIdentidadDueño = input("DNI del dueño: ")
    while documentoIdentidadDueño not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado, no puede añadir una mascota sin un dueño.")

        #elegir ingresasr otro DNI, agregar un nuevo cliente, o regresar al menu
        decision = input("Ingrese: [1] Ingresar otro DNI, [2] Agregar un nuevo cliente, [3] Regresar al menu\n:")

        #buscar otro cliente
        if decision == "1":
            #buscar otro cliente
            documentoIdentidadDueño = input("DNI del dueño: ")
        
            
        #agregar un nuevo cliente
        elif decision == "2":
            informacionCliente = informacionClienteNuevo(diccClientesGuardados)
            if informacionCliente:
                guardarCliente(informacionCliente, diccClientesGuardados)
            print("Nuevo cliente agregado exitosamente.")
            return 
        
        #volver al menu
        elif decision == "3":
            print("--------------------------------------------------------------------------------")
            print("Volviendo al menu...")
            print("--------------------------------------------------------------------------------")
            return
        else:
            print("Ha seleccionado una opcion incorrecta.")

    #solicitar el nombre de la mascota y verificar sea correcto
    nombre = input("Nombre del animal: ")
    patronNombre = "^[^\W\d_]+(\s[^\W\d_]+)*$"
    while not re.match(patronNombre, nombre) or len(nombre > 60):
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
    


    documentoIdentidadDueño = input("DNI del dueño: ")
    while documentoIdentidadDueño not in diccClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")

        #elegir ingresasr otro DNI, agregar una nueva mascota, agregar un nuevo cliente, o regresar al menu
        decision = input("Ingrese: [1] Ingresar otro DNI, [2] Agregar una nueva mascota, [3] Agregar un nuevo cliente, [4] Regresar al menu\n:")

        #buscar otro cliente
        if decision == "1":
            #buscar otro cliente
            documentoIdentidadDueño = input("DNI del dueño: ")
        
        #agregar un nuevo cliente
        elif decision == "2":
            informacionMascota = informacionMascotaNueva(listMascotasGuardadas)
            if informacionMascota:
                guardarCliente(informacionMascota, listMascotasGuardadas)
            return 
        
        elif decision == "3":
            informacionCliente = informacionClienteNuevo(diccClientesGuardados)
            if informacionCliente:
                guardarCliente(informacionCliente, diccClientesGuardados)
            print("Nuevo cliente agregado exitosamente.")
            return 
        
        #volver al menu
        elif decision == "4":
            print("--------------------------------------------------------------------------------")
            print("Volviendo al menu...")
            print("--------------------------------------------------------------------------------")
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
    
    nombre = input("Nombre del animal: ")
    patronNombre = "^[^\W\d_]+(\s[^\W\d_]+)*$"
    while not re.match(patronNombre, nombre) or len(nombre > 60):
        print("El formato o longitud es incorrecto.")
        nombre = input("Nombre del animal: ")


    especie = input("Especie: ")
    raza = input("Raza: ")

    
    fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    while not re.match(patronFechaNacimiento, fechaNacimiento):
        print("El formato o la fecha es incorrecta.")
        fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")


    pesoKilogramos = input("Peso en kilogramos: ")
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
