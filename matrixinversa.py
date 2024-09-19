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
            var = int(input(f'Digite o valor da posição {i+1}x{j+1}: '))
            if var == '':
                print('Digite um valor válido')
                return matrix()
            else:
                linha.append(var)
        matrix.append(linha)

    print("\nMatriz original:")
    for linha in matrix:
        print(linha)

    np_matrix = np.array(matrix)

    det = np.linalg.det(np_matrix)

    if det == 0:
        print("\nA matriz não é inversível (determinante igual a zero).")
    else:
        # Calculando a inversa
        inversa = np.linalg.inv(np_matrix)

        print("\nMatriz inversa:")
        print(inversa)

    print('Pressione Enter para não digitar um valor e usar uma variável simbólica')
    x = input('Digite o valor de RE: ')
    if x == '':
        x = sp.symbols('x') # X = RE
    else:
        x = int(x)

    y = input('Digite o valor de P1: ')
    if y == '':
        y = sp.symbols('y') # Y = P1
    else:
        y = int(y)

    w = input('Digite o valor de P2: ')
    if w == '':
        w = sp.symbols('w') # W = P2
    else:
        w = int(w)

    z = input('Digite o valor de RD: ')
    if z == '':
        z = sp.symbols('z') # Z = RD
    else:
        z = int(z)

    e = input('Digite o valor de E: ')
    if e == '':  
        e = sp.symbols('E') 
    else:
        e = int(e)

    a = input('Digite o valor de A: ')
    if a == '':
        a = sp.symbols('A')
    else:
        a = int(a)

    l = input('Digite o valor de L: ')
    if l == '':
        l = sp.symbols('L')
    else:
        l = int(l)

    vector = [x*((e*a)/l),y*((e*a)/l),w*((e*a)/l),z*((e*a)/l)]

    solution = []
    for i in range(len(inversa)):
        soma = 0
        a = []
        for j in range(len(inversa)):
            soma += inversa[i][j]*vector[j]
        a.append(soma)
        solution.append(a)
    print(solution)
    print(solution[0][0],solution[1][0],solution[2][0],solution[3][0])