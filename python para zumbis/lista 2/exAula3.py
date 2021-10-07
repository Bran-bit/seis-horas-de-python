'''
Modifique o programa da empresa Tchau
para uma promoção onde a tarifa é de R$ 0,08
quando você utiliza mais que 800 minutos.
'''
minutos = int(input('Minutos gastos: '))
print('Valor da conta') 
if minutos < 200:
    preco = 0.2
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08
print(f'R$ {(minutos * preco):.2f}')

