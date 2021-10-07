'''
Escreva um programa para
calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. 
Exiba o total de dias.
'''
cigarrosPorDia = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))
numCigarros = cigarrosPorDia * anos * 365
diasPerdidos = numCigarros * 10 / (60 * 24)
print(f'No total, você perdeu {diasPerdidos} dias de vida ao fumar {numCigarros} cigarros.')