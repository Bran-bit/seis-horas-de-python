#Calcular média dez números
#Somar dez inteiros lidos
soma = 0
i = 1
while i <= 10:
    x = int(input(f'{i}º número: '))
    soma += x
    i += 1
print(f'Média dos {i - 1} números: {soma / 10:.1f}')