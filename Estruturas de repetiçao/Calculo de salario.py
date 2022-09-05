'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do imposto de Renda,
 que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
  a 11% do salário bruto, mas não é descontado (é a empresa que deposita.)O salário líquido corresponde
   ao salário bruto menos os descontos O programa deverá pedir ao usuário o valor da sua hora e a quantidade
    de horas trabalhadas no mês.
a. Desconto do IR;
b. Salário Bruto ate R$900,00 (inclusive) – Isento;
c. Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;
d. Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
e. Salário bruto acima de 2500 – Desconto de 20%.
Imprima na tela as informações, dispostas conforme o exemplo abaixo, 
no exemplo valor da hora é 5 e a quantidade de horas é 220.  Salário bruto (5 * 220)  : R$  
 1100,00( – ) IR (5%) : R$  55,00( – ) INSS ( 10% )  : R$  110,00( – ) Sindicato(3%)  
  : R$      33,00FGTS ( 11%)     : R$     121,00Total de descontos     : R$  198,00Salário Líquido  
   : R$     902,00 '''

valor_hora = float(input('Informe o valor da hora trabalhada: '))
qtde_horas = int(input(' Informe o total de horas trabalhadas no mês: '))
salario_bruto = valor_hora * qtde_horas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.2

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
desc_sind = salario_bruto * 0.03

print('O valor do salario bruto é de:', salario_bruto)
print('O desconto de imposto de renda é:',ir)
print('O valor de desconto do INSS é de: ', salario_bruto * 0.1)
print('O valor de desconto para FGTS é de: ', salario_bruto * 0.11)
print('o valor de desconto do sindicato é de: ',salario_bruto * 0.03)

total_desc = ir + desc_sind + inss
salario_liquido = salario_bruto - total_desc

print( 'o total de descontos é: ',total_desc)
print('o salario liquido é: ',salario_liquido)
    
    
