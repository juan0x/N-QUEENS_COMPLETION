try:
    from src.bruteforce import resolver_fuerza_bruta
except ImportError:
    from src.bruteforce import resolver_fuerza_bruta

from src.backtracking import resolver_backtracking
from tests.validators import verificar_n_queens_completion 


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


# ==========================================
# COMPARACIÓN ENTRE AMBOS ALGORITMOS
# ==========================================

def test_comparar_solucionadores():
    """Compara que ambos algoritmos coincidan en la factibilidad de un problema"""
    n = 5
    reinas_iniciales = [(0, 0), (1, 2)]
    
    solucion_bt = resolver_backtracking(n, reinas_iniciales)
    solucion_fb = resolver_fuerza_bruta(n, reinas_iniciales)
    
    if solucion_bt is None:
        assert solucion_fb is None, "Si Backtracking no halla solución, Fuerza Bruta tampoco debería"
    else:
        assert solucion_fb is not None, "Si Backtracking halla solución, Fuerza Bruta también debería"
        # ambos deben ser válidos aunque las soluciones individuales difieran
        assert verificar_n_queens_completion(n, reinas_iniciales, solucion_bt) == True
        assert verificar_n_queens_completion(n, reinas_iniciales, solucion_fb) == True