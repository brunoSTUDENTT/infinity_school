Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'
  
 while True:
    nome = str(input('informe um nome: '))
    cont = 0
    for i in nome:
        cont += 1

    if cont <= 3:
        print("nome invalido. Informe um nome")
    else:
        print("nome registrado com sucesso")
        break
while True:
    idade = int(input('informe a idade: '))
    if idade < 0 or idade > 150:
        print('idade invalida. informe sua idade: ')
        continue
    else:
        print('idade registrada com sucesso')
        break

while True:
    salario = float(input('informe seu salario: '))
    if salario < 0:
        print('valor invalido. informe o salario: ')

    else:
        print('salario registrado com sucesso')
        break

while True:
    sexo = input('informe o sexo: [M/F]').lower()
    if sexo not in 'mf':
        print('Sexo invalido. Informe o sexo: ')
        continue
    else:
        print('sexo registrado com sucesso')
        break
while True:
    estado_civil = (input('informe o estado civil'))
    if estado_civil not in 'scvd':
        print('estado civil invalido. informe o estado civil: ')
    else:
        print('estado civil registrado com sucesso.')
        break
