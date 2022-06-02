#----INICIO DA FUNÇÃO INTRODUÇÃO----

def intro (s1,s2,s3): #função para cabeçalho

    print('|','--' * 25,'|')
    print('|','-' * 13,s1,'-' * 13,'|')
    print('|','--' * 9,s2,'-' * 19,'|')
    print('|','--' * 25, '|')
    print('|','-'*6,s3,'-'*8,'|')
    print('|','--' * 25,'|')

# ----FIM DA FUNÇÃO INTRODUÇÃO----
#*****************************************************************

# ---- INICIO DA FUNÇÃO CADASTRAR PEÇA ----
listapecas = []
def cadastrobike(codigo):
    print('Você selecionou a opção - Cadastrar Peças.')
    print('Código da Peça {:03d}'.format(codigo))
    nome = input('Por Favor! Entre com o NOME da peça:')
    fabricante = input('Agora,Informe o FABRICANTE da peça:')
    valor = float(input('Entre com o VALOR da peça? R$ '))
    dicionariopecas = {'Código': codigo,
                       'Nome      ': nome,
                       'Fabricante': fabricante,
                       'Valor (R$)': valor}
    listapecas.append(dicionariopecas.copy())

# ---- FIM DA FUNÇÃO CADASTRAR PEÇA ----
#******************************************************************

# ---- INICIO DA FUNÇÃO CONSULTAR PEÇA ----
def consultabike():
    while True:
        try:  # Tentar as condiçoes abaixo
            print('Você selecionou a opção - Consultar Peça.')
            consultapeca = int(input('Escolha a opção desejada:\n'
                                  '1-Consultar todas as Peças\n'
                                  '2-Consultar Peças por Código\n'
                                  '3-Consultar Peças por Fabricante\n'
                                  '4-Retornar'
                                  '>>'))
            if consultapeca == 1:
                print('__' * 20)
                for peças in listapecas: #selecionar cada dicionario da minha lista
                    for key, value in peças.items():#selecionar cada conjunto chave : valor do dicionário
                        print('{} : {}'.format(key,value))
            elif consultapeca == 2:
                print('__'* 20)
                entrada = int(input('Digite o código desejado:'))
                for peças in listapecas:
                    if (peças['Código'] == entrada):
                        for key, value in peças.items():
                            print('{} : {}'.format(key, value))
            elif consultapeca == 3:
                print('__'* 20)
                entrada = input('Digite o Fabricante:')
                for peças in listapecas:
                    if (peças['Fabricante'] == entrada):
                        for key, value in peças.items():
                            print('{} : {}'.format(key, value))
            elif consultapeca == 4:
                break
            else:
                print('Por Favor! Digite uma opção válida.')
                continue  # volta ao começo do while

        except ValueError:  # Caso o usuário digite uma caracter não numérico.
            print('Ooops! Você digitou um valor não numerico.')
            print('Por favor, Informe novamente a opção desejada.')

# ---- FIM DA FUNÇÃO CONSULTAR PEÇA ----

# ---- INICIO DA FUNÇÃO REMOVER PEÇA ----
def removebike():
    print('__'* 20)
    print('você selecionou a opção - Remover Peça.')
    entrada = int(input('Digite o Código a ser Removido:'))
    for peças in listapecas:
        if (peças['Código'] == entrada):
            listapecas.remove(peças)

# ---- FIM DA FUNÇÃO REMOVER PEÇA ----



#----INICIO DO PROGRAMA PRINCIPAL----

intro('Aluno:Alexandre Guedes',' RU:3992768','Controle de Estoque - Bicicletaria', )
contadorbike = 0
while True:
    try:  # Tentar as condiçoes abaixo
        print('Bem Vindo! ')
        escolha = float(input('Escolha a opção desejada:\n'
                          '1-Cadastrar Peças\n'
                          '2-Consultar Peças\n'
                          '3-Remover Peças\n'
                          '4-Sair'
                          '>>'))

        if escolha == 1:
            contadorbike = contadorbike + 1
            cadastrobike(contadorbike)
        elif escolha == 2:
            consultabike()
        elif escolha == 3:
            removebike()
        elif escolha == 4:
            print('Programa Finalizado.')
            break
        else:
            print('Por Favor! Digite uma opção válida.')
            continue  # volta ao começo do while

    except ValueError:  # Caso o usuário digite uma caracter não numérico.
        print('Ooops! Você digitou um valor não numerico.')
        print('Por favor, Informe novamente a opção desejada.')
        continue

