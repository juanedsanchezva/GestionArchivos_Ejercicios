# Mostrar personas en un rango de edad con JSON válido
import json, os

def personas_por_rango_edad():
    ruta = "c:/Users/eduar/OneDrive/Documents/GestionArchivos_Ejercicios/"
    os.makedirs(ruta, exist_ok=True)

    archivo_json = input("Nombre del archivo JSON de entrada (ej. personas.json): ")
    archivo_path = os.path.join(ruta, archivo_json)

    try:
        min_edad = int(input("Edad mínima: "))
        max_edad = int(input("Edad máxima: "))

        with open(archivo_path, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

        resultados = [
            f"{p['nombres']} {p['apellidos']}"
            for p in data.values()
            if min_edad <= p["edad"] <= max_edad
        ]

        if resultados:
            print("\n Personas encontradas:")
            for nombre in resultados:
                print("•", nombre)
        else:
            print("⚠️ No se encontraron personas en ese rango.")

        salida = os.path.join(ruta, "personas_por_rango.json")
        with open(salida, "w", encoding="utf-8") as out:
            json.dump(resultados, out, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except json.JSONDecodeError:
        print("El archivo no contiene un JSON válido.")
    except ValueError:
        print("Debes ingresar edades como números.")

personas_por_rango_edad()
