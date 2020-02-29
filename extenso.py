##########################################
# Arquivo: extenso.py
# Copyright (c) 1990-2020
# John Reilly
# Teste da Função para Tradução de
# Valor por Extenso em Python 3,
# publicada no livro "Deus é Programador"
##########################################

from decimal import Decimal


# Função principal de chamada para converter
# valores numéricos por extenso: recebe os
# parâmetros valor numérico e prefixo da moeda.
def valextenso(valor, prefixo):
    # Avalia o argumento
    if valor == 0:
        # Retorna string 'zero' se o valor recebido for 0
        extenso = 'zero'
    else:
        # Converte valor em string
        str_valor = '%.2f' % valor
        # Calcula a quantidade de milhares
        n_milhares = (len(str_valor)) / 3

        # Condição com n_fracao (que ser=a = 3 ou 6) para completar
        # com 0 à esquerda no ultimo milhar (ordem inversa) caso
        # necessário. Esta tarefa é necessária para assegurar a
        # correta identificação dos milhares em listas e para
        # facilitar a descrição do ultimo milhar.
        n_fracao = int((n_milhares - int(n_milhares)) * 10)
        if n_milhares != int(n_milhares):
            n_milhares = int(n_milhares) + 1
            if n_fracao == 3:
                # Aqui faz com que uma string de 1 dígito
                # fique com 3 dígitos, por exemplo '5' -> '005'
                str_valor = "00" + str_valor
            elif n_fracao == 6:
                # Aqui faz um grupo de 2 dígitos ficar com 3,
                # exemplo '11' -> '011'
                str_valor = "0" + str_valor

        # Acrescenta um espaço no final da string com o valor
        str_valor += ' '

        # Separa Grupos Numéricos de milhares em lista
        lista_grupo_milhares = []
        for n_milhar in range(0, int(n_milhares)):
            # pricar é o número do primeiro carácter a ser lido na string
            pricar = n_milhar * 3
            # ate é o carácter após o último a ser lido na string
            ate = n_milhar * 3 + 3
            # Adiciona os milhares (de 3 em 3 dígitos) na lista
            lista_grupo_milhares.append(str_valor[pricar:ate])

        # n_milhares será o inteiro de si mesmo para ser usado como
        # parâmetro na próxima função, onde se lerá a lista milhar por milhar.
        n_milhares = int(n_milhares)
        # extensogrupo é a função que converterá cada string de milhar em uma
        # string com o extenso, exemplo: '159' -> 'cento e cinquenta e nove'
        extenso = extensogrupo(lista_grupo_milhares, n_milhares,
                               valor, prefixo)

    return extenso


