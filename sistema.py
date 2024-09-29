"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
...



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

def main():

    #-------------------------------------------------
    # Inicialización de variables
    #-------------------------------------------------
    clientesGuardados = {}
    mascotasGuardadas = []
    profesionalesGuardados = {}
    turnosProgramados = []

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------

    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Gestionar Clientes")
        print("[2] Gestionar Mascotas") 
        print("[3] Gestionar Profesionales")
        print("[4] Gestionar Turnos")
        print("[5] Informes")
        print("---------------------------")
        print("[0] Salir del programa")
        print()
            
        opcion_principal = input("Seleccione una opción: ")

        if opcion_principal == "1":  # Submenú de Clientes
            while True:
                print("MENÚ CLIENTES")
                print("[1] Agregar Cliente")
                print("[2] Modificar Cliente")
                print("[3] Eliminar Cliente")
                print("[0] Volver al menú principal")

                opcion_clientes = input("Seleccione una opción: ")

                if opcion_clientes == "1":  # Agregar cliente
                    def informacionClienteNuevo():
                        documentoIdentidad = input("DNI: ")
                        nombreCompleto = input("Nombre completo: ")
                        genero = input("Genero: ")
                        fechaNacimiento = input("Fecha de Nacimiento: ")
                        numeroTelefono = input("Numero de Telefono (+XX-XXXXXXXXXX): ")
                        domicilio = input("Domicilio: ")

                        return documentoIdentidad, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio

                    def guardarCliente(informacionCliente):
                        documentoIdentidad, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio = informacionCliente

                        clientesGuardados[documentoIdentidad] = {
                            "nombreCompleto": nombreCompleto,
                            "genero": genero,
                            "fechaNacimiento": fechaNacimiento,
                            "numeroTelefono" : numeroTelefono,
                            "domicilio": domicilio,
                        }

                    info = informacionClienteNuevo()
                    guardarCliente(info)

                elif opcion_clientes == "2": #modificar cliente
                    def modificarInformacionCliente():
                        dni = input("DNI: ")
                        while dni not in clientesGuardados.keys():
                            print("El DNI no se encuentra registrado.")
                            dni = input("DNI: ")
                        informacionActualCliente = clientesGuardados[dni]

                        for k, v in informacionActualCliente.items():
                            print(f"{k}: {v}")
                        
                        nombreCompleto = input("Nombre completo: ")
                        genero = input("Genero: ")
                        fechaNacimiento = input("Fecha de Nacimiento: ")
                        numeroTelefono = input("Numero de Telefono (+XX-XXXXXXXXXX): ")
                        domicilio = input("Domicilio: ")

                        return dni, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio

                    def guardarCliente(informacionCliente):
                        dni, nombreCompleto, genero, fechaNacimiento, numeroTelefono, domicilio = informacionCliente

                        clientesGuardados[dni] = {
                            "nombreCompleto": nombreCompleto,
                            "genero": genero,
                            "fechaNacimiento": fechaNacimiento,
                            "numeroTelefono" : numeroTelefono,
                            "domicilio": domicilio,
                        }

                    info = modificarInformacionCliente()
                    guardarCliente(info)


                     
                elif opcion_clientes == "0":  # Volver al menú principal
                    break
        
        elif opcion_principal == "2":  # Submenú de Mascotas
            while True:
                print("MENÚ MASCOTAS")
                print("[1] Agregar Mascota")
                print("[2] Modificar Mascota")
                print("[3] Eliminar Mascota")
                print("[0] Volver al menú principal")

                opcion_mascotas = input("Seleccione una opción: ")

                if opcion_mascotas == "1":
                    def informacionMascotaNueva():
                        dueño = input("DNI del dueño: ")
                        while dueño not in clientesGuardados.keys():
                            print("El DNI no se encuentra registrado.")
                            dueño = input("DNI del dueño: ")
                        nombre = input("Nombre del animal: ")
                        tipo = input("Tipo: ")
                        raza = input("Raza: ")
                        fechaNacimiento = input("Edad: ")
                        peso = input("Peso: ")

                        return dueño, nombre, tipo, raza, fechaNacimiento, peso

                    def guardarMascota(informacionMascota):
                        dueño, nombre, tipo, razaAnimal, fechaNacimiento, peso = informacionMascota

                        mascotasGuardadas.append({
                            "dueño": dueño,
                            "nombre": nombre,
                            "tipo": tipo,
                            "razaAnimal": razaAnimal,
                            "fechaNacimiento": fechaNacimiento,
                            "peso": peso
                        })
                        print(f"Mascota {nombre} agregada con éxito!")

                    info = informacionMascotaNueva()
                    guardarMascota(info)

                elif opcion_mascotas == "2":
                    def modificarInformacionMascota():
                        dueño = input("DNI del dueño: ")
                        while dueño not in clientesGuardados.keys():
                            print("El DNI no se encuentra registrado.")
                            dueño = input("DNI del dueño: ")
                        
                        mascotasCliente = [m for m in mascotasGuardadas if m["dueño"] == dueño]
                        print(mascotasCliente)
                        
                        if not mascotasCliente:
                            print("Este cliente no tiene mascotas registradas.")
                            return None
                        
                        for i, mascota in enumerate(mascotasCliente):
                            print(f"[{i}] Nombre: {mascota['nombre']}, Tipo: {mascota['tipo']}")

                        indiceMascotaCliente = int(input("Seleccione la mascota: "))
                        while indiceMascotaCliente > len(mascotasCliente) - 1 or indiceMascotaCliente < 0:
                            indiceMascotaCliente = int(input("Seleccione la mascota: "))

                        mascotaSeleccionada = mascotasCliente[indiceMascotaCliente]
                        indiceMascotaGeneral = mascotasGuardadas.index(mascotaSeleccionada)

                        nombre = input("Nombre: ")
                        tipo = input("Tipo: ")
                        raza = input("Raza: ")
                        fechaNacimiento = input("Fecha de nacimiento: ")
                        peso = input("Peso: ")

                        return dueño, indiceMascotaGeneral, nombre, tipo, raza, fechaNacimiento, peso
                    
                    def guardarMascota(informacionMascota):
                        dueño, indiceMascota, nombre, tipo, razaAnimal, fechaNacimiento, peso = informacionMascota

                        mascotasGuardadas[indiceMascota] = {
                            "dueño": dueño,
                            "nombre": nombre,
                            "tipo": tipo,
                            "razaAnimal": razaAnimal,
                            "fechaNacimiento": fechaNacimiento,
                            "peso": peso
                        }
                        print(f"Mascota {nombre} modificada con éxito!")

                    info = modificarInformacionMascota()
                    guardarMascota(info)


                
                elif opcion_mascotas == "0":  # Volver al menú principal
                    break
        
        elif opcion_principal == "3":  # Submenú de Profesionales
            while True:
                print("MENÚ PROFESIONALES")
                print("[1] Agregar Profesional")
                print("[2] Modificar Profesional")
                print("[3] Eliminar Profesional")
                print("[0] Volver al menú principal")

                opcion_profesionales = input("Seleccione una opción: ")

                if opcion_profesionales == "1": #agregar profesional nuevo
                    def informacionProfesionalNuevo():
                        documentoIdentidad = input("DNI: ")
                        nombreCompleto = input("Nombre completo: ")
                        genero = input("Genero: ")
                        especializacion = input("Especializacion: ")
                        fechaNacimiento = input("Fecha de Nacimiento: ")
                        domicilio = input("Domicilio: ")
                        numeroTelefono = input("Numero de Telefono (+XX-XXXXXXXXXX): ")
                        horarioAtencion = input("Horario de atencion:")

                        return documentoIdentidad, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion

                    def agregarProfesionalNuevo(informacionProfesional):
                        documentoIdentidad, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion = informacionProfesional

                        profesionalesGuardados[documentoIdentidad] = {
                            "nombreCompleto": nombreCompleto,
                            "genero": genero,
                            "especializacion": especializacion,
                            "fechaNacimiento": fechaNacimiento,
                            "domicilio": domicilio,
                            "numeroTelefono" : numeroTelefono,
                            "horarioAtencion": horarioAtencion
                        }
                        print(f"Profesional {nombreCompleto} agregado con éxito!")

                    info = informacionProfesionalNuevo()
                    agregarProfesionalNuevo(info)

                elif opcion_profesionales == "2": #modificar profesional

                    def modificarInformacionProfesional():
                        dni = input("DNI del profesional: ")
                        while dni not in profesionalesGuardados.keys():
                            print("El DNI no se encuentra registrado en la lista de profesionales.")
                            dni = input("DNI del profesional: ")
                        informacionActualProfesional = profesionalesGuardados[dni]

                        for k, v in informacionActualProfesional.items():
                            print(f"{k}: {v}")
                        
                        nombreCompleto = input("Nombre completo: ")
                        genero = input("Genero: ")
                        especializacion = input("Especializacion: ")
                        fechaNacimiento = input("Fecha de Nacimiento: ")
                        domicilio = input("Domicilio: ")
                        numeroTelefono = input("Numero de Telefono (+XX-XXXXXXXXXX): ")
                        horarioAtencion = input("Horario de atencion:")

                        return dni, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion

                    def guardarProfesional(informacionProfesional):
                        dni, nombreCompleto, genero, especializacion, fechaNacimiento, domicilio, numeroTelefono, horarioAtencion = informacionProfesional

                        profesionalesGuardados[dni] = {
                            "nombreCompleto": nombreCompleto,
                            "genero": genero,
                            "especializacion": especializacion,
                            "fechaNacimiento": fechaNacimiento,
                            "domicilio": domicilio,
                            "numeroTelefono" : numeroTelefono,
                            "horarioAtencion": horarioAtencion
                        }

                    info = modificarInformacionProfesional()
                    guardarProfesional(info)

                elif opcion_profesionales == "2": #modificar profesional
                    def eliminarProfesional():
                        eliminado = False
                        dni = input("DNI del profesional: ")
                        while dni not in profesionalesGuardados.keys():
                            print("El DNI no se encuentra registrado en la lista de profesionales.")
                            dni = input("DNI del profesional: ")
                        print(f"DNI: {dni}\n Nombre:{profesionalesGuardados[dni]['nombre']}")
                        confirmarEliminacion = input("Esta seguro que desea eliminar el profesional (y/n): ")
                        while confirmarEliminacion.lower != "y" or confirmarEliminacion.lower != "n":
                            print("Ha ingresado un valor incorrecto.")
                            confirmarEliminacion = input("Esta seguro que desea eliminar el profesional (y/n): ")

                        if confirmarEliminacion.lower == "y":
                            profesionalesGuardados.pop(dni)
                            print("Se ha eliminado el profesional con exito.")
                        elif confirmarEliminacion.lower == "n":
                            print("Se ha elegido cancelar la operacion.")
                    
                    eliminarProfesional()
                        

                elif opcion_profesionales == "0":  # Volver al menú principal
                    break
        
        elif opcion_principal == "4":  # Submenú de Turnos
            while True:
                print("MENÚ TURNOS")
                print("[1] Programar Turno")
                print("[2] Modificar Turno")
                print("[3] Cancelar Turno")
                print("[0] Volver al menú principal")

                opcion_turnos = input("Seleccione una opción: ")

                if opcion_turnos == "1":
                    def informacionTurnoCliente():
                        documentoIdentidad = input("DNI del cliente: ")
                        while documentoIdentidad not in clientesGuardados.keys():
                            print("El DNI no se encuentra registrado.")
                            documentoIdentidad = input("DNI: ")

                        mascotasCliente = [m for m in mascotasGuardadas if m["dueño"] == documentoIdentidad]
                        if not mascotasCliente:
                            print("Este cliente no tiene mascotas registradas.")

                        for i, mascota in enumerate(mascotasCliente):
                            print(f"[{i}] Nombre: {mascota['nombre']}, Tipo: {mascota['tipo']}")

                        indiceMascota = int(input("Seleccione la mascota: "))
                        while indiceMascota > len(mascotasCliente) - 1 or indiceMascota < 0:
                            indiceMascota = int(input("Seleccione la mascota: "))


                        for dni, profesional in profesionalesGuardados.items():
                            print(f"DNI: {dni}, Nombre: {profesional['nombreCompleto']}, Especialización: {profesional['especializacion']}")

                        especialista = input("Ingrese el DNI del especialista: ")
                        fecha = input("Formato -> XX/XX/XXXX\nFecha: ")
                        horario = input("Formato -> XX:XX\nHorario: ")
                        motivo = input("Motivo: ")

                        return documentoIdentidad, indiceMascota, especialista, fecha, horario, motivo
                    
                    def añadirTurnoCliente(informacionTurno):
                        documentoIdentidad, indiceMascota, especialista, fecha, horario, motivo = informacionTurno
                        turnosProgramados.append({
                            "documentoIdentidad": documentoIdentidad,
                            "indiceMascota": indiceMascota,
                            "especialista": especialista,
                            "fecha": fecha,
                            "horario": horario,
                            "motivo": motivo
                            })
                        print(f"Turno programado para el {fecha} a las {horario}.")

                    info = informacionTurnoCliente()
                    añadirTurnoCliente(info)

                elif opcion_turnos == "0":  # Volver al menú principal
                    break
        elif opcion_principal == "5":  # Submenú de informes
            print(clientesGuardados)
            print(mascotasGuardadas)
            print(profesionalesGuardados)
            print(turnosProgramados)
        
        elif opcion_principal == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

        
        opcion_principal = ""

        

# Punto de entrada al programa
main()
