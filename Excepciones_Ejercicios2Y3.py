#Suma entre int y str

def operar(a, b):
    return a + b

def ejercicio_2_3():
    try:
        a = int(input("Ingrese un número entero: "))
        b = 'hola'
        resultado = operar(a, b)  # Esto genera TypeError
        print(resultado)
    except TypeError:
        print("❗ Error: estás sumando tipos incompatibles (int + str)")

ejercicio_2_3()