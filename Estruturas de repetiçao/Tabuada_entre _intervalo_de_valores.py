'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente
 iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:'''

tabuada = int(input('informe o valor a ser multiplicado'))
v_inicial = int(input('informe um valor incial: '))
v_final = int(input('informe um valor final: '))


for i in range(v_inicial ,v_final + 1):
    multiplicador = tabuada * i
    print(f' {tabuada} * {i} = {multiplicador}')
