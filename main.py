from utils import get_integer_input
from matrix import replace_current_matrix, swap_rows, times, sum_rows, generate_random_matrix, print_matrix

def main():
    generate_new_matrix = True
    
    while True:
        if generate_new_matrix:
            rows = get_integer_input('Digite o número de linhas da matriz: ')
            cols = get_integer_input('Digite o número de colunas da matriz: ')
            matrix = generate_random_matrix(rows, cols)

            if(isinstance(matrix, str)):
                print(matrix)
                continue
            generate_new_matrix = False

        print('\nMatriz:')
        print_matrix(matrix)

        choice = get_integer_input('\nEscolha uma operação:\n1 - Trocar linhas.\n2 - Multiplicar linha por uma constante.\n3 - Somar linha com outra multiplicada por uma constante.\n4 - Gerar nova matriz.\n5 - Sair.\nOpção: ')

        if choice == 1:
            row_index_1 = get_integer_input('Digite o índice da primeira linha a ser trocada: ')
            row_index_2 = get_integer_input('Digite o índice da segunda linha a ser trocada: ')
            result = swap_rows(matrix, row_index_1, row_index_2)
            if isinstance(result, str):
                print(result)
            else:
                print('\nMatriz com linhas trocadas:')
                print_matrix(result)
                matrix = replace_current_matrix(matrix, result)            

        elif choice == 2:
            row_index = get_integer_input('Digite o índice da linha a ser multiplicada: ')
            constant = get_integer_input('Digite a constante pela qual multiplicar a linha: ')
            result = times(matrix, row_index, constant)
            if isinstance(result, str):
                print(result)
            else:
                print('\nMatriz com a linha multiplicada:')
                print_matrix(result)
                matrix = replace_current_matrix(matrix, result)            
        
        elif choice == 3:
            target_row_index = get_integer_input('Digite o índice da linha de destino: ')
            source_row_index = get_integer_input('Digite o índice da linha a ser somada: ')
            constant = get_integer_input('Digite a constante pela qual multiplicará a linha a ser somada: ')
            result = sum_rows(matrix, target_row_index, source_row_index, constant)
            if isinstance(result, str):
                print(result)
            else:
                print('\nMatriz com a operação realizada:')
                print_matrix(result)
                matrix = replace_current_matrix(matrix, result)  

        elif choice == 4:
            generate_new_matrix = True
            
        elif choice == 5:
            break
            
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
