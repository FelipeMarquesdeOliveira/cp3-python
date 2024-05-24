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

while True:
    print('[1] Verificar se número é perfeito')
    print('[2] Verificar se a lista é um palíndromo')
    print('[3] Preencher Matriz')
    print('[4] Exibir Matriz')
    print('[5] Somar elementos acima da diagonal principal')
    print('[6] Finalizar')

    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        n = int(input('Número: '))
        numero_perfeito(n)
    elif opcao == 2:
        lista = input('Digite a lista separada por espaços: ').split()
        palindromo(lista)
    elif opcao == 3:
        linhas = int(input('Linhas: '))
        colunas = int(input('Colunas: '))
        matriz = preencher_matriz(linhas, colunas)
    elif opcao == 4:
        if 'matriz' not in locals():
            print('A matriz ainda não foi preenchida.')
        else:
            exibir_matriz(matriz)
    elif opcao == 5:
        if 'matriz' not in locals():
            print('A matriz ainda não foi preenchida.')
        else:
            soma = soma_itens(matriz)
            print('A soma dos elementos acima da diagonal principal é:', soma)
    elif opcao == 6:
        break
    else:
        print('Opção Inválida')
