# 👑 N-Queens Completion Problem

Este repositorio contiene la implementación, validación y comparación de rendimiento de cuatro enfoques algorítmicos distintos para resolver el **Problema de Completación de las N-Reinas** (N-Queens Completion).

A diferencia del problema clásico de las N-Reinas, en la variante de **completación** partimos de un tablero que ya cuenta con algunas reinas fijas en posiciones predefinidas. El objetivo es colocar las reinas restantes de forma que ninguna reina se ataque entre sí (es decir, que no compartan fila, columna ni diagonal).

---

## 🚀 Algoritmos Implementados

Para resolver y analizar este problema, implementamos cuatro estrategias de diseño algorítmico:

1. **Fuerza Bruta (Brute Force):** Explora todas las combinaciones posibles de forma exhaustiva para encontrar una solución válida. Útil como referencia básica para tableros muy pequeños.
2. **Backtracking:** Una estrategia de búsqueda sistemática con poda que retrocede inmediatamente cuando detecta que una configuración parcial viola las restricciones del tablero.
3. **Búsqueda Local (Local Search):** Un enfoque heurístico que parte de un estado inicial completo y realiza intercambios locales orientados a minimizar progresivamente el número de conflictos.
4. **Algoritmo Genético (Genetic Algorithm):** Una metaheurística inspirada en la evolución natural. Utiliza selección por torneo, cruce por mapeo parcial (PMX) adaptado a restricciones y mutaciones por intercambio sobre las filas libres para "evolucionar" tableros hasta hallar uno óptimo sin colisiones.

---

## 📁 Estructura del Proyecto

```text
n_queens_completion/
│
├── src/
│   ├── brute_force.py      # Algoritmo de fuerza bruta
│   ├── backtracking.py     # Algoritmo de backtracking con restricciones
│   ├── local_search.py     # Heurística de búsqueda local
│   ├── genetic.py          # Algoritmo genético y su adaptador de formatos
│   └── validators.py       # Validadores lógicos del estado del tablero
│
├── tests/
│   └── test_nqueenscompletion.py   # Suite de pruebas automatizadas (Pytest)
│
├── benchmark.py            # Script para medir tiempos de ejecución de cada algoritmo
├── plotter.py              # Generador de gráficas comparativas utilizando Matplotlib
├── resultados.json         # Archivo de persistencia de datos del benchmark
└── README.md               # Este archivo descriptivo
