def multiplicacion(a, b):
    """Multiplica dos números sin usar el operador '*'."""
    # Usamos una lista c para almacenar el proceso y resultado
    c = []
    
    # Calculamos valores absolutos manualmente sin usar abs()
    abs_a = a if a >= 0 else -a
    abs_b = b if b >= 0 else -b
    
    # Realizamos la multiplicación agregando elementos a la lista c
    for _ in range(abs_a):
        for _ in range(abs_b):
            c.append(1)
    
    # Determinamos el signo del resultado
    resultado = len(c)
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        # Si uno de los números es negativo, el resultado es negativo
        resultado_final = 0
        for _ in range(resultado):
            resultado_final = resultado_final - 1
    else:
        # Si ambos son positivos o ambos negativos, el resultado es positivo
        resultado_final = 0
        for _ in range(resultado):
            resultado_final = resultado_final + 1
    
    return resultado_final