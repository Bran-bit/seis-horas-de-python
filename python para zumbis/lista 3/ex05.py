'''
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.
'''
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
while a % b != 0:
    a, b = b, a%b
print(f'mdc: {b}')