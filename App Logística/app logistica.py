#----INICIO DA FUNÇÃO INTRODUÇÃO----

def intro (s1,s2,s3): #função para cabeçalho

    print('|','--' * 20,'|')
    print('|','-' * 8,s1,'-' * 8,'|')
    print('|','--' * 7,s2,'-' * 13,'|')
    print('|','--' * 20, '|')
    print('|','-'*6,s3,'-'*5,'|')
    print('|','--' * 20,'|')

#----FIM DA FUNÇÃO INTRODUÇÃO----



#----INICIO DA FUNÇÃO DIMENSÕES----
def dimensoes ():#função para cálcula da dimensão do pacote / comprimento * altura * largura

    while True:
        try:# Tentar as condiçoes abaixo

            c = float(input('Digite o comprimento do pacote em cm: '))
            a = float(input('Digite a altura do pacote em cm: '))
            l = float(input('Digite a largura do pacote em cm: '))
            res = c * a * l #comprimento * altura * largura

            if res <= 1000:
                print('O volume do Objeto é: {}cm3'.format(res))
                return 10 #valor referente a dimensão
            elif res >= 1001 and res <= 10000:
                print('O volume do Objeto é: {}cm3'.format(res))
                return 20
            elif res >= 10001 and res <= 30000:
                print('O volume do Objeto é: {}cm3'.format(res))
                return 30
            elif res >= 30001 and res <= 100000:
                print('O volume do Objeto é: {}cm3'.format(res))
                return 50
            else:
                print('Desculpe, não aceitamos objetos tão grandes!')
                continue # volta ao começo do while

        except ValueError:# Caso o usuário digite uma caracter não numérico.
            print('Ooops! Você digitou um valor não numerico.')
            print('Por favor, entre com as dimensões desejadas.')
            continue

#----FIM DA FUNÇÃO DIMENSÕES----



#----INICIO DA FUNÇÃO PESO----
def peso ():

    while True:
        try:# Tentar as condiçoes abaixo
            p = float(input('Digite o peso do pacote em Kg \n'
                            'O peso Máximo permitido é 30Kg) \n'
                            '>>'))

            if p <= 0.1:
                print('O peso do pacote é: {}Kg'.format(p))
                return 1 #multiplicador do peso
            elif p >= 0.11 and p <= 1:
                print('O peso do pacote é: {}Kg'.format(p))
                return 1.5
            elif p >= 1.10 and p <= 10:
                print('O peso do pacote é: {}Kg'.format(p))
                return 2
            elif p >= 10.1 and p <= 30:
                print('O peso do pacote é: {}Kg'.format(p))
                return 3
            else:
                print('Desculpe, pacote fora do peso permitido!')
                print('Por Favor! Informe o peso novamente.')
                continue  # volta ao começo do while

        except ValueError:  # Caso o usuário digite uma caracter não numérico.
            print('Ooops! Você digitou um valor não numerico.')
            print('Por favor, Informe novamente o peso.')
            continue

#----FIM DA FUNÇÃO PESO----



#----INICIO DA FUNÇÃO ROTA----
def rota ():

    while True:
        try:# Tentar as condiçoes abaixo

            print('BR', ' - De Brasilia para Rio de Janeiro')
            print('BS', ' - De Brasilia para São Paulo')
            print('RB', ' - De Rio de Janeiro para Brasilia')
            print('RS', ' - De Rio de Janeiro para São Paulo')
            print('SR', ' - De São Paulo para Rio de Janeiro')
            print('SB', ' - De São Paulo para Brasilia')
            rt = input('Selecione a rota: ')

            if rt == 'RS':
                print('Rota escolhida [Rio de Janeiro / São Paulo]')
                return 1 #multiplicador referente a rota.
            elif rt == 'SR':
                print('Rota escolhida [São Paulo / Rio de Janeiro]')
                return 1
            elif rt == 'BS':
                print('Rota escolhida [Brasilia / São Paulo]')
                return 1.2
            elif rt == 'SB':
                print('Rota escolhida [São Paulo / Brasilia]')
                return 1.2
            elif rt == 'BR':
                print('Rota escolhida [Brasilia / Rio de Janeiro]')
                return 1.5
            elif rt == 'RB':
                print('Rota escolhida [Rio de Janeiro / Brasilia]')
                return 1.5
            else:
                print('Você digitou uma rota inexistente!')
                print('Por Favor! entre com a rota desejada novamente.')
                continue # volta ao inicio do while

        except:  # Caso o usuário digite uma caracter inválido.
            print('Por favor, Informe novamente a rota desejada.')
            break

#----FIM DA FUNÇÃO ROTA----



#----INICIO DO PROGRAMA PRINCIPAL----

intro('Aluno:Alexandre Guedes',' RU:3992768','Bem vindo a UNI-Transportes', )
dm = dimensoes()
pe = peso()
rt = rota()
total = dm * pe * rt
print('O total a pagar é: R${:.2f},(Dimensões: {} * Peso: {} * Rota: {} '.format(total,dm,pe,rt))
