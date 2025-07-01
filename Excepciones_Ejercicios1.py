#Acceso a una posición inexistente en una lista

def ejercicio1():
    lista = [1, 2, 3, 4]
    try:
        print(lista[5])  # Índice inválido
    except IndexError:
        print("❗ Intenta acceder una posición que no está en la lista")

ejercicio1()
