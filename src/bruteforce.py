import itertools
from tests.validators import verificar_n_queens_completion 

def resolver_fuerza_bruta(n, reinas_iniciales):
    """
    encuentra una solución para N-Queens Completion probando todas las combinaciones
    retorna la lista de posiciones si hay solución, o "none" si es imposible.
    """
    reinas_faltantes = n - len(reinas_iniciales)
    
    # si ya están todas las reinas, verificamos si el estado inicial ya es valido
    if reinas_faltantes == 0:
        if verificar_n_queens_completion(n, reinas_iniciales, reinas_iniciales):
            return reinas_iniciales
        return None
        
    # 1 obtener todas las casillas posibles del tablero n x n
    todas_las_casillas = set((r, c) for r in range(n) for c in range(n))
    
    # 2 dejar solo las casillas que están vacías
    casillas_vacias = todas_las_casillas - set(reinas_iniciales)
    
    # 3 probar TODAS las combinaciones posibles en los espacios vacios
    for combinacion in itertools.combinations(casillas_vacias, reinas_faltantes):
        
        # unimos las iniciales con la combinación que estamos probando
        propuesta_tablero = list(reinas_iniciales) + list(combinacion)
        
        # 4 verificamos
        if verificar_n_queens_completion(n, reinas_iniciales, propuesta_tablero):
            return propuesta_tablero # ¡Encontramos la solución!
            
    # si revisa miles de combinaciones y el ciclo termina sin retornar nada:
    return None