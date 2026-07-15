'''
PSEUDOCÓDIGO

LOCAL SEARCH CON N-QUEENS BASE MODIFICADO

IDEA 1: DESCARTAR SOLUCIONES QUE ALTEREN LA POSICIÓN DE LAS REINAS INICIALES

IDEA 2: ALGORIMO QUE GENERE REINAS EN LAS FILAS RESTANTES Y REUBIQUE COLUMNAS SI HAY CONFLICTOS

IDEA 3: ALGORITMO QUE REUBIQUE ÚNICAMENTE LAS REINAS NO INICIALES
'''
'''
PSEUDOCÓDIGO

LOCAL SEARCH CON N-QUEENS BASE MODIFICADO

IDEA 1: DESCARTAR SOLUCIONES QUE ALTEREN LA POSICIÓN DE LAS REINAS INICIALES

IDEA 2: ALGORIMO QUE GENERE REINAS EN LAS FILAS RESTANTES Y REUBIQUE COLUMNAS SI HAY CONFLICTOS

IDEA 3: ALGORITMO QUE REUBIQUE ÚNICAMENTE LAS REINAS NO INICIALES
'''
from numpy import random

def conflictos(reinas):
    for (r1, c1) in reinas:
        for (r2, c2) in reinas:
            if (r1, c1) != (r2, c2):
                if r1 == r2 or c1 == c2 or r1-c1 == r2-c2 or r1+c1 == r2+c2:
                    return True
    return False

def reina_max_conflictos(reinas, reinas_iniciales):
    reina_max = None
    n_max_conflictos = -1

    for (r1, c1) in reinas:
        if not (r1, c1) in reinas_iniciales:
            n_conflictos = 0
            for (r2, c2) in reinas:
                if (r1, c1) != (r2, c2):
                    if r1 == r2 or c1 == c2 or r1-c1 == r2-c2 or r1+c1 == r2+c2:
                        n_conflictos += 1

            if n_conflictos > n_max_conflictos:
                reina_max = (r1, c1)
                n_max_conflictos = n_conflictos
    return reina_max

def resolver_local_search(n, reinas_iniciales, max_iter=1000):
    if conflictos(reinas_iniciales):
        return None

    reinas_colocadas = set(reinas_iniciales)
    filas_ocupadas = {r for (r, c) in reinas_iniciales}
    
    for i in range(n):
        if i not in filas_ocupadas:
            col_aleatoria = random.randint(0, n-1)
            reinas_colocadas.add((i, col_aleatoria))
    
    iteraciones = 0
    while conflictos(reinas_colocadas) and iteraciones < max_iter:
        reina_conflictiva = reina_max_conflictos(reinas_colocadas, reinas_iniciales)
        if reina_conflictiva is None:
            break
            
        col_aleatoria = random.randint(0, n-1)
        reinas_colocadas.remove(reina_conflictiva)
        reinas_colocadas.add((reina_conflictiva[0], col_aleatoria))
        iteraciones += 1

    # Si salió del while pero aún hay conflictos, significa que se rindió por max_iter
    if conflictos(reinas_colocadas):
        return None
        
    return list(reinas_colocadas)
