import pytest

try:
    from src.bruteforce import resolver_fuerza_bruta
except ImportError:
    from src.bruteforce import resolver_fuerza_bruta

from src.backtracking import resolver_backtracking
from src.local_search import resolver_local_search
from src.genetic_algorithm import solve_completion_ga

from tests.validators import verificar_n_queens_completion 
from tests.generator import generar_tablero_aleatorio, restriccion_perm_aleatoria,perm_conjunto_entero


# ==========================================
# PRUEBAS PARA BACKTRACKING
# ==========================================

def test_backtracking_tablero_vacio():
    """Prueba que Backtracking resuelva un tablero vacío de 4x4"""
    n = 4
    reinas_iniciales = []
    solucion = resolver_backtracking(n, reinas_iniciales)
    
    assert solucion is not None, "Debería encontrar una solución para N=4 vacío"
    assert len(solucion) == n, f"Debería tener exactamente {n} reinas"
    assert verificar_n_queens_completion(n, reinas_iniciales, solucion) == True, "La solución debe ser matemáticamente válida"


def test_backtracking_con_reinas_iniciales():
    """Prueba Backtracking con un tablero 4x4 que ya tiene una reina puesta en (0, 1)"""
    n = 4
    reinas_iniciales = [(0, 1)]
    solucion = resolver_backtracking(n, reinas_iniciales)
    
    assert solucion is not None, "Debería encontrar solución con la reina inicial en (0, 1)"
    # asegurar que la reina inicial sigue en su posición original
    assert (0, 1) in solucion, "La solución final debe conservar la reina inicial"
    assert verificar_n_queens_completion(n, reinas_iniciales, solucion) == True


def test_backtracking_caso_imposible():
    """Prueba que Backtracking devuelva None ante una configuración inicial imposible"""
    n = 4
    # dos reinas iniciales atacándose mutuamente en la misma fila
    reinas_iniciales = [(0, 0), (0, 1)]
    solucion = resolver_backtracking(n, reinas_iniciales)
    
    assert solucion is None, "Debería retornar None porque el estado inicial ya es inválido"


# ==========================================
# PRUEBAS PARA FUERZA BRUTA
# ==========================================

def test_fuerza_bruta_tablero_vacio():
    """Prueba que Fuerza Bruta resuelva un tablero vacío pequeño (N=4)"""
    n = 4
    reinas_iniciales = []
    solucion = resolver_fuerza_bruta(n, reinas_iniciales)
    
    assert solucion is not None
    assert len(solucion) == n
    assert verificar_n_queens_completion(n, reinas_iniciales, solucion) == True


def test_fuerza_bruta_con_reinas_iniciales():
    """Prueba Fuerza Bruta con una reina inicial"""
    n = 4
    reinas_iniciales = [(0, 2)]
    solucion = resolver_fuerza_bruta(n, reinas_iniciales)
    
    assert solucion is not None
    assert (0, 2) in solucion
    assert verificar_n_queens_completion(n, reinas_iniciales, solucion) == True


def test_fuerza_bruta_caso_imposible():
    """Prueba que Fuerza Bruta devuelva None si es imposible resolverlo"""
    n = 3  # el problema de las 3 reinas es matemáticamente imposible de resolver
    reinas_iniciales = []
    solucion = resolver_fuerza_bruta(n, reinas_iniciales)
    
    assert solucion is None, "Para N=3 no existe solución, debe retornar None"


# =====================================================================
# PRUEBAS ALEATORIAS
# =====================================================================

@pytest.mark.parametrize("ejecucion", range(10))  # Repite la prueba 10 veces con tableros diferentes
def test_algoritmos_con_tableros_aleatorios(ejecucion):
    """
    Genera tableros aleatorios sorpresa de tamaños entre 4 y 6,
    los resuelve y verifica matemáticamente que las soluciones sean válidas.
    """
    import random
    
    # elegimos un tamaño de tablero al azar (mantenemos tamaños pequeños para no ralentizar Pytest)
    n = random.randint(4, 6)
    reinas_iniciales_por_tablero = 1
    
    # 1 generamos el tablero sorpresa
    tablero_inicial = generar_tablero_aleatorio(n, reinas_iniciales_por_tablero)
    restriccion_perm = restriccion_perm_aleatoria(n, tablero_inicial)
    
    # 2 probamos y validamos backtracking
    solucion_bt = resolver_backtracking(n, tablero_inicial)
    if solucion_bt is not None:
        # Si encontró solución, verificamos que no se ataquen y que respete las iniciales
        exito_bt = verificar_n_queens_completion(n, tablero_inicial, solucion_bt)
        assert exito_bt == True, f"¡Fallo! Backtracking dio una solución inválida para N={n} con iniciales {tablero_inicial}"
        
    # 3 probamos y validamos Fuerza Bruta
    solucion_fb = resolver_fuerza_bruta(n, tablero_inicial)
    if solucion_fb is not None:
        exito_fb = verificar_n_queens_completion(n, tablero_inicial, solucion_fb)
        assert exito_fb == True, f"¡Fallo! Fuerza Bruta dio una solución inválida para N={n} con iniciales {tablero_inicial}"

    # 4 probamos y validamos Local Search
    solucion_ls = resolver_local_search(n, tablero_inicial)
    if solucion_ls is not None:
        exito_ls = verificar_n_queens_completion(n, tablero_inicial, solucion_ls)
        assert exito_ls == True, f"¡Fallo! Local Search dio una solución inválida para N={n} con iniciales {tablero_inicial}"
    
    # 5 probamos y validamos Algoritmo Genético
    solucion_ga = solve_completion_ga(n, restriccion_perm)
    if solucion_ga is not None:
        exito_ga = verificar_n_queens_completion(n, tablero_inicial, perm_conjunto_entero(solucion_ga))
        assert exito_ga == True, f"¡Fallo! Algoritmo Genético dio una solución inválida para N={n} con iniciales {tablero_inicial}"