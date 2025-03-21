from operations.suma import suma
from operations.resta import resta
from operations.multiplicacion import multiplicacion
from operations.division import division

def validar_entero(valor):
    """Valida que la entrada sea un número entero."""
    try:
        return int(valor)
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return None

def main():
    """Función principal que ejecuta la calculadora."""
    operations = {
        "suma": suma,
        "resta": resta,
        "multiplicacion": multiplicacion,
        "division": division,
    }

    print("Bienvenido a la Calculadora sin Operadores Aritméticos")
    while True:
        # Paso 1: Selección de operación
        operacion = input(
            "Seleccione operación (suma, resta, multiplicacion, division, salir): "
        ).strip().lower()

        if operacion == "salir":
            print("¡Hasta luego!")
            break

        if operacion not in operations:
            print("Operación no válida. Intente nuevamente.")
            continue

        # Paso 2: Entrada de números
        a = validar_entero(input("Ingrese el primer número: "))
        if a is None:
            continue

        b = validar_entero(input("Ingrese el segundo número: "))
        if b is None:
            continue

        # Paso 3: Cálculo del resultado
        funcion = operations[operacion]
        c = funcion(a, b)  # Guardamos el resultado en la variable 'c'

        # Paso 4: Salida del resultado
        if c is not None:
            print(f"El resultado es: {c}")

if __name__ == "__main__":
    main()