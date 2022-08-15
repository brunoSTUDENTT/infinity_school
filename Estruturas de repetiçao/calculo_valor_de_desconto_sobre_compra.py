'''Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos
 começam quando o cliente faz compras acima dos R$500. A cada 100 reais que ultrapasse esse valor, o cliente
  ganhará 1% de desconto, sendo este cumulativo até o limite de 25%. 
 Por exemplo: R$500 = 1% || R$600,00 = 2% … e assim por diante.
 Faça um programa que desenvolva uma tabela de descontos utilizando o formato abaixo, você deve atribuir 
  o valor de compra de cada cliente.
 valor da compra – porcentagem de desconto – valor final
 

Exemplo:
ENTRADA:

Compra = 520,00
SAÍDA:
520,00 ( Valor da compra ) - 1% ( Porcentagem ) = 514,80 ( Valor final )'''

# Resolução do exercicio:


total = float(input("Informe o valor total da compra: "))
if total < 500:
    print(f"{total} (Valor da compra)")

elif 500 <= total < 600:
    percent = 0.01
    desconto = total * 0.01
    total_desconto = total - desconto
    print(f"{total} (Valor da compra) - {percent*100}% (Porcentagem) = {total_desconto} (Valor final)")
else:
    percent = ((total - 500)/10000) + 0.01
    if percent > 0.25:
        percent = 0.25
    desconto = total * percent
    total_desconto = total - desconto
    print(percent)
    print(f"{total} - {(percent*100):.2f}%  = {total_desconto} ")
