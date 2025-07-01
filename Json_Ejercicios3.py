#crear JSON con deportes como claves
import json, os

def json_por_deporte():
    ruta = "c:/Users/eduar/OneDrive/Documents/GestionArchivos_Ejercicios/"
    os.makedirs(ruta, exist_ok=True)

    archivo_entrada = input("Nombre del archivo JSON de entrada (ej: personas.json): ")
    entrada_path = os.path.join(ruta, archivo_entrada)
    salida_path = os.path.join(ruta, "deportes.json")

    try:
        with open(entrada_path, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

        deportes = {}
        for username, p in data.items():
            for d in p["deportes"]:
                deportes.setdefault(d, []).append(username)

        with open(salida_path, "w", encoding="utf-8") as out:
            json.dump(deportes, out, indent=4, ensure_ascii=False)

        print("Archivo 'deportes.json' creado correctamente.")
    
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except json.JSONDecodeError:
        print("El archivo contiene un JSON inválido.")

json_por_deporte()
