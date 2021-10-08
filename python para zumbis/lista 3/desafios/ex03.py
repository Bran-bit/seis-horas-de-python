# Verifique se um inteiro positivo n é primo.
# Condição para ser primo: ser divisível apenas por 1 e por ele mesmo.

# 1. Ir testando a divisibilidade por todos os números, começando pelo 2 (1 e 0 sempre deixam o resto 0)
# 2. Ou o laço irá sair quando divisor < num e divisor % num == 0, ou quando número = num.
num = int(input('Informe um número inteiro e positivo: '))
divisor = 1
while divisor <= num:
    if num % divisor == 0 and num != 1:
        if divisor < num:
            print(f'{num} não é um número primo, pois é divisível por {divisor}.')
            break
        elif divisor == num:
            print(f'{num} é um número primo.')
    divisor += 1
    