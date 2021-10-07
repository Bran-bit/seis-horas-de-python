'''
Solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar.
'''
preço = float(input("Valor da mercadoria: R$ "))
desconto = float(input("Percentual de desconto: R$ "))
valorDesconto = preço * (desconto / 100)
print(f'Valor do desconto: R$ {valorDesconto:.2f}')
print(f'Preço a pagar: R$ {(preço - desconto):.2f}')