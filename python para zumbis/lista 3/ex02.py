'''
Faça um programa que leia um nome de
usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
usuario = input('Nome de usuário: ')
senha = input('senha: ')
while usuario == senha:
    print('Erro! Dados iguais. Informe-os novamente.')
    usuario = input('Nome de usuário: ')
    senha = input('senha: ')