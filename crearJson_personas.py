import json

personas = {
    "angvasquez": {
        "nombres": "Angelo Jose",
        "apellidos": "Vasquez",
        "edad": 15,
        "colombiano": True,
        "deportes": ["Futbol", "Ajedrez", "ultimate"]
    },
    "juasanchezva": {
        "nombres": "Juan Eduardo",
        "apellidos": "Sanchez Vasquez",
        "edad": 18,
        "colombiano": False,
        "deportes": ["Baloncesto", "futbol", "volleyball"]
    }
}

ruta = "c:/Users/eduar/OneDrive/Documents/GestionArchivos_Ejercicios/personas.json"

with open(ruta, "w", encoding="utf-8") as archivo:
    json.dump(personas, archivo, indent=4, ensure_ascii=False)

print("✅ Archivo personas.json recreado exitosamente.")