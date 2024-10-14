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
    "30111222": {
        "nombreCompleto": "Juan Perez",
        "genero": "Masculino",
        "fechaNacimiento": "15/03/1985",
        "numeroTelefono": "+5491167886543",
        "domicilio": "Av. Corrientes 1234"
    },
    "30222333": {
        "nombreCompleto": "Maria Gonzalez",
        "genero": "Femenino",
        "fechaNacimiento": "22/07/1990",
        "numeroTelefono": "+5491167896543",
        "domicilio": "Calle Falsa 123"
    },
    "30333444": {
        "nombreCompleto": "Carlos Lopez",
        "genero": "Masculino",
        "fechaNacimiento": "30/11/1978",
        "numeroTelefono": "+5491167886544",
        "domicilio": "Calle Siempre Viva 742"
    },
    "30444555": {
        "nombreCompleto": "Ana Martinez",
        "genero": "Femenino",
        "fechaNacimiento": "10/04/1989",
        "numeroTelefono": "+5491167896544",
        "domicilio": "San Juan 456"
    },
    "30555666": {
        "nombreCompleto": "Roberto Diaz",
        "genero": "Masculino",
        "fechaNacimiento": "01/02/1982",
        "numeroTelefono": "+5491167886545",
        "domicilio": "Av. Libertador 4567"
    },
    "30666777": {
        "nombreCompleto": "Laura Sanchez",
        "genero": "Femenino",
        "fechaNacimiento": "18/09/1991",
        "numeroTelefono": "+5491167896545",
        "domicilio": "Av. Rivadavia 7890"
    },
    "30777888": {
        "nombreCompleto": "Sofia Gutierrez",
        "genero": "Femenino",
        "fechaNacimiento": "05/12/1995",
        "numeroTelefono": "+5491167886546",
        "domicilio": "Calle Mitre 123"
    },
    "30888999": {
        "nombreCompleto": "Luis Romero",
        "genero": "Masculino",
        "fechaNacimiento": "23/06/1976",
        "numeroTelefono": "+5491167896546",
        "domicilio": "Pueyrredón 456"
    },
    "30999000": {
        "nombreCompleto": "Marta Fernandez",
        "genero": "Femenino",
        "fechaNacimiento": "11/05/1987",
        "numeroTelefono": "+5491167886547",
        "domicilio": "Santa Fe 789"
    },
    "30100111": {
        "nombreCompleto": "Jorge Alvarez",
        "genero": "Masculino",
        "fechaNacimiento": "20/01/1980",
        "numeroTelefono": "+5491167896547",
        "domicilio": "Belgrano 1234"
    },
    "31000222": {
        "nombreCompleto": "Julia Herrera",
        "genero": "Femenino",
        "fechaNacimiento": "27/03/1992",
        "numeroTelefono": "+5491167886548",
        "domicilio": "Dorrego 5678"
    },
    "31111333": {
        "nombreCompleto": "Diego Rodriguez",
        "genero": "Masculino",
        "fechaNacimiento": "13/10/1983",
        "numeroTelefono": "+5491167896548",
        "domicilio": "Corrientes 912"
    },
    "31222444": {
        "nombreCompleto": "Patricia Castro",
        "genero": "Femenino",
        "fechaNacimiento": "30/06/1990",
        "numeroTelefono": "+5491167886549",
        "domicilio": "Sarmiento 123"
    },
    "31333555": {
        "nombreCompleto": "Oscar Ruiz",
        "genero": "Masculino",
        "fechaNacimiento": "08/11/1975",
        "numeroTelefono": "+5491167896549",
        "domicilio": "Maipú 456"
    },
    "31444666": {
        "nombreCompleto": "Carla Morales",
        "genero": "Femenino",
        "fechaNacimiento": "15/04/1993",
        "numeroTelefono": "+5491167886550",
        "domicilio": "Alberdi 789"
    }
}

    mascotasGuardadas = [
    {
        "documentoIdentidadDueño": "30111222",
        "nombre": "Max",
        "especie": "Perro",
        "razaAnimal": "Labrador",
        "fechaNacimiento": "01/01/2020",
        "pesoKilogramos": 30.5
    },
    {
        "documentoIdentidadDueño": "30111222",
        "nombre": "Bella",
        "especie": "Perro",
        "razaAnimal": "Bulldog",
        "fechaNacimiento": "15/05/2019",
        "pesoKilogramos": 25.0
    },
    {
        "documentoIdentidadDueño": "30222333",
        "nombre": "Whiskers",
        "especie": "Gato",
        "razaAnimal": "Siamés",
        "fechaNacimiento": "22/07/2021",
        "pesoKilogramos": 5.0
    },
    {
        "documentoIdentidadDueño": "30222333",
        "nombre": "Fluffy",
        "especie": "Gato",
        "razaAnimal": "Persa",
        "fechaNacimiento": "10/10/2020",
        "pesoKilogramos": 7.0
    },
    {
        "documentoIdentidadDueño": "30222333",
        "nombre": "Rocky",
        "especie": "Perro",
        "razaAnimal": "Caniche",
        "fechaNacimiento": "18/08/2018",
        "pesoKilogramos": 10.0
    },
    {
        "documentoIdentidadDueño": "30333444",
        "nombre": "Mittens",
        "especie": "Gato",
        "razaAnimal": "Maine Coon",
        "fechaNacimiento": "12/02/2019",
        "pesoKilogramos": 8.0
    },
    {
        "documentoIdentidadDueño": "30333444",
        "nombre": "Buddy",
        "especie": "Perro",
        "razaAnimal": "Golden Retriever",
        "fechaNacimiento": "05/04/2017",
        "pesoKilogramos": 35.0
    },
    {
        "documentoIdentidadDueño": "30444555",
        "nombre": "Ginger",
        "especie": "Gato",
        "razaAnimal": "Bengala",
        "fechaNacimiento": "30/09/2022",
        "pesoKilogramos": 4.5
    },
    {
        "documentoIdentidadDueño": "30555666",
        "nombre": "Rex",
        "especie": "Perro",
        "razaAnimal": "Pastor Alemán",
        "fechaNacimiento": "14/11/2018",
        "pesoKilogramos": 40.0
    },
    {
        "documentoIdentidadDueño": "30666777",
        "nombre": "Nina",
        "especie": "Gato",
        "razaAnimal": "Persa",
        "fechaNacimiento": "23/03/2023",
        "pesoKilogramos": 4.0
    },
    {
        "documentoIdentidadDueño": "30777888",
        "nombre": "Charlie",
        "especie": "Perro",
        "razaAnimal": "Bulldog",
        "fechaNacimiento": "08/12/2020",
        "pesoKilogramos": 28.0
    },
    {
        "documentoIdentidadDueño": "30888999",
        "nombre": "Simba",
        "especie": "Gato",
        "razaAnimal": "Siamés",
        "fechaNacimiento": "19/01/2021",
        "pesoKilogramos": 6.5
    },
    {
        "documentoIdentidadDueño": "30999000",
        "nombre": "Coco",
        "especie": "Perro",
        "razaAnimal": "Chihuahua",
        "fechaNacimiento": "15/07/2019",
        "pesoKilogramos": 3.0
    },
    {
        "documentoIdentidadDueño": "31000222",
        "nombre": "Luna",
        "especie": "Gato",
        "razaAnimal": "Maine Coon",
        "fechaNacimiento": "20/08/2022",
        "pesoKilogramos": 7.5
    },
    {
        "documentoIdentidadDueño": "31111333",
        "nombre": "Rocky",
        "especie": "Perro",
        "razaAnimal": "Beagle",
        "fechaNacimiento": "12/12/2020",
        "pesoKilogramos": 12.0
    },
    {
        "documentoIdentidadDueño": "31222444",
        "nombre": "Toby",
        "especie": "Perro",
        "razaAnimal": "Buldog Francés",
        "fechaNacimiento": "01/05/2019",
        "pesoKilogramos": 9.0
    },
    {
        "documentoIdentidadDueño": "31333555",
        "nombre": "Sasha",
        "especie": "Gato",
        "razaAnimal": "Siamés",
        "fechaNacimiento": "17/02/2023",
        "pesoKilogramos": 4.2
    },
    {
        "documentoIdentidadDueño": "31444666",
        "nombre": "Oscar",
        "especie": "Perro",
        "razaAnimal": "Cocker Spaniel",
        "fechaNacimiento": "25/06/2021",
        "pesoKilogramos": 10.5
    }
]

    profesionalesGuardados = {
    "20221111": {
        "nombreCompleto": "Pedro Alvarez",
        "genero": "Masculino",
        "especializacion": "Veterinario",
        "fechaNacimiento": "15/04/1985",
        "domicilio": "Calle de la Salud 123",
        "numeroTelefono": "+5491161234567",
        "horarioAtencion": "09:00 - 17:00",
        "activo": True
    },
    "20222222": {
        "nombreCompleto": "Ana López",
        "genero": "Femenino",
        "especializacion": "Veterinaria especializada en felinos",
        "fechaNacimiento": "25/12/1990",
        "domicilio": "Av. de los Gatos 456",
        "numeroTelefono": "+5491162345678",
        "horarioAtencion": "10:00 - 18:00",
        "activo": True
    },
    "20233333": {
        "nombreCompleto": "Carlos Ramirez",
        "genero": "Masculino",
        "especializacion": "Veterinario especializado en caninos",
        "fechaNacimiento": "05/06/1988",
        "domicilio": "Calle Canina 789",
        "numeroTelefono": "+5491163456789",
        "horarioAtencion": "08:00 - 16:00",
        "activo": True
    },
    "20244444": {
        "nombreCompleto": "Sofía Martínez",
        "genero": "Femenino",
        "especializacion": "Veterinaria general",
        "fechaNacimiento": "14/02/1992",
        "domicilio": "Calle de los Animales 321",
        "numeroTelefono": "+5491164567890",
        "horarioAtencion": "11:00 - 19:00",
        "activo": False
    },
    "20255555": {
        "nombreCompleto": "Jorge Torres",
        "genero": "Masculino",
        "especializacion": "Veterinario cirujano",
        "fechaNacimiento": "30/10/1980",
        "domicilio": "Av. de la Medicina 654",
        "numeroTelefono": "+5491165678901",
        "horarioAtencion": "07:00 - 15:00",
        "activo": True
    }
}
    
    turnosProgramados = [
    {
        "documentoIdentidadCliente": "30111222",
        "indiceMascota": 0,
        "documentoIdentidadEspecialista": "30123456",
        "fecha": "10/10/2024",
        "horario": "10:00",
        "motivo": "Consulta general",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30222333",
        "indiceMascota": 1,
        "documentoIdentidadEspecialista": "30223456",
        "fecha": "11/10/2024",
        "horario": "11:00",
        "motivo": "Vacunación",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30333444",
        "indiceMascota": 2,
        "documentoIdentidadEspecialista": "30323456",
        "fecha": "12/10/2024",
        "horario": "12:00",
        "motivo": "Chequeo anual",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30444555",
        "indiceMascota": 3,
        "documentoIdentidadEspecialista": "30423456",
        "fecha": "13/10/2024",
        "horario": "13:00",
        "motivo": "Consulta por alergias",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30555666",
        "indiceMascota": 4,
        "documentoIdentidadEspecialista": "30523456",
        "fecha": "14/10/2024",
        "horario": "14:00",
        "motivo": "Control de peso",
        "activo": True
    },

    {
        "documentoIdentidadCliente": "30666777",
        "indiceMascota": 5,
        "documentoIdentidadEspecialista": "30623456",
        "fecha": "15/10/2024",
        "horario": "09:00",
        "motivo": "Consulta general",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30777888",
        "indiceMascota": 6,
        "documentoIdentidadEspecialista": "30723456",
        "fecha": "16/10/2024",
        "horario": "10:00",
        "motivo": "Vacunación",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30888999",
        "indiceMascota": 7,
        "documentoIdentidadEspecialista": "30823456",
        "fecha": "17/10/2024",
        "horario": "11:00",
        "motivo": "Chequeo anual",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30999000",
        "indiceMascota": 8,
        "documentoIdentidadEspecialista": "30923456",
        "fecha": "18/10/2024",
        "horario": "12:00",
        "motivo": "Consulta por alergias",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30100111",
        "indiceMascota": 9,
        "documentoIdentidadEspecialista": "30123456",
        "fecha": "19/10/2024",
        "horario": "13:00",
        "motivo": "Control de peso",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "31000222",
        "indiceMascota": 0,
        "documentoIdentidadEspecialista": "30223456",
        "fecha": "20/10/2024",
        "horario": "14:00",
        "motivo": "Consulta general",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "31111333",
        "indiceMascota": 1,
        "documentoIdentidadEspecialista": "30323456",
        "fecha": "21/10/2024",
        "horario": "09:00",
        "motivo": "Vacunación",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "31222444",
        "indiceMascota": 2,
        "documentoIdentidadEspecialista": "30423456",
        "fecha": "22/10/2024",
        "horario": "10:00",
        "motivo": "Chequeo anual",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "31333555",
        "indiceMascota": 3,
        "documentoIdentidadEspecialista": "30523456",
        "fecha": "23/10/2024",
        "horario": "11:00",
        "motivo": "Consulta por alergias",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "31444666",
        "indiceMascota": 4,
        "documentoIdentidadEspecialista": "30623456",
        "fecha": "24/10/2024",
        "horario": "12:00",
        "motivo": "Control de peso",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30111222",
        "indiceMascota": 5,
        "documentoIdentidadEspecialista": "30723456",
        "fecha": "25/10/2024",
        "horario": "13:00",
        "motivo": "Consulta general",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30222333",
        "indiceMascota": 6,
        "documentoIdentidadEspecialista": "30823456",
        "fecha": "26/10/2024",
        "horario": "14:00",
        "motivo": "Vacunación",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30333444",
        "indiceMascota": 7,
        "documentoIdentidadEspecialista": "30923456",
        "fecha": "27/10/2024",
        "horario": "09:00",
        "motivo": "Chequeo anual",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30444555",
        "indiceMascota": 8,
        "documentoIdentidadEspecialista": "30123456",
        "fecha": "28/10/2024",
        "horario": "10:00",
        "motivo": "Consulta por alergias",
        "activo": True
    },
    {
        "documentoIdentidadCliente": "30555666",
        "indiceMascota": 9,
        "documentoIdentidadEspecialista": "30223456",
        "fecha": "29/10/2024",
        "horario": "11:00",
        "motivo": "Control de peso",
        "activo": True
    }
]


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


                if opcion_turnos == "2":

                    #solicitar informacion para modificar un turno
                    infoTurnoModificado = modificarTurnoCliente(turnosProgramados, clientesGuardados, profesionalesGuardados)

                    #guardar la informacion del turno a modificar en la lista
                    if infoTurnoModificado:
                        guardarTurnoModificado(infoTurnoModificado, turnosProgramados)

                if opcion_turnos == "2":

                    cancelarTurnoCliente(turnosProgramados, clientesGuardados)

                elif opcion_turnos == "0":  # Volver al menú principal
                    break

        elif opcion_principal == "5":  # Submenú de informes
            while True:
                print("MENÚ INFORMES")
                print("[1] Turnos por profesional")
                print("[2] Turnos por mascota")
                print("[3] Turnos en un rango de dias")
                print("[4] Turnos en un rango de horas")
                print("[0] Volver al menú principal")

                opcion_informes = input("Seleccione una opción: ")

                if opcion_informes == "1":

                    #mostrar turnos en los que se encuentra un profesional en especifico 
                    desplegarTurnosPorProfesional(turnosProgramados, profesionalesGuardados)

                elif opcion_informes == "2":
                    #mostrar los turnos en los que se encuentra una mascota en especifica
                    desplegarTurnosPorMascota(mascotasGuardadas, turnosProgramados,clientesGuardados)

                elif opcion_informes == "3":

                    
                    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
                    fechaInicio = input("Fecha de inicio: ")
                    while not re.match(patronFecha, fechaInicio):
                        print("El formato o la fecha es incorrecta.")
                        fechaInicio = input("Fecha de inicio: ")

                    fechaFinal = input("Fecha de fin: ")
                    while not re.match(patronFecha, fechaFinal):
                        print("El formato o la fecha es incorrecta.")
                        fechaFinal = input("Fecha de fin: ")


                    mostrarTurnosPorFecha(turnosProgramados, fechaInicio, fechaFinal)
                
                
                elif opcion_informes == "4":


                    patronHorario = "^(0[0-9]|1[0-9]|2[0-3]):00$"

                    horarioInicio = input("Horario de inicio (HH:00): ")
                    while not re.match(patronHorario, horarioInicio):
                        print("El formato o la fecha es incorrecta.")
                        horarioInicio = input("Horario de inicio (HH:00): ")

                    horarioFinal = input("Horario final (HH:00): ")
                    while not re.match(patronHorario, horarioFinal):
                        print("El formato o la fecha es incorrecta.")
                        horarioFinal = input("Horario final (HH:00): ")

                    horaInicioRecortado = horarioInicio[:2]
                    horaFinalRecortado = horarioFinal[:2]
                    print(horaInicioRecortado, horaFinalRecortado)

                    fecha = input("Fecha (DD/MM/AAAA): ")
                    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
                    while not re.match(patronFecha, fechaInicio):
                        print("El formato o la fecha es incorrecta.")
                        fechaInicio = input("Fecha (DD/MM/AAAA): ")

                    mostrarTurnosPorFechaYHorarios(turnosProgramados, fecha, horaInicioRecortado, horaFinalRecortado)
                
                elif opcion_turnos == "0":  # Volver al menú principal
                    break
            
        elif opcion_principal == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

        
        opcion_principal = ""

# Punto de entrada al programa
main()
