def suma(a, b):
    """Suma dos números sin usar el operador '+'."""
    # Usamos una lista c para almacenar el proceso y resultado
    c = []
    
    # Procesamos el primer número
    if a >= 0:
        for _ in range(a):
            c.append(1)  # Agregamos 'a' elementos si es positivo
    else:
        # Calculamos valor absoluto manualmente sin usar abs()
        a_abs = -a
        for _ in range(a_abs):
            c.append(-1)  # Agregamos 'a' elementos negativos si es negativo
    
    # Procesamos el segundo número
    if b >= 0:
        for _ in range(b):
            c.append(1)  # Agregamos 'b' elementos si es positivo
    else:
        # Calculamos valor absoluto manualmente sin usar abs()
        b_abs = -b
        for _ in range(b_abs):
            c.append(-1)  # Agregamos 'b' elementos negativos si es negativo
    
    # Calculamos el resultado contando los elementos positivos y negativos
    resultado = 0
    for elemento in c:
        if elemento == 1:
            resultado = resultado + 1
        else:  # elemento == -1
            resultado = resultado - 1
    
    return resultado