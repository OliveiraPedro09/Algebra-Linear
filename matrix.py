# Pedro Martins de Oliveira, 2024, Lista de Programação 1 - Algebra Linear, Prof. Hudson Bode
import sympy as sp

def matrix():
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

    print(matrix)

    print('Pressione Enter para não digitar um valor e usar uma variável simbólica')
    x = input('Digite o valor de U2: ')
    if x == '':
        x = sp.symbols('x') # X = U2
    else:
        x = int(x)

    y = input('Digite o valor de U3: ')
    if y == '':
        y = sp.symbols('y') # Y = U3
    else:
        y = int(y)

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

    vector = [0 ,x * ((e * a) / l), y * ((e * a) / l), 0]

    solution = []
    for i in range(len(matrix)):
        soma = 0
        a = []
        for j in range(len(matrix)):
            soma += matrix[i][j]*vector[j]
        a.append(soma)
        solution.append(a)
    print(solution)
    print("O valor de RE é :",solution[0][0],"O Valor de RD é: ",solution[3][0])

matrix()
