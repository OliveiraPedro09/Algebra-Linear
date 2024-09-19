import sympy as sp
import numpy as np

def matrix_inversa():
    col = 4
    row = 4
    matrix = []

    print('Digite os valores da matriz linha por linha')

    for i in range(row):
        linha = []
        for j in range(col):
            try:
                var = int(input(f'Digite o valor da posição {i+1}x{j+1}: '))
                linha.append(var)
            except ValueError:
                print('Valor inválido! Digite um número inteiro.')
                return
        matrix.append(linha)

    print("\nMatriz original:")
    for linha in matrix:
        print(linha)

    np_matrix = np.array(matrix)

    det = np.linalg.det(np_matrix)

    if det == 0:
        print("\nA matriz não é inversível (determinante igual a zero).")
        return
    else:
        # Calculando a inversa
        inversa = np.linalg.inv(np_matrix)

        print("\nMatriz inversa:")
        print(inversa)

    print('Pressione Enter para usar uma variável simbólica')
    
    # Função auxiliar para verificar entrada
    def get_input(prompt, symbol):
        valor = input(f'Digite o valor de {prompt}: ')
        if valor == '':
            return sp.symbols(symbol)
        return int(valor)

    x = get_input('RE', 'x')
    y = get_input('P1', 'y')
    w = get_input('P2', 'w')
    z = get_input('RD', 'z')
    e = get_input('E', 'E')
    a = get_input('A', 'A')
    l = get_input('L', 'L')

    vector = [x * ((e * a) / l), y * ((e * a) / l), w * ((e * a) / l), z * ((e * a) / l)]

    solution = []
    for i in range(len(inversa)):
        soma = 0
        for j in range(len(inversa)):
            soma += inversa[i][j] * vector[j]
        solution.append(soma)

    # Forçando o U1 e U4 a serem 0
    solution[0] = 0
    solution[-1] = 0

    print("\nSolução final:")
    for sol in solution:
        print(sol)

matrix_inversa()