# Função que concatena as strings com os extensos de cada milhar.
# É chamada pela função extensogrupo e recebe os parâmetros
# lista_extensogrupo, grupo_milhares, milhares, prefixo, v_valor
# transferindo-os para as variáveis/listas l_extensogrupo, g_milhares,
# n_milhares, v_prefixo, c_valor respectivamente.
def concatena(l_extensogrupo, g_milhares, n_milhares, v_prefixo, c_valor):
    # sinplu é a lista de nomes da escala dos milhares.
    sinplu = [' quatrilhão', ' quatrilhões', ' trilhão', ' trilhões',
              ' bilhão', ' bilhões', ' milhão', ' milhões', ' mil', ' mil']
    # contador_sinplu é o contador para sinplu com -1 para começar do último
    # para o primeiro, a partir da escala dos 'mil'. Será usado para extrair
    # os respectivos nomes plural e singular na lista de escala sinplu.
    contador_sinplu = -1

    # Terminações monetárias:
    # Converte para maiúsculo
    v_prefixo = v_prefixo
    # Verifica e define real, dólar ou euro.
    if v_prefixo == 'U':
        msinplur = [' dólar', ' dólares']
    elif v_prefixo == 'E':
        msinplur = [' euro', ' euros']
    else:
        # Usa o Real caso não seja válido.
        msinplur = [' real', ' reais']

    # dpcnn: Detecta a Primeira Casa Não Nula na lista, diferente de ''
    dpcnn = 0
    # Loop para ler a lista dos milhares convertidos por extenso,
    # começando a partir do penúltimo na lista, para concatenar apenas
    # a parte inteira do valor, ficando os centavos para outro loop.
    for milhar in range(-2, -n_milhares - 1, -1):
        # gmilhares é uma string que separa cada um dos milhares na lista por vez,
        # para algumas condições saberem o que fazer na hora de concatenar.
        gmilhares = g_milhares[milhar]

        if dpcnn == 0:
            # Se a primeira casa não nula (!= '') for encontrada, dpcnn passa a
            # ser igual a 1 para a função saber que já foi encontrada.
            if l_extensogrupo[milhar] != '':
                dpcnn = 1
                # Concatena com ' e ' se não houver ' e ' na string e
                # não for o último na leitura inversa da lista (!= -n_milhares)
                if ' e ' not in l_extensogrupo[milhar] and milhar != -n_milhares:
                    l_extensogrupo[milhar] = ' e ' + l_extensogrupo[milhar]
                elif milhar != -n_milhares:
                    l_extensogrupo[milhar] = ', ' + l_extensogrupo[milhar]
        else:
            # Se a string não for nula e não for a última concatena com ', '
            if l_extensogrupo[milhar] != '' and milhar != -n_milhares:
                l_extensogrupo[milhar] = ', ' + l_extensogrupo[milhar]

        if milhar <= -3:
            # A partir do terceiro na leitura inversa, verifica se o valor
            # corresponde a 1, >1 ou 0, para acrescentar o plural, singular
            # (ou nada) correspondente na lista de escala sinplu.
            if int(gmilhares) == 1:
                sinp = sinplu[contador_sinplu - 1]
            elif int(gmilhares) > 1:
                sinp = sinplu[contador_sinplu]
            else:
                sinp = ''
            l_extensogrupo[milhar] = l_extensogrupo[milhar] + sinp
            # O contador_sinplu pula 2 casas para o próximo milhar
            contador_sinplu -= 2

    # Concatena os extensos de cada grupo de milhar da parte inteira
    # na variável ext_concatenado.
    ext_concatenado = ''
    for milhar in range(-2, -n_milhares - 1, -1):
        ext_concatenado = l_extensogrupo[milhar] + ext_concatenado

    # Coloca a terminação de moeda em plural ou singular
    # decidindo, por exemplo, se é 'real' ou 'de reais',
    # usando a variável c_valor no critério.
    if int(c_valor) > 0:
        if int(c_valor) == 1:
            ext_concatenado += msinplur[0]
        else:
            # Decide se coloca ' de' antes do nome da moeda.
            # Ex: 'dois milhões de reais'
            if str(int(c_valor))[-6:] == '000000':
                ext_concatenado += ' de' + msinplur[1]
            else:
                ext_concatenado += msinplur[1]

    # Tratando a casa dos centavos, se plural ou singular.
    if l_extensogrupo[-1] != '':
        gmilhares = g_milhares[-1]
        # Se for 1 centavo. É necessário o fatiamento por causa do '.' na string.
        if int(gmilhares[1:3]) == 1:
            l_extensogrupo[-1] = l_extensogrupo[-1] + ' centavo'
        # Se for mais de 1 centavo
        elif int(gmilhares[1:3]) > 1:
            l_extensogrupo[-1] = l_extensogrupo[-1] + ' centavos'

        if int(c_valor) > 0 and int(gmilhares[1:3]) > 0:
            # Acrescenta ' e ' caso a parte inteira e os centavos sejam >0
            l_extensogrupo[-1] = ' e ' + l_extensogrupo[-1]

        # Adiciona os centavos à variável de concatenação.
        ext_concatenado += l_extensogrupo[-1]

    return ext_concatenado


