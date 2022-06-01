print('----------------------------------------------------------')
print('--------------- BEM VINDO A NOSSA LANCHONETE -------------')
print('------------ ALUNO: ALEXANDRE GUEDES RU:3992768 ----------')
print('----------------------------------------------------------')
print('-------------------- NOSSO CARDÁPIO ----------------------')
print('----------------------------------------------------------')
print('[CÓDIGO]----------[DESCRIÇÃO]------------------[VALOR(R$)]')
print('  [100]        CACHORRO - QUENTE                 R$9,00')
print('  [101]        CACHORRO - QUENTE DUPLO           R$11,00')
print('  [102]        X-Egg                             R$12,00')
print('  [103]        X-SALADA                          R$13,00')
print('  [104]        X-BACON                           R$14,00')
print('  [105]        X-TUDO                            R$17,00')
print('  [200]        REFRIGERANTE LATA                 R$5,00')
print('  [201]        CHÁ GELADO                        R$4,00')
print('----------------------------------------------------------')
total = 0   #variável para receber os valores de entrada
while True:

    codigo = int(input('Entre com o código do produto desejado:'))

    if (codigo == 100):
        valor = 9
        print('Você pediu um Cachorro-Quente no valor de R$9,00')

    elif (codigo == 101):
        valor = 11
        print('Você pediu um Cachorro-Quente duplo no valor de R$11,00')

    elif (codigo == 102):
        valor = 12
        print('Você pediu um X-Egg no valor de R$12,00')

    elif (codigo == 103):
        valor = 13
        print('Você pediu um X-Salada no valor de R$13,00')

    elif (codigo == 104):
        valor = 14
        print('Você pediu um X-Bacon no valor de R$14,00')

    elif (codigo == 105):
        valor = 17
        print('Você pediu um X-Tudo no valor de R$17,00')

    elif (codigo == 200):
        valor = 5
        print('Você pediu um Refrigerante Lata no valor de R$5,00')

    elif (codigo == 201):
        valor = 4
        print('Você pediu um Chá Gelado no valor de R$4,00')
    else:
        print('Opção Invalida!')
        continue   # volta ao começo do while
    total = total + valor   #soma do total das entradas

    print('Deseja pedir mais alguma coisa?')
    print('1 - sim')
    print('0 - não')
    saida = int(input('>>'))


    if saida == 1:
        continue
    elif saida == 0:
        print('Pedido Finalizado!')
        print('O Total a ser pago é: R${:.2f}'.format(total))
        break

    else:
        print('Código Inválido!')



