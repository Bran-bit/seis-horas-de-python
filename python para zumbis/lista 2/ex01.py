'''
Faça um Programa que peça os três lados de um triângulo. 
O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, 
se o mesmo é: equilátero, isósceles ou escaleno
'''
#Equilátero = três lados iguais
#Isóceles = dois lados iguais
#Escaleno = não possui lados iguais
print('Triangulo')
a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a > b + c or b > a + c or c > a + b:
    print('Não é um triângulo.')
elif a == b == c:
    print('Triângulo Equilátero')
elif a == b or b == c or a == c:
    print('Triângulo Isóceles')
else:  
    print('Triângulo Escaleno')