'''
Pergunte a velocidade de um carro, supondo
um valor inteiro. Caso ultrapasse 110 km/h, exiba
uma mensagem dizendo que o usuário foi multado. Neste caso,
exiba o valor da multa, cobrando R$ 5,00 por km acima de 110
'''
velocidade = float(input('Velocidade (km/h): '))
if velocidade > 110:
    kmsAcima = (velocidade - 110)
    multa = kmsAcima * 5
    print(f'Você recebeu uma multa de {multa:.2f} por estar à {kmsAcima:.1f} km/h do permitido.')