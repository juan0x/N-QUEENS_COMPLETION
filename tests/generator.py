import random

def generar_tablero_aleatorio(n, num_reinas_iniciales):
    """
    Se genera una configuración inicial aleatoria de reinas para un tablero NxN.
    Se asegura de que las reinas iniciales no se ataquen entre si
    """
    reinas_colocadas = []
    
    # creamos una lista de filas disponibles para no poner dos reinas en la misma fila
    filas_disponibles = list(range(n))
    
    # intentamos colocar la cantidad de reinas solicitadas
    for _ in range(num_reinas_iniciales):
        intentos = 0
        # le damos un máximo de intentos para evitar que el programa se quede atrapado
        while intentos < 100:
            if not filas_disponibles:
                break # Ya no hay filas libres
            
            # elegimos una fila al azar de las disponibles y una columna al azar
            r = random.choice(filas_disponibles)
            c = random.randint(0, n - 1)
            
            # verificamos si esta posición choca con las reinas que ya pusimos
            conflicto = False
            for (reina_r, reina_c) in reinas_colocadas:
                # comparamos columna y diagonales (no verificamos fila porque ya son únicas)
                if reina_c == c or abs(reina_r - r) == abs(reina_c - c):
                    conflicto = True
                    break
            
            # si no hay conflicto, la agregamos a nuestra lista oficial
            if not conflicto:
                reinas_colocadas.append((r, c))
                filas_disponibles.remove(r) # quitamos la fila para no re-usarla
                break # rompemos el ciclo while y pasamos a la siguiente reina
            
            intentos += 1

    return reinas_colocadas

def restriccion_perm_aleatoria(n,tablero):
    base = [-1]*n
    for (r,c) in tablero:
        base[r]=c
    return base