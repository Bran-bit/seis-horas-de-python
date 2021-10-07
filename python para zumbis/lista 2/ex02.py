'''
Determine se um ano é bissexto.
'''

import calendar

ano = int(input('Digite um ano: '))
if calendar.isleap(ano):
    print('Bissexto')
else:
    print('Não é bissexto')