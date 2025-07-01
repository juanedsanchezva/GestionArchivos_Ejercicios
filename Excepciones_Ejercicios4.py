#Acceso a una clave inexistente en un diccionario
def ejercicio_4():
    datos = {
        'Juan': 'Java',
        'David': 'C',
        'Mateo': 'Python'
    }

    try:
        print(datos['Ada'])  # 'Ada' no existe
    except KeyError:
        print("❗ Llave inexistente en el diccionario")

ejercicio_4()
