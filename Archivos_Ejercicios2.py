#compras realizadas por un metodo de pago
import csv
import os

def total_compras_por_pago():
    ruta = "c:/Users/eduar/OneDrive/Documents/GestionArchivos_Ejercicios/SalesJan2009.csv"

    if not os.path.exists(ruta):
        print("Archivo no encontrado.")
        return

    metodo = input("Ingrese el método de pago (ej. Visa): ").strip().lower()
    total = 0

    try:
        with open(ruta, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["Tipo_de_pago"].strip().lower() == metodo:
                    total += int(fila["Total_Compras"])

        print(f"Total de compras con método '{metodo.title()}': {total}")

    except KeyError:
        print("Las columnas deben llamarse 'Tipo_de_pago' y 'Total_Compras'.")
    except Exception as e:
        print("Error al procesar el archivo:", e)

total_compras_por_pago()
