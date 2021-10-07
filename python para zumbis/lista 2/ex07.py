'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.
Obs. : somente são vendidos um número inteiro de latas.
'''
# 1 lata pinta 54 m²
tamanhoArea = int(input('Tamanho da área (m²): '))
if tamanhoArea % (18 * 3) == 0:
    latas = tamanhoArea / (18 * 3)
else:
    latas = int(tamanhoArea / (18 * 3)) + 1
preco = latas * 80
print(f'Para {tamanhoArea} m², serão necessárias {latas} latas, totalizando R$ {preco}')
