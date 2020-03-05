##########################################
# Arquivo: jokenpo.py
# Copyright (c) 2019-2020
# John Reilly
# Jogo de jokenpô, Maquina x Humano com a
# voz do R2D2, sugerido no livro
# "Deus é Programador"
##########################################

import random
import pygame
import os
import time
pygame.init()


def robotvoice(qual):
    if qual == 0:
        pygame.mixer.music.load('ExcitedR2D2.mp3')
        pygame.mixer.music.play()
    elif qual == 1:
        pygame.mixer.music.load('WEEEOOOOWW.mp3')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('HappyConfirmationR2D2.mp3')
        pygame.mixer.music.play()


def jokempo(valor):
    if valor == 1:
        print("""
        MMMMMMMMMMMMMMMMMMMMM0;   'kMWo. .,kMMMMMMMMMMMMMM
        MMMMMMMMMMMMMM0o::cdc lk0Oo.'.,dOko.'NMMMMMMMMMMMM
        MMMMMMMMMMMMN..xKX0c dMMMMMO ,MMMMMO xMMMMMMMMMMMM
        MMMMMMMMMWKOl OMMMMW cMMMMMK dMMWKOc kMMMMMMMMMMMM
        MMMMMMMX;.;l; :MMMMM'.MMMMMx ll'.;lo:.:NMMMMMMMMMM
        MMMMMMM,.WMMM: KMMMMl XOl;'.'ckNMMMMMN,.KMMMMMMMMM
        MMMMMMM. XMMMW.,MMMMO l cXMMMMMMMMMX;0W; KMMMMMMMM
        MMMMMMN  'WMMMO xMMMW ;'.OWMMMMMMWk.'NMW,.XMMMMMMM
        MMMMMM0 c.'NMMM, OMMK  '   .'''.. :OMMMMN.,MMMMMMM
        MMMMMMO kNc.;lc.,;,,,oK: ;xNMMMWx;.';KMMMd 0MMMMMM
        MMMMMMk OMMWKO0NMMMMWc lNMMMMMMMMMMWNMMMMd OMMMMMM
        MMMMMMk OMMMMMMMMMMX..XMMMMMMMMMMMMMMMMM0 ;MMMMMMM
        MMMMMM0 xMMMMMMMMMX.,WMMMMMMMMMMMMMMMMX:.dMMMMMMMM
        MMMMMMX lMMMMMMMMMNxWMMMMMMMMMMMMMMM0;.oNMMMMMMMMM
        MMMMMMMo 0MMMMMMMMMMMMMMMMMMMMMK:.cKMMMMMMMMMMMMMM
        MMMMMMMW..NMMMMMMMMMMMMMMMMMMMc oWMMMMMMMMMMMMMMMM
        MMMMMMMMN..XMMMMMMMMMMMMMMMMMX lMMMMMMMMMMMMMMMMMM
        MMMMMMMMMN lMMMMMMMMMMMMMMMMMO xMMMMMMMMMMMMMMMMMM
        MMMMMMMMMX oMMMMMMMMMMMMMMMMMX oMMMMMMMMMMMMMMMMMM
        MMMMMMMMM0 dMMMMMMMMMMMMMMMMMW ;MMMMMMMMMMMMMMMMMM
        MMMMMMMMMO cOOOOOOOOOOOOOOOOOO..MMMMMMMMMMMMMMMMMM""")
    elif valor == 2:
        print("""
        MMMMMMMMMMMMMMMMMMMMWc.  ;XMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMXKKWMMMMMM; oOd..WMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMO..;'.oWMMMX cMMMd kMMMMMKl;;c0MMMMMMMMMMM
        MMMMMMMM; OMMO lMMMX lMMMk dMMMMx ,kd  XMMMMMMMMMM
        MMWWMMMMN..WMMN.'WMX lMMMx kMMK..WMMO ,MMMMMMMMMMM
        x....dWMMd dMMMd xMX lMMMd OMW' OMMW' 0MMMMMMMMMMM
         ,MWx..KMW..XMMW,.WX lMMMo 0Mo lMMMx cMMMMMMMMMMMM
        : kMMK..0Md :MMM0 oX lMMMl KX 'WMMM' XMMMMMMMMMMMM
        W; dMMN, dN. 0MMM; k lMMMc 0, KMMMk lMMMMMMMMMMMMM
        MWc cWMWl cx 'WMMO . lMMM: ; oMMMN..NMMMMMMMMMMMMM
        MMMx ,XMMO.'. xMMM:  lMMM;  'WMMMl oMMMMMMMMMMMMMM
        MMMMO..KMMK.  .WMMNk0NMMMNXXWMMMX .NMMMMMNOddd0NMM
        MMMMMK..0MMN:;dWMMMMMMMMMMMMMMMMl oMMMM0, 'coc'.:K
        MMMMMMX' kMMMMMMMMMMMMMMMMMMMMMMd cMMNl cXMMMWx..d
        MMMMMMMk cMMMMMMMMMMMMMMMMMMMMMMX .;..,OMMMNd.'xWM
        MMMMMMMo dMMMMMMMMMMMMMMMMMMMM0c..ckNMMMMXc.,OMMMM
        MMMMMMMd oMMMMMMMMMMMMMMMMMM0' :0MMMMMMWl ,KMMMMMM
        MMMMMMMK .WMMMMMMMMMMMMMMMMN;cXMMMMMMMK..xWMMMMMMM
        MMMMMMMMMd lMMMMMMMMMMMMMMMMMMMMWx, cXMMMMMMMMMMMM
        MMMMMMMMMMc lWMMMMMMMMMMMMMMMMXo..lXMMMMMMMMMMMMMM
        MMMMMMMMMMWd..OMMMMMMMMMMMMMO,.,kWMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMNo lMMMMMMMMMMMM,.NMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMM.'MMMMMMMMMMMM,.MMMMMMMMMMMMMMMMMMMM""")
    else:
        print("""
        MMMMMMMMMMMMMMMMMMMWxllkMMMMMMMMMMWMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMN.lKK,,MMMMMMW;':,,XMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMM,;MMM,,MMMMW.oMMX 0MMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMx WMMO KMMMx WMMl.MMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMW xMMM.:MMM.cMMM.oMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMM;,MMMO XM0 XMM0 XMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMK',ll.oMMMO x 0MMM dMMMMMMMMMMMMMM
        MMMMMMMMMMMMMx;;.;MMMo.MMMMk:OMMM0 XMMMMMMMMMMMMMM
        MMMMMMMMMMMMo.NMo.MMMo.;;;;cdOXMMx MMMMMMMMMMMMMMM
        MMMMMMMMMMMMl.MMW.dMM':MMMMXOdc;,' MMMMMMMMMMMMMMM
        MMMMMMMMMMMMK OMMO KMX.:XMMMMMMMMO OMMMMMMMMMMMMMM
        MMMMMMMMMMMMW  KMMo.XMMx ';ldWMMMMc.MMMMMMMMMMMMMM
        MMMMMMMMMMMMM.'.c00, ;;,ol.o 0MMMMN OMMMMMMMMMMMMM
        MMMMMMMMMMMMM:'MOdokNMMM,'NModMMMMM.oMMMMMMMMMMMMM
        MMMMMMMMMMMMMX OMMMMMMMK.WMMMMMMMMO XMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMO.lNMMMMMMMMMMMMWo.kMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMWx,,lkKXNNNKOo;'dWMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMWKxolcccldOWMMMMMMMMMMMMMMMMMMM""")


