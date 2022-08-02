'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer
 um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando 
 o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo,
  do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''

maior_peso = 0
cod_maior_peso = 0
menor_peso = 200
cod_menor_peso = 0
maior_alt = 0
cod_maior_alt = 0
menor_alt = 2.30
cod_menor_alt = 0
media_peso = 0
soma_alt = 0
soma_peso = 0
cont = 0
while True:
    codigo = int(input('informe o codigo: '))
    if codigo == 0:
        break
    altura = float(input('informe a altura:'))
    peso = float(input('informe o peso: '))


    if menor_alt > altura:
        menor_alt = altura
        cod_menor_alt = codigo
    if maior_alt < altura:
        maior_alt = altura
        cod_maior_alt = codigo
    soma_alt += altura


    if menor_peso > peso:
        menor_peso = peso
        cod_menor_peso = codigo
    if maior_peso < peso:
        maior_peso = peso
        cod_maior_peso = codigo
    soma_peso += peso
    cont += 1


media_alt = soma_alt / (cont)
media_peso = soma_peso / (cont)
print(f'o cliente mais alto tem {maior_alt}m, o mais baixo {menor_alt} e a media de altura dos clientes foi de {media_alt}m')
print(f'o cliente mais gordo tem {maior_peso}kg, o mais magro tem {menor_peso}kg e a media de peso dos clientes foi de {media_peso}kg')
print(f' o codigo do mais alto é {cod_maior_alt}, do mais baixo {cod_menor_alt} do mais pesado é {cod_maior_peso} e do mais leve {cod_menor_peso}')
