'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
 de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
  Faça um programa que calcule e escreva o número de anos necessários para que a população 
  do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

pop_A = 80000
txA =  0.03
pop_B = 200000
txB = 0.015
i = 0
anos = 0
while True:
    pop_A = pop_A + (pop_A * txA )
    pop_B = pop_B + (pop_B * txB)
    i += 1
    print(pop_A)
    print(pop_B)
    if pop_A >= pop_B:
        break
print(i)

#Continuação

'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
 Valide a entrada e permita repetir a operação.'''

i = 0
anos = 0
while True:
    pop_A = float(input('informe qtos habitantes tem A:'))
    txA = float(input('Informe a taxa de crescimento da A:'))
    pop_B = float(input('informe qtos habitantes tem B:'))
    txB = float(input('Informe a taxa de crescimento da B:'))
    while True:
        pop_A = pop_A + (pop_A * txA )
        pop_B = pop_B + (pop_B * txB)
        i += 1
        print(pop_A)
        print(pop_B)
        if pop_A >= pop_B:
            break
    print(i)
    opcao = input('quer colocar mais um numero de habitantes e mais uma tx de crescimento? S/N').lower()
    if opcao == 's':
        continue
    else:
        break
print(i)
