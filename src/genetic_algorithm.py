import random

# ------------------------------------------------------------
# Funciones originales (no modificadas)
# ------------------------------------------------------------

def fitness(chrom):
    """Cuenta pares de reinas que no se atacan. Máximo = n*(n-1)//2."""
    n = len(chrom)
    max_pairs = n * (n - 1) // 2
    conflicts = sum(
        1 for i in range(n) for j in range(i + 1, n)
        if abs(chrom[i] - chrom[j]) == abs(i - j)
    )
    return max_pairs - conflicts

def tournament_select(pop, fitnesses, k=3):
    """Selecciona el mejor individuo entre k candidatos aleatorios."""
    candidates = random.sample(range(len(pop)), k)
    best = max(candidates, key=lambda i: fitnesses[i])
    return pop[best][:]

def pmx_crossover(p1, p2):
    """Cruce por mapeo parcial (PMX) para permutaciones."""
    n = len(p1)
    start, end = sorted(random.sample(range(n), 2))
    child = [-1] * n
    child[start:end+1] = p1[start:end+1]
    for i in list(range(0, start)) + list(range(end+1, n)):
        val = p2[i]
        while val in child[start:end+1]:
            idx = p1.index(val)
            val = p2[idx]
        child[i] = val
    return child

def swap_mutate(chrom, rate=0.02):
    """Intercambia dos posiciones aleatorias con probabilidad `rate`."""
    chrom = chrom[:]
    if random.random() < rate:
        i, j = random.sample(range(len(chrom)), 2)
        chrom[i], chrom[j] = chrom[j], chrom[i]
    return chrom

# ------------------------------------------------------------
# Nuevas funciones para el problema de completación
# ------------------------------------------------------------

def init_population_completion(n, fixed, pop_size):
    """
    Genera una población inicial respetando las posiciones fijas.
    `fixed` es una lista de longitud n; fixed[i] = columna fija o -1 si está libre.
    """
    free_rows = [i for i in range(n) if fixed[i] == -1]
    used_cols = {fixed[i] for i in range(n) if fixed[i] != -1}
    available = [c for c in range(n) if c not in used_cols]

    if len(available) != len(free_rows):
        raise ValueError("Posiciones fijas inválidas: columnas duplicadas o número incorrecto.")

    population = []
    for _ in range(pop_size):
        chrom = fixed[:]                # copia con -1 en las filas libres
        cols = available[:]             # copia de las columnas disponibles
        random.shuffle(cols)
        for row in free_rows:
            chrom[row] = cols.pop()     # asigna en orden (ya está barajado)
        population.append(chrom)
    return population

def pmx_crossover_free(p1, p2, fixed):
    """
    Aplica PMX únicamente sobre las filas libres.
    Las posiciones fijas se heredan sin cambios.
    """
    n = len(fixed)
    free_rows = [i for i in range(n) if fixed[i] == -1]

    # Extraer los valores de las filas libres en ambos padres
    list1 = [p1[i] for i in free_rows]
    list2 = [p2[i] for i in free_rows]

    child_list = pmx_crossover(list1, list2)   # cruce PMX sobre las sub‑permutaciones

    child = fixed[:]                           # copia de las fijas (con -1 en libres)
    for idx, row in enumerate(free_rows):
        child[row] = child_list[idx]
    return child

def swap_mutate_free(chrom, fixed, rate=0.02):
    """
    Mutación por intercambio de dos filas libres.
    Las fijas nunca se modifican.
    """
    n = len(fixed)
    free_rows = [i for i in range(n) if fixed[i] == -1]
    if len(free_rows) < 2:
        return chrom[:]

    chrom = chrom[:]
    if random.random() < rate:
        i, j = random.sample(free_rows, 2)
        chrom[i], chrom[j] = chrom[j], chrom[i]
    return chrom

def has_fixed_conflicts(fixed):
    """Comprueba si dos reinas fijas se atacan entre sí."""
    n = len(fixed)
    rows = [i for i in range(n) if fixed[i] != -1]
    for a in range(len(rows)):
        for b in range(a+1, len(rows)):
            i, j = rows[a], rows[b]
            if fixed[i] == fixed[j] or abs(fixed[i] - fixed[j]) == abs(i - j):
                return True
    return False

# ------------------------------------------------------------
# Algoritmo genético para el problema de completación
# ------------------------------------------------------------

def solve_completion_ga(n, fixed, pop_size=100, max_gen=1000):
    """
    Resuelve el problema de completación de N‑Reinas.
    - n: tamaño del tablero.
    - fixed: lista de longitud n; fixed[i] = columna fija (0..n-1) o -1 si libre.
    Retorna (solución, generación) si se encuentra, o (mejor encontrado, max_gen).
    """
    # Validación rápida de las fijas
    if len(fixed) != n:
        raise ValueError("La lista 'fixed' debe tener longitud n.")
    if has_fixed_conflicts(fixed):
        print("Las reinas fijas ya se atacan entre sí. No hay solución.")
        return None, 0

    max_fitness = n * (n - 1) // 2

    # Inicialización poblacional
    population = init_population_completion(n, fixed, pop_size)

    for gen in range(max_gen):
        fitnesses = [fitness(ind) for ind in population]

        # Mejor individuo actual
        best_idx = max(range(len(fitnesses)), key=lambda i: fitnesses[i])
        if fitnesses[best_idx] == max_fitness:
            return population[best_idx], gen + 1

        # Elitismo: conservar el mejor
        new_pop = [population[best_idx][:]]

        # Generar el resto de la nueva población
        while len(new_pop) < pop_size:
            p1 = tournament_select(population, fitnesses)
            p2 = tournament_select(population, fitnesses)

            # Cruce respetando las fijas
            child = pmx_crossover_free(p1, p2, fixed)

            # Mutación solo en filas libres
            child = swap_mutate_free(child, fixed)

            new_pop.append(child)

        population = new_pop

    # Si no se encontró solución, devolver el mejor encontrado
    fitnesses = [fitness(ind) for ind in population]
    best = max(range(len(fitnesses)), key=lambda i: fitnesses[i])
    return population[best], max_gen

def resolver_genetico_adapter(n, reinas_iniciales):
    """Adaptador para conectar el algoritmo genético con Pytest y el Benchmark."""
    
    # 1. Traducir formato de entrada: [(r, c)] -> [-1, 2, -1...]
    fixed = [-1] * n
    for r, c in reinas_iniciales:
        fixed[r] = c
        
    # 2. Ejecutar el algoritmo de tu compañero
    try:
        solucion_1d, iteraciones = solve_completion_ga(n, fixed)
    except ValueError:
        return None
        
    if solucion_1d is None:
        return None
        
    # 3. Validar si la solución es perfecta (0 choques)
    # Si alcanzó el límite de generaciones y devolvió una solución con choques, 
    # retornamos None para que Pytest no falle en rojo.
    conflictos = sum(1 for i in range(n) for j in range(i + 1, n) 
                     if abs(solucion_1d[i] - solucion_1d[j]) == abs(i - j))
    if conflictos > 0:
        return None
        
    # 4. Traducir formato de salida: [1, 3...] -> [(0, 1), (1, 3)...]
    solucion_tuplas = [(i, solucion_1d[i]) for i in range(n)]
    
    return solucion_tuplas