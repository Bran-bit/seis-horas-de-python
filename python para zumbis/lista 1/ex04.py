'''
aça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a
porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
'''
salario = float(input('Valor do salário: '))
porcentagem = float(input('Porcentagem do aumento: '))
aumento = salario * (porcentagem / 100)
print(f'Valor do aumento: R$ {aumento:.2f}')
print(f'Valor do salário atualizado: R$ {(salario + aumento):.2f}')