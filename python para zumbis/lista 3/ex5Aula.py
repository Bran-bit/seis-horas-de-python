#Calcular fatorial de um número lido
i = 1
fat = 1
num = int(input('Digite um número: '))
while i <= num:
    fat *= i
    i += 1
print(f'fat({num}) = {fat}')