import time
import json
import os

from src.local_search import resolver_local_search

try:
    from src.bruteforce import resolver_fuerza_bruta
except ImportError:
    from src.bruteforce import resolver_fuerza_bruta

from src.backtracking import resolver_backtracking
from src.local_search import resolver_local_search
from src.genetic_algorithm import solve_completion_ga
from tests.generator import generar_tablero_aleatorio, restriccion_perm_aleatoria

def ejecutar_pruebas_rendimiento():
    """
    Ejecuta pruebas en tableros de distintos tamaños, mide el tiempo 
    y guarda los resultados en un archivo JSON.
    """
    # tamaños de tablero a probar (dejamos hasta 8 porque Fuerza Bruta colapsa rápido)
    tamanos = [4, 5, 6, 7, 8]
    reinas_iniciales_por_tablero = 1
    
    datos_grafica = {
        "tamanos_n": tamanos,
        "tiempos_brute_force": [],
        "tiempos_backtracking": [],
        "tiempos_local_search": [],
        "tiempos_genetic_algorithm": []
    }

    print("Iniciando pruebas de rendimiento...")
    print("-" * 40)

    for n in tamanos:
        print(f"Evaluando tablero de {n}x{n}...")
        
        # 1 generamos el tablero sorpresa
        tablero_inicial = generar_tablero_aleatorio(n, reinas_iniciales_por_tablero)
        restriccion_perm = restriccion_perm_aleatoria(n,tablero_inicial)
        
        #  medimos el tiempo de fuerza bruta
        inicio_fb = time.perf_counter()
        resolver_fuerza_bruta(n, tablero_inicial)
        fin_fb = time.perf_counter()
        tiempo_fb = (fin_fb - inicio_fb) * 1000  
        
        #  medimos el tiempo de backtracking
        inicio_bt = time.perf_counter()
        resolver_backtracking(n, tablero_inicial)
        fin_bt = time.perf_counter()
        tiempo_bt = (fin_bt - inicio_bt) * 1000  

        #  medimos el tiempo de local_search
        inicio_ls = time.perf_counter()
        resolver_local_search(n, tablero_inicial)
        fin_ls = time.perf_counter()
        tiempo_ls = (fin_ls - inicio_ls) * 1000  

        #  medimos el tiempo de genetic_algorithm
        inicio_ga = time.perf_counter()
        solve_completion_ga(n, restriccion_perm)
        fin_ga = time.perf_counter()
        tiempo_ga = (fin_ga - inicio_ga) * 1000  

        # 4 guardamos los resultados
        datos_grafica["tiempos_brute_force"].append(tiempo_fb)
        datos_grafica["tiempos_backtracking"].append(tiempo_bt)
        datos_grafica["tiempos_local_search"].append(tiempo_ls)
        datos_grafica["tiempos_genetic_algorithm"].append(tiempo_ga)
        
        print(f"  - Fuerza Bruta: {tiempo_fb:.4f} ms")
        print(f"  - Backtracking: {tiempo_bt:.4f} ms")
        print(f"  - Local Search: {tiempo_fb:.4f} ms")
        print(f"  - Algoritmo Genético: {tiempo_bt:.4f} ms")


    # 5 exportamos a un archivo JSON
    ruta_json = os.path.join(os.path.dirname(__file__), 'resultados_rendimiento.json')
    with open(ruta_json, 'w') as archivo:
        json.dump(datos_grafica, archivo, indent=4)
        
    print("-" * 40)
    print(f"¡Resultados guardados exitosamente en:\n{ruta_json}")

if __name__ == "__main__":
    ejecutar_pruebas_rendimiento()