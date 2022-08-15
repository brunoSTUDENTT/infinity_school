'''[LP-A02] De acordo ao estudado em aula, crie um programa que receba um número inteiro e calcule seu fatorial.
Exemplos:
5! = 5*4*3*2*1 = 120
8! = 8*7*6*5*4*3*2*1 = 40320'''

numero = int(input('informe um numero: '))
fatorial = 1
while numero > 0:
    fatorial *=  numero
    numero -= 1
print(' o resultado é igual a', fatorial)
