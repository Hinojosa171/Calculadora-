def division(a, b):
    """Divide dos números sin usar el operador '/'."""
    if b == 0:
        print("Error: División entre cero.")
        return None

    c = 0
    temp_a = abs(a)
    temp_b = abs(b)

    while temp_a >= temp_b:
        temp_a -= temp_b
        c += 1

    # Determinar el signo del resultado
    signo_negativo = False
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        signo_negativo = True

    return -c if signo_negativo else c