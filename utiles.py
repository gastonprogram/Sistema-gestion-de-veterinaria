import json

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
