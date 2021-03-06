from datetime import date

cor = {  # cores normais

    'vermelho': '\033[31m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'branco': '\033[30m',
    'roxo': '\033[35m',
    'verde': '\033[32m',
    'ciano': '\033[36m',
    'limpa': '\033[m',
    'pretoEbranco': '\033[7;30;m',

    # cores em negrito

    'vermelhoEMnegrito': '\033[1;31m',
    'azulEMnegrito': '\033[1;34m',
    'amareloEMnegrito': '\033[1;33m',
    'brancoEMnegrito': '\033[1;30m',
    'roxoEMnegrito': '\033[1;35m',
    'verdeEMnegrito': '\033[1;32m',
    'cianoEMnegrito': '\033[1;36m',

    # cores sublinhadas

    'vermelhoSublinhado': '\033[4;31m',
    'azulSublinhado': '\033[4;34m',
    'amareloSublinhado': '\033[4;33m',
    'brancoSublinhado': '\033[4;30m',
    'roxoSublinhado': '\033[4;35m',
    'verdeSublinhado': '\033[4;32m',
    'cianoSublinhado': '\033[4;36m'
}

print('=' * 39)
print('Checar anos bissextos!')
print('Se digitar zero ele assume o ano atual!')
print('=' * 39)
ano1 = int(input('Digite o primeiro ano da sequência: '))
ano2 = int(input('Digite o ultimo ano da sequência: '))

if ano1 == 0:
    ano1 = date.today().year
if ano2 == 0:
    ano2 = date.today().year
for ano in range(ano1, ano2+1):
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        print('{}O ano {} é bissexto!'.format(cor['azul'], ano))
    else:
        print('{}O ano {} NÃO é bissexto!'.format(cor['branco'], ano))
