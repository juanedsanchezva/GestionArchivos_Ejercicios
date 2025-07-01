#compras realizadas en un pais
import csv
import os

def total_compras_por_pais():
    ruta = "c:/Users/eduar/OneDrive/Documents/GestionArchivos_Ejercicios/SalesJan2009.csv"

    if not os.path.exists(ruta):
        print("Archivo no encontrado.")
        return

    pais_input = input("Ingrese el país (ej. Colombia): ").strip().lower()
    total = 0

    try:
        with open(ruta, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["Pais"].strip().lower() == pais_input:
                    total += int(fila["Total_Compras"])

        print(f"Total de compras realizadas en '{pais_input.title()}': {total}")

    except KeyError:
        print("Verifica que las columnas del CSV estén bien escritas (ej. 'Pais', 'Total_Compras').")
    except Exception as e:
        print("Error al procesar el archivo:", e)

total_compras_por_pais()
