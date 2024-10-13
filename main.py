#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

from clientes import *
from profesionales import *
from mascotas import *
from turnos import *
from informes import *

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

def main():

    #-------------------------------------------------
    # Inicialización de variables
    #-------------------------------------------------
    clientesGuardados = {
    "47294258": {
        "nombreCompleto": "Gaston Hirschbein",
        "genero": "masculino",
        "fechaNacimiento": "01/05/2003",
        "numeroTelefono": "3521521521",
        "domicilio": "Lago Puelo"
    },
    "42567432": {
        "nombreCompleto": "María López",
        "genero": "femenino",
        "fechaNacimiento": "12/11/1995",
        "numeroTelefono": "3516452145",
        "domicilio": "Córdoba"
    },
    "43781234": {
        "nombreCompleto": "Joaquín Pérez",
        "genero": "masculino",
        "fechaNacimiento": "07/03/1987",
        "numeroTelefono": "3547253121",
        "domicilio": "Rosario"
    },
    "45097234": {
        "nombreCompleto": "Lucía Fernández",
        "genero": "femenino",
        "fechaNacimiento": "21/08/1998",
        "numeroTelefono": "3517852145",
        "domicilio": "La Plata"
    },
    "41324567": {
        "nombreCompleto": "Carlos Gómez",
        "genero": "masculino",
        "fechaNacimiento": "19/02/1975",
        "numeroTelefono": "3541543265",
        "domicilio": "Mendoza"
    },
    "42987432": {
        "nombreCompleto": "Sofía Martínez",
        "genero": "femenino",
        "fechaNacimiento": "15/07/2000",
        "numeroTelefono": "3512589632",
        "domicilio": "Buenos Aires"
    },
    "43127654": {
        "nombreCompleto": "Juan González",
        "genero": "masculino",
        "fechaNacimiento": "30/06/1990",
        "numeroTelefono": "3541589632",
        "domicilio": "Tucumán"
    },
    "41725364": {
        "nombreCompleto": "Ana Rodríguez",
        "genero": "femenino",
        "fechaNacimiento": "04/12/1993",
        "numeroTelefono": "3517896541",
        "domicilio": "Salta"
    },
    "40985643": {
        "nombreCompleto": "Felipe Pérez",
        "genero": "masculino",
        "fechaNacimiento": "09/09/1985",
        "numeroTelefono": "3541856325",
        "domicilio": "San Juan"
    }}
    mascotasGuardadas = [{
        "documentoIdentidadDueño": "47294258",
        "nombre": "Michi",
        "especie": "gato",
        "razaAnimal": "Siames",
        "fechaNacimiento": "23/06/2014",
        "pesoKilogramos": 10
    },
    {
        "documentoIdentidadDueño": "47294258",
        "nombre": "Firulais",
        "especie": "perro",
        "razaAnimal": "Labrador",
        "fechaNacimiento": "12/01/2018",
        "pesoKilogramos": 25
    },
    {
        "documentoIdentidadDueño": "42567432",
        "nombre": "Pelusa",
        "especie": "gato",
        "razaAnimal": "Persa",
        "fechaNacimiento": "05/05/2016",
        "pesoKilogramos": 8
    },
    {
        "documentoIdentidadDueño": "43781234",
        "nombre": "Rex",
        "especie": "perro",
        "razaAnimal": "Pastor Alemán",
        "fechaNacimiento": "15/09/2015",
        "pesoKilogramos": 30
    },
    {
        "documentoIdentidadDueño": "45097234",
        "nombre": "Tom",
        "especie": "gato",
        "razaAnimal": "Angora",
        "fechaNacimiento": "11/11/2017",
        "pesoKilogramos": 9
    },
    {
        "documentoIdentidadDueño": "41324567",
        "nombre": "Duke",
        "especie": "perro",
        "razaAnimal": "Bulldog",
        "fechaNacimiento": "20/04/2014",
        "pesoKilogramos": 20
    },
    {
        "documentoIdentidadDueño": "42987432",
        "nombre": "Luna",
        "especie": "gato",
        "razaAnimal": "Siberiano",
        "fechaNacimiento": "30/10/2019",
        "pesoKilogramos": 6
    },
    {
        "documentoIdentidadDueño": "43127654",
        "nombre": "Max",
        "especie": "perro",
        "razaAnimal": "Golden Retriever",
        "fechaNacimiento": "18/07/2018",
        "pesoKilogramos": 28
    },
    {
        "documentoIdentidadDueño": "41725364",
        "nombre": "Nina",
        "especie": "perro",
        "razaAnimal": "Pug",
        "fechaNacimiento": "02/12/2017",
        "pesoKilogramos": 7
    },
    {
        "documentoIdentidadDueño": "40985643",
        "nombre": "Milo",
        "especie": "gato",
        "razaAnimal": "Bengala",
        "fechaNacimiento": "12/03/2016",
        "pesoKilogramos": 9
    }]
    profesionalesGuardados = {
    "47482192" :{
        "nombreCompleto": "Luis Marcelo Perez",
        "genero": "masculino",
        "especializacion": "veterinario",
        "fechaNacimiento": "08/04/1987",
        "domicilio": "Carabobo 82",
        "numeroTelefono" : "48391748",
        "horarioAtencion": "09:00 - 15:00",
        "activo" : True
    },
    "39645821": {
        "nombreCompleto": "Ana Gabriela Rodríguez",
        "genero": "femenino",
        "especializacion": "cirujana veterinaria",
        "fechaNacimiento": "12/11/1991",
        "domicilio": "Av. Siempre Viva 123",
        "numeroTelefono": "45318273",
        "horarioAtencion": "08:00 - 14:00",
        "activo": True
    },
    "38219476":{
        "nombreCompleto": "Carlos Esteban González",
        "genero": "masculino",
        "especializacion": "veterinario de pequeños animales",
        "fechaNacimiento": "04/07/1985",
        "domicilio": "Calle Falsa 456",
        "numeroTelefono": "45879123",
        "horarioAtencion": "10:00 - 18:00",
        "activo": False
    }}
    turnosProgramados = [{
        "documentoIdentidadCliente": "47294258",
        "indiceMascota": "0",
        "documentoIdentidadEspecialista": "47482192",
        "fecha": "21/06/2024",
        "horario": "09:00",
        "motivo": "operacion"
    }]

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

                    # solicitar informacion para crear un nuevo cliente
                    informacionCliente = informacionClienteNuevo(clientesGuardados)

                    #guardar la informacion del nuevo cliente en el diccionario
                    if informacionCliente:
                        guardarCliente(informacionCliente, clientesGuardados)

                elif opcion_clientes == "2": #modificar cliente

                    # solicitar informacion para modificar un cliente
                    informacionClienteModificar = modificarInformacionCliente(clientesGuardados)
                    
                    #guardar la informacion del cliente a modificar en el diccionario
                    if informacionClienteModificar:
                        guardarCliente(informacionClienteModificar, clientesGuardados)

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

                    # solicitar informacion para añadir una nueva mascota
                    infoMascotaNueva = informacionMascotaNueva(clientesGuardados)

                    # guardar la informacion de la nueva mascota en la lista
                    if infoMascotaNueva:
                        guardarMascotaNueva(infoMascotaNueva, mascotasGuardadas)

                elif opcion_mascotas == "2":
                    
                    # solicitar informacion para modificar una mascota  existente
                    infoMascotaModificar = modificarInformacionMascotaExistente(clientesGuardados, mascotasGuardadas)
                    
                    #guardar la informacion modificada sobre la mascota en la lista
                    if infoMascotaModificar:
                        guardarMascotaModificada(infoMascotaModificar, mascotasGuardadas)

                
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

                if opcion_profesionales == "1":

                    # solicitar informacion para añadir un nuevo profesional
                    infoNuevoProfesional = informacionProfesionalNuevo()
                    
                    #guardar la informaicon del profesional en el diccionario
                    if infoNuevoProfesional:
                        guardarInformacionProfesional(infoNuevoProfesional, profesionalesGuardados)

                elif opcion_profesionales == "2": #modificar profesional

                    #solicitar informacion para modificar un profesional existente
                    infoProfesionalModificar = modificarInformacionProfesional(profesionalesGuardados)
                    
                    #guardar la informacion del profesional a modificar en el diccionario
                    if infoProfesionalModificar:
                        guardarInformacionProfesional(infoProfesionalModificar, profesionalesGuardados)


                elif opcion_profesionales == "3": #eliminar profesional

                    # se elimina el profesional elegido del diccionario
                    eliminarProfesional(profesionalesGuardados)
                        
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
                    
                    #solicitar informacion para añadir un nuevo turno
                    infoTurnoNuevo = informacionTurnoCliente(clientesGuardados, mascotasGuardadas, profesionalesGuardados, turnosProgramados)
                    
                    # añadir el turno con la informacion en la lista
                    if infoTurnoNuevo:
                        añadirTurnoCliente(infoTurnoNuevo, turnosProgramados)


                elif opcion_turnos == "0":  # Volver al menú principal
                    break

        elif opcion_principal == "5":  # Submenú de informes
            while True:
                print("MENÚ INFORMES")
                print("[1] Turnos por profesional")
                print("[2] Turnos por mascota")
                print("[0] Volver al menú principal")

                opcion_informes = input("Seleccione una opción: ")

                if opcion_informes == "1":

                    desplegarTurnosPorProfesional(turnosProgramados, profesionalesGuardados)

                elif opcion_informes == "2":

                    desplegarTurnosPorMascota(mascotasGuardadas, turnosProgramados)

                elif opcion_informes == "3":

                    fechaInicio = input("Fecha de inicio: ")
                    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
                    while not re.match(patronFecha, fechaInicio):
                        print("El formato o la fecha es incorrecta.")
                        fechaInicio = input("Fecha de inicio: ")

                    fechaFinal = input("Fecha de fin: ")
                    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
                    while not re.match(patronFecha, fechaFinal):
                        print("El formato o la fecha es incorrecta.")
                        fechaFinal = input("Fecha de fin: ")


                    mostrarTurnosPorFecha(turnosProgramados, fechaInicio, fechaFinal)
            
        elif opcion_principal == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

        
        opcion_principal = ""

# Punto de entrada al programa
main()
