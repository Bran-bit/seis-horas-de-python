'''
Faça um Programa que leia três números e mostre o maior deles
'''
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n3:
    maior = n2
else:
    maior = n3
print(f'Maior: {maior}')
