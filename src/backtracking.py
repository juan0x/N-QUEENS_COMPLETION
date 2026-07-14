def resolver_backtracking(n, reinas_iniciales):
    """
    Encuentra una solución para N-Queens Completion usando Backtracking.
    Avanza fila por fila. Si una fila ya tiene reina, la salta.
    """
    
    # convertimos las reinas iniciales a un set para busquedas rápidas
    reinas_colocadas = set(reinas_iniciales)
    
    # averiguamos las filas ya están ocupadas por las reinas iniciales
    filas_ocupadas = {r for r, c in reinas_iniciales}
    
    def es_seguro(fila, col):
        """Verifica si podemos poner una reina en (fila, col) sin ser atacada"""
        for r, c in reinas_colocadas:
            # misma columna o misma diagonal (no revisamos fila porque el algoritmo avanza por filas)
            if c == col or abs(r - fila) == abs(c - col):
                return False
        return True

    def backtrack(fila_actual):
        # CASO BASE: si logramos pasar la última fila gg
        if fila_actual == n:
            return True
            
        # si la fila actual ya tiene una reina inicial, saltamos a la siguiente
        if fila_actual in filas_ocupadas:
            return backtrack(fila_actual + 1)
            
        # si la fila está vacia, intentamos poner una reina en cada columna
        for col in range(n):
            if es_seguro(fila_actual, col):
                # 1. HACER: colocamos la reina
                reinas_colocadas.add((fila_actual, col))
                
                # 2. EXPLORAR: avanzamos a la siguiente fila
                if backtrack(fila_actual + 1):
                    return True # si el camino funciona, pasamos el éxito hacia arriba
                    
                # 3. DESHACER (Backtrack): si el camino falla, quitamos la reina e intentamos otra columna
                reinas_colocadas.remove((fila_actual, col))
                
        # si probamos todas las columnas de esta fila y ninguna sirvió, este camino no tiene salida
        return False

    # iniciamos la exploración desde la fila 0
    if backtrack(0):
        return list(reinas_colocadas)
    else:
        return None