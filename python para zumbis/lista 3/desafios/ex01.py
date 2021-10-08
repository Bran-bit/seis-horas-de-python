'''
Dizemos que um número natural é triangular
se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. 
Dado um inteiro não-negativo n,
verificar se n é triangular
'''
# repetir a condição dada de multiplicação até achar o número
# ou o produto ficar maior que ele
num = int(input('Digite um número: '))
i = 1
while i * (i + 1) * (i + 2) < num:
    i += 1
condicao = i * (i + 1) * (i + 2)
if condicao == num:
    print(f'{num} é um número triangular, pois {i} * {i+1} * {i+2} = {num}')
else:
   print(f'{num} não é um número triangular. O triangular mais próximo dele é: {i} * {i+1} * {i+2} = {i * (i+1) * (i+2)}') 
