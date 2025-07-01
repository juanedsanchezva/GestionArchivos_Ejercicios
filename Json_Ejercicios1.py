#Mostrar personas que practican un deporte 
import json, os

def personas_que_practican():
    ruta = "c:/Users/eduar/OneDrive/Documents/GestionArchivos_Ejercicios/"
    os.makedirs(ruta, exist_ok=True)

    archivo_json = input("Nombre del archivo JSON de entrada (ej. personas.json): ")
    deporte = input("Ingrese el deporte a buscar: ")

    ruta_completa = os.path.join(ruta, archivo_json)

    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            resultados = [
                f"{p['nombres']} {p['apellidos']}"
                for p in data.values()
                if deporte.lower() in [d.lower() for d in p["deportes"]]
            ]

        if resultados:
            for nombre in resultados:
                print("✅", nombre)
        else:
            print("No se encontraron personas que practiquen ese deporte.")

        # Guardar resultados
        with open(os.path.join(ruta, "personas_que_practican.json"), "w", encoding="utf-8") as out:
            json.dump(resultados, out, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except json.JSONDecodeError:
        print("El archivo no contiene un JSON válido.")

personas_que_practican()