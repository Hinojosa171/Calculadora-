def multiplicacion(a, b):
    """Multiplica dos números sin usar el operador '*'."""
    c = []
    for _ in range(abs(a)):
        for _ in range(abs(b)):
            c.append(1)  # Agregar 'a' veces 'b' elementos

    # Determinar el signo del resultado
    signo_negativo = False
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        signo_negativo = True

    return -len(c) if signo_negativo else len(c)