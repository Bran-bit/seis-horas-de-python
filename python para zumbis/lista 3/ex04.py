'''
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o
seu número de Fibonacci. F1= 1, 
                         F2 = 1, 
                         F3 = 2, etc.
''' 
num = int(input('Digite um número: '))
a, b = 1, 1
i = 1
# a e b são os dois primeiros da sequência, por isso se subtrai 2
while i <= num - 2:
# a fica com o valor antecessor
    a, b = b, a + b
    i += 1
print(b)