'''
Calcule o tempo de uma viagem de carro. 
Pergunte a distância a percorrer e a velocidade média
esperada para a viagem
'''
distancia = float(input('Digite quantos kms de distância: '))
velocidadeMedia = float(input('Digite a velocidade média do veículo (km/h): '))
tempo = distancia / velocidadeMedia
print(f'O tempo de viagem será de {tempo} horas.')