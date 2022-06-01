print ('----------------------------------------------------------')
print ('------------------ BEM VINDO A NOSSA LOJA ----------------')
print ('------------ ALUNO ALEXANDRE GUEDES RU:3992768 -----------')
print ('----------------------------------------------------------')
vp = float(input('Informe o valor unitário do produto:R$'))  #vp (valor do produto)
qtd = int(input('Informe a quantidade desejada:'))
print ('----------------------------------------------------------')
if qtd >= 1 and qtd <=9:  # limita o intervalo entre 1 e 9.
   print('Desconto fornecido somente para mais de 10 unidades.')
   print('O valor total sem desconto é de:R${:.2f}'.format(vp*qtd))
elif  qtd >= 10 and qtd <=99:  # limita o intervalo entre 10 e 99.
   valor = vp - (vp * 0.05)
   print('O valor total sem desconto é :R${:.2f}'.format(vp*qtd))
   print('O valor com desconto de 5% é :R${:.2f}'.format(valor*qtd))
elif  qtd >= 100 and qtd <=999:  # limita o intervalo entre 100 e 999.
   valor = vp - (vp * 0.10)
   print('O valor total sem desconto é :R${:.2f}'.format(vp*qtd))
   print('O valor com desconto de 10% é :R${:.2f}'.format(valor*qtd))
elif  qtd >= 1000:  # Aceita valores acima de 1000.
   valor = vp - (vp * 0.15)
   print('O valor total sem desconto é :R${:.2f}'.format(vp*qtd))
   print('O valor com desconto de 15% é :R${:.2f}'.format(valor*qtd))
else:
   print('Operação Inválida!')  # Inválido para quantidade 0.
