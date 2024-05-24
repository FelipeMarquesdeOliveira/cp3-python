import random

def numero_perfeito(numero):
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
    if soma == numero:
        print(f'{numero} é um número perfeito')
    else:
        print(f'{numero} não é um número perfeito')

def palindromo(lista):
    if lista == lista[::-1]:
        print(f'A lista {lista} é um palíndromo')
    else:
        print(f'A lista {lista} não é um palíndromo')

def preencher_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            n = random.randint(1, 50)
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

def soma_itens(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:
                soma += matriz[i][j]
    return soma