import random
from copy import deepcopy

def swap_rows(matrix, row_index_1, row_index_2):
    if row_index_1 < 0 or row_index_2 >= len(matrix):
        return 'Índice inválido'
    
    result = deepcopy(matrix)
    result[row_index_1], result[row_index_2] = result[row_index_2], result[row_index_1]
    return result

def times(matrix, row_index, constant):
    if row_index < 0 or row_index >= len(matrix):
        return 'Indices invalidos'
    
    result = deepcopy(matrix)
    for i, row in enumerate(matrix):
        if i == row_index:
            result[i] = [element * constant for element in row]

    return result

def sum_rows(matrix, target_row_index, source_row_index, constant):
    if target_row_index < 0 or target_row_index >= len(matrix) or source_row_index < 0 or source_row_index >= len(matrix):
        return 'Índice inválido'
    
    result = deepcopy(matrix)
    source_row = [element * constant for element in result[source_row_index]]
    result[target_row_index] = [sum(pair) for pair in zip(result[target_row_index], source_row)]
    
    return result

def generate_random_matrix(rows, cols):
    if (rows < 0 or cols < 0) or (rows == 1 or cols == 1):
        return 'Valores invalidos'
    
    matrix = []
    for i in range(rows):
        row = [random.randint(0, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def replace_current_matrix(matrix, result):
    while True:
        replace = input('\nDeseja substituir a matriz original pela matriz resultante? (S/N): ')
        if replace.lower() == 's':
            return result
        elif replace.lower() == 'n':
            return matrix
        print('Opção inválida. Tente novamente.')
