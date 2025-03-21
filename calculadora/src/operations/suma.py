def suma(a, b):
    """Suma dos números sin usar el operador '+'."""
    c = []
    if a > 0:
        for _ in range(a):
            c.append(1)  # Agregamos 'a' elementos
    else:
        for _ in range(-a):
            c.pop() if c else None  # Restamos 'a' elementos si es negativo

    if b > 0:
        for _ in range(b):
            c.append(1)  # Agregamos 'b' elementos
    else:
        for _ in range(-b):
            c.pop() if c else None  # Restamos 'b' elementos si es negativo

    return len(c) if c else 0