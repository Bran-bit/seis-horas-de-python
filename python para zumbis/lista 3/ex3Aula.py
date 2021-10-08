#Somar dez inteiros lidos
soma = 0
i = 1
while i <= 10:
    x = int(input(f'{i}º número: '))
    soma += x
    i += 1
print(f'Soma dos {i - 1} números: {soma}')