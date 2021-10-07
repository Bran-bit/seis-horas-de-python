'''
Escreva um programa que pergunte a quantidade de km
percorridos por um carro alugado pelo usuário, assim como a quantidade 
de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
'''
kmPercorridos = float(input('Digite a quantidade de km percorridos: '))
quantidadeDias = int(input('Digite a quantidade de dias do aluguel do carro: '))
preco = float(quantidadeDias * 60) + kmPercorridos * 0,15
print(f'Preço a pagar: {preco:.2f}')