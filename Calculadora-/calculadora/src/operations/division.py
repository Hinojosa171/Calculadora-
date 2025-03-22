def division(a, b):
    """Divide dos números sin usar el operador '/'."""
    if b == 0:
        print("Error: División entre cero.")
        return None
    
    # Usamos una lista c para almacenar el proceso y resultado
    c = []
    
    # Calculamos valores absolutos manualmente sin usar abs()
    abs_a = a if a >= 0 else -a
    abs_b = b if b >= 0 else -b
    
    # Realizamos la división contando cuántas veces podemos restar b de a
    contador = 0
    temp = 0
    while temp < abs_a:
        temp_anterior = temp
        # Sumamos abs_b a temp
        for _ in range(abs_b):
            temp = temp + 1
        
        # Si nos pasamos, salimos del bucle
        if temp > abs_a:
            temp = temp_anterior
            break
        
        contador = contador + 1
        c.append(1)  # Agregamos un elemento por cada vez que b cabe en a
    
    # Determinamos el signo del resultado
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        # Si uno de los números es negativo, el resultado es negativo
        resultado = 0
        for _ in range(contador):
            resultado = resultado - 1
    else:
        # Si ambos son positivos o ambos negativos, el resultado es positivo
        resultado = 0
        for _ in range(contador):
            resultado = resultado + 1
    
    return resultado