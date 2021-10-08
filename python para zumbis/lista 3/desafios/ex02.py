# Não pode usar array ainda...
'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. 
Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado
desprezando os centavos. Suponha que as notas para troco sejam as de 50, 20, 10,
5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
'''
# 1. Saber quanto deve de troco
# 2. Descontar o valor começando pelas notas maiores 
# (tem que verificar se é >= ao valor)
# 3. Ir armazenando o valor de quantas notas a partir do processo de descontar
despesa = float(input('Valor da conta: '))
pagamento = float(input('Valor pago: '))
while pagamento <= despesa:
    pagamento = float(input('Valor insuficiente. Pague com uma quantia maior: '))
troco = pagamento - despesa
trocoDescontar = troco
n50 = n20 = n10 = n5 = n1 = 0
# Enquanto o troco não estiver zerado nos descontos,
# Obs: quando o troco for menor que 0, é porque faltam os centavos
# devolvidos através de uma nota de 1 real
while trocoDescontar > 0:
    if trocoDescontar >= 50:
        n50 += 1
        descontaNota = 50
    elif trocoDescontar >= 20:
        n20 += 1
        descontaNota = 20
    elif trocoDescontar >= 5:
        n5 += 1
        descontaNota = 5
    else:
        n1 += 1
        descontaNota = 1
    trocoDescontar -= descontaNota
print(f'Você pagou R$ {pagamento:.2f} para a dívida de R$ {despesa:.2f}.')
print(f'Portanto, deverá receber R$ {troco:.2f} em notas de: ')
if n50 > 0:
    print(f'{n50} notas de 50.')
if n20 > 0:
    print(f'{n20} notas de 20.')
if n10 > 0:
    print(f'{n10} notas de 10.')
if n5 > 0:
    print(f'{n5} notas de 5.')
if n1 > 0:
    print(f'{n1} notas de 1.')