opcoes = [1, 2, 3]

resp = 's'
while resp.lower() == 's':
    random.shuffle(opcoes)
    maquina = opcoes[0]
    ganhador = 2
    os.system('cls' if os.name == 'nt' else 'clear')
    # O comando acima limpa a tela se executado pelo
    # terminal do sistema operacional, com o comando
    # python3 jokenpo.py
    # Pelo terminal do PyCharm, pelo menos em Linux,
    # dá o erro "TERM environment variable not set. 256"
    print('=' * 35)
    print('******** JOGO DE JO KEN PÔ ********')
    print('=' * 35)
    humano = int(input('Eu já escolhi minha opção entre:'
                       '\n1 - Pedra!'
                       '\n2 - Papel!'
                       '\n3 - Tesoura!'
                       '\nJogue a sua opção: '))

    if maquina == humano:
        jokempo(maquina)
        print('''
        ******HUMANO E MÁQUINA JOGARAM IGUAIS!******''')
        print('''
        ****************DEU EMPATE!*****************''')
        ganhador = 2
    elif maquina == 1 and humano == 3:
        jokempo(humano)
        print('''
        ***********HUMANO JOGOU TESOURA*************''')
        jokempo(maquina)
        print('''
        **************EU JOGUEI PEDRA***************''')
        print('''
        -------------------GANHEI-------------------''')
        ganhador = 0
    elif maquina == 1 and humano == 2:
        jokempo(humano)
        print('''
        ************HUMANO JOGOU PAPEL**************''')
        jokempo(maquina)
        print('''
        ***************EU JOGUEI PEDRA**************''')
        print('''
        ----------------HUMANO GANHOU---------------''')
        ganhador = 1
    elif maquina == 2 and humano == 1:
        jokempo(humano)
        print('''
        ************HUMANO JOGOU PEDRA**************''')
        jokempo(maquina)
        print('''
        ***************EU JOGUEI PAPEL**************''')
        print('''
        -------------------GANHEI-------------------''')
        ganhador = 0
    elif maquina == 2 and humano == 3:
        jokempo(humano)
        print('''
        ***********HUMANO JOGOU TESOURA*************''')
        jokempo(maquina)
        print('''
        ***************EU JOGUEI PAPEL**************''')
        print('''
        ----------------HUMANO GANHOU---------------''')
        ganhador = 1
    elif maquina == 3 and humano == 1:
        jokempo(humano)
        print('''
        ************HUMANO JOGOU PEDRA**************''')
        jokempo(maquina)
        print('''
        *************EU JOGUEI TESOURA**************''')
        print('''
        ----------------HUMANO GANHOU---------------''')
        ganhador = 1
    elif maquina == 3 and humano == 2:
        jokempo(humano)
        print('''
        ************HUMANO JOGOU PAPEL**************''')
        jokempo(maquina)
        print('''
        *************EU JOGUEI TESOURA**************''')
        print('''
        -------------------GANHEI-------------------''')
        ganhador = 0

    print('''
    ********************************************''')
    print('''
    ************VAMOS JOGAR DE NOVO?************''')
    robotvoice(ganhador)
    resp = str(input('''
    ****** Sim ou Não? s/n '''))[0]

print('''
    ********************************************''')
print('''
    *************** ATÉ A PRÓXIMA **************''')
print('''
    ********************************************''')
pygame.mixer.music.load('SnappyR2D2.mp3')
pygame.mixer.music.play()
time.sleep(1)
