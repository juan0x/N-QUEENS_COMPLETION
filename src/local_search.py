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

# Función para ver si hay amenazas entre reinas
def conflictos(reinas):
  for (r1,c1) in reinas:
    for (r2,c2) in reinas:
      if (r1,c1) != (r2,c2):
        if r1 == r2 or c1 == c2 or r1-c1 == r2-c2 or r1+c1 == r2+c2:
          return True
  return False

# Función para ver la reina con más amenazas
def reina_max_conflictos(reinas, reinas_iniciales):
  reina_max_conflictos = None
  n_max_conflictos = -1

  for (r1,c1) in reinas:
      if not (r1,c1) in reinas_iniciales:
        n_conflictos = 0
        for (r2,c2) in reinas:
            if (r1,c1) != (r2,c2):
              if r1 == r2 or c1 == c2 or r1-c1 == r2-c2 or r1+c1 == r2+c2:
                n_conflictos+=1

        if n_conflictos > n_max_conflictos:
            reina_max_conflictos = (r1,c1)
            n_max_conflictos = n_conflictos
  return reina_max_conflictos

# FUNCIÓN PRINCIPAL
def resolver_local_search(n, reinas_iniciales):

    #Verificar si una configuración es solucionable
    if conflictos(reinas_iniciales):
        return False

    #Crear el primer tablero aleatorio
    reinas_colocadas = set(reinas_iniciales)
    filas_ocupadas = {r for (r,c) in reinas_iniciales}
    for i in range(n):
        if i in filas_ocupadas:
            pass
        else:
            col_aleatoria = random.randint(n)
            reinas_colocadas.add((i,col_aleatoria))
    
    #Mover la reina con más amenazas hasta encontrar la solución
    while conflictos(reinas_colocadas):
        reina_conflictiva = reina_max_conflictos(reinas_colocadas,reinas_iniciales)
        if reina_conflictiva is None:
            break
        col_aleatoria = random.randint(n)
        reinas_colocadas.remove(reina_conflictiva)
        reinas_colocadas.add((reina_conflictiva[0],col_aleatoria))

    return list(reinas_colocadas)

print(resolver_local_search(4,[]))
