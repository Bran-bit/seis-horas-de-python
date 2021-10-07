'''
Escreva um programa que leia a quantidade de dias,
horas, minutos e segundos do usuário. Calcule
o total em segundos.
'''
dias = int(input('Quantidade de dias: '))
horas = int(input('Quantidade de horas: '))
minutos = int(input('Quantidade de minutos: '))
segundos = int(input('Quantidade de segundos: '))
dias *= 24 * 60 * 60 * 60
horas *= 60 * 60 * 60
minutos *= 60
segundos += dias + horas + minutos
print('Total em segundos: ' + str(segundos))
