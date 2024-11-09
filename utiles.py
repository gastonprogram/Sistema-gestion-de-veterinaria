import json
import re

from datetime import datetime

def verificarDocumento(_rutaArchivo: str, _repetido: bool):
    try:
        archivoLeer = open(_rutaArchivo, "r", encoding="utf-8")
        registrosGuardados = json.load(archivoLeer)
        
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return False
    
    finally:
        try:
            archivoLeer.close()
        except:
            pass

    while True:
        documentoIdentidad = input("Ingrese DNI: ")
        
        if documentoIdentidad in registrosGuardados:
            if not _repetido:
                print("DNI ya registrado.")
                res = menuDecision()
                if res == -1:
                    return -1  
            else:
                return documentoIdentidad
        else:
            if _repetido:
                print("DNI no registrado.")
                res = menuDecision()
                if res == -1:
                    return -1  
            else:
                return documentoIdentidad


def menuDecision():
    while True:
        decision = input("Seleccione:\n[1] Ingresar DNI nuevamente\n[2] Regresar al menú\nElegir una opción: ")
        
        if decision == "1":
            return 1
        elif decision == "2":
            print("-" * 50)
            print("Volviendo al menú...")
            print("-" * 50)
            return -1
        else:
            print("Ha seleccionado una opción incorrecta.")


def elegirGenero() -> str :
    
    while True:
        try:
            genero = int(input("Genero ([0]Masculino / [1]Femenino): "))

            if genero == 0:
                genero = "Masculino"
                break
            
            elif genero == 1:
                genero = "Femenino"
                break

            else:
                print("El valor ingresado debe ser 0 o 1.")
                print("Intente nuevamente.")

        except ValueError:
            print("El valor ingresado debe ser un número entero (0 o 1).")
            print("Intente nuevamente.")
    
    return genero


def ingresarNombre() -> str:
    patronNombre = "^[^\W\d_]+(\s[^\W\d_]+)*$"
    
    while True:
        try:
            nombreCompleto = input("Nombre completo (menor a 60 caracteres): ")
            
            #el nombre no cumple con el patron o longitud
            if not re.match(patronNombre, nombreCompleto) or len(nombreCompleto) > 60:
                print("El formato o longitud es incorrecto.")
                print("Intente nuevamente.")
            
            #el nombre es correcto
            else:
                break
                
        except:
            pass
        
    #devolver el nombre con formato correcto
    return nombreCompleto.lower().title()

def ingresarFechaNacimiento() -> str:
    
    patronFechaNacimiento = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
    
    while True:
        try:
            fechaNacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")
            
            if not re.match(patronFechaNacimiento, fechaNacimiento):
                print("El formato o la fecha es incorrecta.")
                print("Intente nuevamente.")
                
            else: break
            
        except:
            pass
        
    return fechaNacimiento

def ingresarNumeroTelefono() -> str:
    patronNumeroTel = "^\+?(\d{1,4})?[-.\s]?(\(?\d{1,4}\)?)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    
    while True:
        try:
            numeroTelefono = input("Numero de telefono: ")
            
            if not re.match(patronNumeroTel, numeroTelefono):
                print("El formato o el numero es incorrecto.")
                print("Intente nuevamente.")
        except:
            pass
        
def ingresarFecha():
    
    patronFecha = "^(0[1-9]|[12]\d|3[01])/(0[13578]|1[02])/(19\d{2}|20\d{2})$|^(0[1-9]|[12]\d|30)/(0[13456789]|1[012])/(19\d{2}|20\d{2})$|^(0[1-9]|1\d|2[0-8])/02/(19\d{2}|20\d{2})$|^29/02/(19([02468][048]|[13579][26])|20([02468][048]|[13579][26]))$"
            
    while True:
        fecha = input("Ingrese la nueva fecha (DD/MM/AAAA): ")
        
        if re.match(patronFecha, fecha):
            fecha_ingresada = datetime.strptime(fecha, "%d/%m/%Y")
            fecha_actual = datetime.now()

            #la fecha es correcta y termina la funcion
            if fecha_ingresada > fecha_actual:
                return fecha
            else:
                print("La fecha ingresada es anterior a la fecha actual. Intente de nuevo.")
        else:
            print("El formato o la fecha es incorrecta. Intente de nuevo.")


def seleccionarHorario(turnosGuardados, turnoSeleccionado, profesionalesGuardados):
    """
    Filtra y muestra los horarios disponibles para la fecha y el profesional seleccionados.
    """
    documentoProfesional = turnoSeleccionado['documentoIdentidadProfesional']
    horarios = profesionalesGuardados[documentoProfesional]["horarioAtencion"]
    
    # Obtener el rango de horas
    horario_inicio = int(horarios[:2])
    horario_fin = int(horarios[8:10])
    horariosDisponibles = [f"{hora:02d}:00" for hora in range(horario_inicio, horario_fin)]

    # Filtrar horarios ocupados
    for turno in turnosGuardados:
        if turno['fecha'] == turnoSeleccionado['fecha'] and turno['documentoIdentidadProfesional'] == documentoProfesional:
            if turno['horario'] in horariosDisponibles:
                horariosDisponibles.remove(turno['horario'])

    # Mostrar y seleccionar horario disponible
    print("Horarios disponibles:")
    for i, horario in enumerate(horariosDisponibles):
        print(f"[{i}] {horario}")

    seleccion = int(input("Seleccione un nuevo horario: "))
    while seleccion < 0 or seleccion >= len(horariosDisponibles):
        seleccion = int(input("Seleccione una opción válida: "))

    return horariosDisponibles[seleccion]