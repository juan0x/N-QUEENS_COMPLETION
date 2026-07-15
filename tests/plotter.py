import json
import os
import matplotlib.pyplot as plt

def generar_grafica():
    """
    Lee los datos del JSON de rendimiento y genera una gráfica comparativa.
    """
    ruta_json = os.path.join(os.path.dirname(__file__), 'resultados_rendimiento.json')
    
    if not os.path.exists(ruta_json):
        print("Error: No se encontró el archivo de resultados. Corre primero el benchmark.")
        return
        
    with open(ruta_json, 'r') as archivo:
        datos = json.load(archivo)
        
    tamanos = datos["tamanos_n"]
    tiempos_fb = datos["tiempos_brute_force"]
    tiempos_bt = datos["tiempos_backtracking"]
    tiempos_ls = datos["tiempos_local_search"]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(tamanos, tiempos_fb, label="Fuerza Bruta (Brute Force)", marker='o', color='#e74c3c', linewidth=2)
    plt.plot(tamanos, tiempos_bt, label="Backtracking", marker='s', color='#3498db', linewidth=2)
    plt.plot(tamanos, tiempos_ls, marker='^', label='Búsqueda Local', color='green')
    
    plt.title("Análisis de Rendimiento: FB VS BT VS LS VS G", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Tamaño del Tablero (N)", fontsize=12)
    plt.ylabel("Tiempo de Ejecución (milisegundos)", fontsize=12)
    
    plt.yscale("log") 
    

    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend(fontsize=11, loc="upper left")
    

    ruta_grafica = os.path.join(os.path.dirname(__file__), 'comparacion_rendimiento.png')
    plt.savefig(ruta_grafica, dpi=300, bbox_inches='tight')
    plt.close()
    
    print("-" * 50)
    print("¡Gráfica generada con éxito!")
    print(f"La puedes encontrar en:\n{ruta_grafica}")
    print("-" * 50)

if __name__ == "__main__":
    generar_grafica()