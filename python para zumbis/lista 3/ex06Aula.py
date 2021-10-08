# Somar números até o usuário digitar zero.
soma = 0
contador = 0
while True:
    x = int(input('Digite um número: '))
    if x == 0:
        break
    soma += x
    contador += 1
print(f'Soma: {soma}')
print(f'Média: {soma / contador:.1f}')