# Faz a conversão extenso dos valores de cada milhar na lista grupo_milhares.
def extensogrupo(grupo_milhares, milhares, v_valor, prefixo):
    # Listas de nomes dos dígitos
    unidade = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
               'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

    dezena = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
              'sessenta', 'setenta', 'oitenta', 'noventa', '*']

    centena = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos',
               'quinhentos', 'seiscentos', 'setecentos',
               'oitocentos', 'novecentos', 'mil']

    # A lista_extensogrupo, é onde serão listados os valores por extenso.
    lista_extensogrupo = []
    # str_moeda é para concatenar o valor numérico em formato de moeda.
    str_moeda = ''
    for milhar in range(0, milhares):
        grupo_num = grupo_milhares[milhar]
        grupo_ext = ''
        # centavo é para avisar quando o grupo ('.00') for dos centavos:
        centavo = ''
        for digito in range(0, 3):
            # Caso seja o grupo dos centavos substitui '.' por '0' para
            # se referir nas listas de nomes dos dígitos.
            if '.' in grupo_num:
                grupo_num = '0' + grupo_num[1:3]
                centavo = 's'

            # Nomeia dígito das centenas
            if digito == 0:
                if grupo_num == '100':
                    grupo_ext = grupo_ext + 'cem'
                else:
                    # Caso não seja '100' o nome será 'cento'.
                    grupo_ext = grupo_ext + centena[int(grupo_num[0])]

                # Decide se deve adicionar ' e ' após centena
                if int(grupo_num[0]) > 0 and int(grupo_num[1:3]) > 0:
                    grupo_ext = grupo_ext + ' e '

            # Nomeia dígito das dezenas e de 10 a 19
            if digito == 1:
                if grupo_num[1:3] == '10':
                    grupo_ext = grupo_ext + 'dez'
                # de 11 a 19
                elif 10 < int(grupo_num[1:3]) < 20:
                    grupo_ext = grupo_ext + unidade[int(grupo_num[1:3])]
                else:
                    grupo_ext = grupo_ext + dezena[int(grupo_num[1])]
                    # Decide se deve adicionar ' e ' após dezena a partir de 20
                    if int(grupo_num[2]) > 0 and int(grupo_num[1]) > 0:
                        grupo_ext = grupo_ext + ' e '

            # Nomeia dígito das unidades se o valor não for de 10 a 19.
            if digito == 2:
                if not (10 < int(grupo_num[1:3]) < 20):
                    grupo_ext = grupo_ext + unidade[int(grupo_num[2])]

            # Caso seja o grupo dos centavos devolve o '.' à string.
            if centavo == 's':
                grupo_num = '.' + grupo_num[1:3]

        # Cria a string do valor em formato moeda.
        if '.' not in grupo_num:
            # Se não for a escala dos centavos concatena com ponto.
            str_moeda = str_moeda + grupo_num + '.'
        else:
            # Se for a escala dos centavos concatena com vírgula.
            str_moeda = str(int(str_moeda[0:3])) \
                        + str_moeda[3:-1] + ',' + grupo_num[1:3]

        # Adiciona cada grupo de milhar na lista de extensos.
        lista_extensogrupo.append(grupo_ext)

    # Adiciona R$, U$ ou E$ na string do formato moeda.
    prefixo = prefixo
    if prefixo != 'U' and prefixo != 'E':
        prefixo = 'R'
    str_moeda = prefixo + '$ {}'.format(str_moeda)

    # extenso_completo receberá o valor por extenso concatenado.
    extenso_completo = concatena(lista_extensogrupo, grupo_milhares,
                                 milhares, prefixo, v_valor)

    # moeda_e_extenso é uma lista que será retornada com a
    # string do formato moeda e o extenso_completo.
    moeda_e_extenso = [str_moeda, extenso_completo]

    return moeda_e_extenso


valorin = -1
while valorin < 0 or valorin > 69999999999999.99:
    # Solicitará um número enquanto valorin <0 ou >=70 trilhões.
    # A função está preparada para converter valores até 999 quatrilhões,
    # mas esse limite foi colocado devido a uma dificuldade do Python 3 em
    # lidar com números grandes e mantê-los intactos, sem arredondamentos.
    valorin = Decimal(input('Digite um valor de 0 a 69999999999999.99: '))

currency = str(input('Digite U para Dolar, E para Euro ou R para Real.'
                     '\nSe você digitar algo errado, o Real será adotado:'
                     ' ')).upper().strip()[0]

# Chama a função principal com parâmetros valor e o identificador 'u', 'e' ou 'r'.
moedaEextenso = valextenso(valorin, currency)
print('O extenso de {} é:'
      .format(moedaEextenso[0]))
print(moedaEextenso[1])
