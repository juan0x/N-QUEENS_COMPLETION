def verificar_n_queens_completion(n, q_inicial, q_final):
  """
  Verifica en tiempo O(n) si el certificado (q_final) es una solución válida
  para el problema N-Queens Completion.
  """
  # 1. Verificar la cardinalidad
  if len(q_final) != n:
    return False

  # 2. Verificar que las reinas preubicadas sigan ahí
  q_final_set = set(q_final)
  for q in q_inicial:
    if q not in q_final_set:
      return False

  # 3. Verificar que no haya ataques utilizando Hash Sets
  filas, columnas, diag_principal, diag_secundaria = set(), set(), set(), set()

  for r, c in q_final:
    # Validar límites del tablero
    if not (0 <= r < n and 0 <= c < n):
      return False

    # Comprobar choques en la libreta de registros
    if (r in filas or c in columnas or
      (r - c) in diag_principal or (r + c) in diag_secundaria):
      return False

    # Registrar la reina actual
    filas.add(r)
    columnas.add(c)
    diag_principal.add(r - c)
    diag_secundaria.add(r + c)

  return True