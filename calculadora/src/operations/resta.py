def resta(a, b):
    """Resta dos números sin usar el operador '-'."""
    c = [1] * abs(a)  # Creamos una lista con 'a' elementos

    if b > 0:
        for _ in range(b):
            if c:
                c.pop()  # Eliminamos un elemento
    else:
        for _ in range(-b):
            c.append(1)  # Agregamos un elemento si 'b' es negativo

    return len(c) if c else 0