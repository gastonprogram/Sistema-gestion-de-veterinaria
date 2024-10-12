#tomar informacion de mascota nueva
def informacionMascotaNueva(dicClientesGuardados):
    documentoIdentidadDueño = input("DNI del dueño: ")
    while documentoIdentidadDueño not in dicClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        documentoIdentidadDueño = input("DNI del dueño: ")

    nombre = input("Nombre del animal: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    fechaNacimiento = input("Fecha de nacimiento: ")
    pesoKilogramos = input("Peso en kilogramos: ")
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
def modificarInformacionMascotaExistente(dicClientesGuardados, listMascotasGuardadas):
    documentoIdentidadDueño = input("DNI del dueño: ")
    while documentoIdentidadDueño not in dicClientesGuardados.keys():
        print("El DNI no se encuentra registrado.")
        documentoIdentidadDueño = input("DNI del dueño: ")
    
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
    especie = input("Especie: ")
    raza = input("Raza: ")
    fechaNacimiento = input("Fecha de nacimiento: ")
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
