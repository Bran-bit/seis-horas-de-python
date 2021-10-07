'''
Faça um Programa que pergunte quanto você
ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se 
que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, 
quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
Observe que Salário Bruto - Descontos = Salário Líquido. 
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
'''
valorHora = float(input('Ganho por hora: '))
numHoras = int(input('Horas trabalhadas: '))
salarioBruto = valorHora * numHoras
ir = salarioBruto * (11 / 100)
inss = salarioBruto * (8 / 100)
sindicato = salarioBruto * (5 / 100)
descontos = ir + inss + sindicato
print(f'Salário bruto: {salarioBruto:.2f}')
print(f'Descontos: R$ {ir:.2f} + R$ {inss:.2f} + R$ {sindicato:.2f}')
print(f'Salário líquido: {(salarioBruto - descontos):.2f}')
