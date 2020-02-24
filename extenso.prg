/***
* Arquivo: extenso.prg
* Copyright (c) 1990-2010
* John Reilly
* Teste da Função para Tradução de Valor por Extenso
***/

Set confirm on
Clear Screen
Valor := 000000000000000000.00
@ 10,10 Say "Digite um numero:" Get Valor;
Picture "999,999,999,999,999,999.99" valid Valor<>0
Read
VSOR_extenso2 = valextenso(Valor,"r")
? Valor
? VSOR_extenso2

Function valextenso (VSOR_valor, VSOR_prefixo)
   If VSOR_valor = 0  // Avalia o argumento.
      Return ("")
   EndIf
   VSOR_valor = abs(VSOR_valor)  // Estrai valor absoluto.

   *** Declarar Vetores
   DECLARE Unidade[19]
   DECLARE Dezena[10]
   DECLARE Centena[10]
   DECLARE Grupo[7]
   DECLARE ExtGrupo[7]
   DECLARE TerminSing[7]
   DECLARE TerminPlur[7]

   *** Declarar Terminações
   VSOR_prefixo = upper(VSOR_prefixo) // Converte para maiúsculo.
   If VSOR_prefixo="R" // Verifica e define Real, Dólar ou Euro.
      TerminSing[1] = " real"
      TerminPlur[1] = " reais"
   Elseif VSOR_prefixo="U"
      TerminSing[1] = " dolar"
      TerminPlur[1] = " dolares"
   Elseif VSOR_prefixo="E"
      TerminSing[1] = " euro"
      TerminPlur[1] = " euros"
   Else
      TerminSing[1] = " real"  // Usa o Real caso não seja válido.
      TerminPlur[1] = " reais"
   Endif
   TerminSing[2] = " mil"
   TerminPlur[2] = " mil"
   TerminSing[3] = " milhao"
   TerminPlur[3] = " milhoes"
   TerminSing[4] = " bilhao"
   TerminPlur[4] = " bilhoes"
   TerminSing[5] = " trilhao"
   TerminPlur[5] = " trilhoes"
   TerminSing[6] = " quatrilhao"
   TerminPlur[6] = " quatrilhoes"
   TerminSing[7] = " centavo"
   TerminPlur[7] = " centavos"

   *** Grupos de Numerais
   Grupo[1] = ""
   Grupo[2] = ""
   Grupo[3] = ""
   Grupo[4] = ""
   Grupo[5] = ""
   Grupo[6] = ""
   Grupo[7] = ""

   *** Vetores para Extenso dos Grupos
   ExtGrupo[1] = ""
   ExtGrupo[2] = ""
   ExtGrupo[3] = ""
   ExtGrupo[4] = ""
   ExtGrupo[5] = ""
   ExtGrupo[6] = ""
   ExtGrupo[7] = ""

   *** Declarar Nomes dos Dígitos
   Unidade[1] = "um"
   Unidade[2] = "dois"
   Unidade[3] = "tres"
   Unidade[4] = "quatro"
   Unidade[5] = "cinco"
   Unidade[6] = "seis"
   Unidade[7] = "sete"
   Unidade[8] = "oito"
   Unidade[9] = "nove"
   Unidade[10] = ""
   Unidade[11] = "onze"
   Unidade[12] = "doze"
   Unidade[13] = "treze"
   Unidade[14] = "quatorze"
   Unidade[15] = "quinze"
   Unidade[16] = "dezesseis"
   Unidade[17] = "dezessete"
   Unidade[18] = "dezoito"
   Unidade[19] = "dezenove"
   Dezena[1] = "dez"
   Dezena[2] = "vinte"
   Dezena[3] = "trinta"
   Dezena[4] = "quarenta"
   Dezena[5] = "cinquenta"
   Dezena[6] = "sessenta"
   Dezena[7] = "setenta"
   Dezena[8] = "oitenta"
   Dezena[9] = "noventa"
   Dezena[10] = ""
   Centena[1] = "cento"
   Centena[2] = "duzentos"
   Centena[3] = "trezentos"
   Centena[4] = "quatrocentos"
   Centena[5] = "quinhentos"
   Centena[6] = "seiscentos"
   Centena[7] = "setecentos"
   Centena[8] = "oitocentos"
   Centena[9] = "novecentos"
   Centena[10] = ""

   *** Converte VSOR_Valor em string.
   VSOR_StrValor = alltrim(str(int(VSOR_valor)))
   *** Calcula a quantidade de milhares. 
   nMilhares = len(VSOR_StrValor)/3 

   *** Condição com nFracao para completar com 0 à esquerda 
   *** no ultimo milhar caso necessário. Esta tarefa é necessária 
   *** para assegurar a correta separação dos milhares em vetores 
   *** e para facilitar a descrição do ultimo milhar. 
   nFracao = int((nMilhares - int(nMilhares)) * 10) 
   If nMilhares != int(nMilhares) 
      nMilhares = int(nMilhares)+1 
      If nFracao = 3 
         VSOR_StrValor = "00" + VSOR_StrValor 
      Elseif nFracao = 6 
         VSOR_StrValor = "0" + VSOR_StrValor 
      Endif 
   Endif 

   *** Rotina Separa Grupos - Separa os milhares em vetores. 
   For nMilhar = 1 to nMilhares 
      Grupo[nMilhar] = substr(VSOR_StrValor, -(nMilhar * 3), 3) 
   Next 

   *** Rotina Nomeia Milhares - Descrição dos milhares. 
   If VSOR_Valor > int(VSOR_valor)  // Verifica se decimal è > 0. 
      nDecimal = right(str(VSOR_valor),2)  // Centavos p/ Inteiro. 
      Grupo[7] = "0" + nDecimal   // Completa com 0 à esquerda. 
      ExtGrupo[7] = " e "   // Memoriaza conjunção “ e ”. 
   Else 
      Grupo[7] = "000"  // Caso não tenha valor representativo. 
   Endif 

   *** Loop que faz o extenso de cada Grupo. 
   For nMilhar = 0 to nMilhares 
      If nMilhar = 0 // Processa os centavos. 
         If ExtGrupo[7] = " e " 
            nMilhar = 7 
         Else 
            nMilhar = nMilhar + 1  // Para centavos sem valor. 
         Endif 
      Endif 
      nDigito = 1    // Identificará o Dígito a ser nomeado. 
      Do While nDigito < 4 
         nNome = val(substr(Grupo[nMilhar], nDigito, 1)) 
         If nNome = 0 
            nNome = 10 
         Endif 
         Do Case // Caso de cada dig., Centena, Dezena e Unidade. 
            Case nDigito = 1 
               If (nNome = 1; 
                  .and. val(substr(Grupo[nMilhar], 2, 2)) = 0) 
                  ExtGrupo[nMilhar] = "Cem"   // muda Cento p/ Cem. 
                  Exit 
               Elseif (nNome = 1; 
                      .and. val(substr(Grupo[nMilhar], 2, 2)) >0) 
                  ExtGrupo[nMilhar] = ExtGrupo[nMilhar]; 
                  + Centena[nNome] + " e " 
               Elseif nNome > 1 .and. nNome < 10 // Quando >= 200. 
                  ExtGrupo[nMilhar] = ExtGrupo[nMilhar]; 
                  + Centena[nNome] 
                  If  val(substr(Grupo[nMilhar], 2, 2)) > 0 
                      ExtGrupo[nMilhar] = ExtGrupo[nMilhar]; 
                      + " e " 
                  Endif 
               Endif 
            Case nDigito = 2 
               If (nNome > 0 .and. nNome < 10) // Nomes 11 a 19. 
                  nOnzeDezenove = val(right(Grupo[nMilhar],2)) 
                  If (nOnzeDezenove > 10; 
                     .and. nOnzeDezenove < 20) 
                     ExtGrupo[nMilhar] = ExtGrupo[nMilhar]; 
                     + Unidade[nOnzeDezenove] 
                     Exit 
                  Else 
                     ExtGrupo[nMilhar] = ExtGrupo[nMilhar]; 
                     + Dezena[nNome] 
                     If (val(substr(Grupo[nMilhar], 3, 1)) > 0; 
                        .and. nNome > 0) 
                        ExtGrupo[nMilhar] = ExtGrupo[nMilhar]; 
                        + " e " 
                     Endif 
                  Endif 
               Endif 
            Case nDigito = 3 
               ExtGrupo[nMilhar] = ExtGrupo[nMilhar]; 
               + Unidade[nNome] 
         EndCase 
         nDigito = nDigito + 1 
      Enddo 
      If nMilhar = 7 
         nMilhar = 0 
      Endif 
   Next 

   *** Rotina Concatena ExtGrupo. 
   *** Monta o valor por Extenso com todos os grupos e 
   *** as suas terminações. 
   VSOR_extenso = "" 
   nMilhar = 0 
   Do While nMilhar <= nMilhares 
      Do Case 
         Case nMilhar = 0 
            nMilhar = 7 
            If val(Grupo[nMilhar]) = 1 // Define plural ou sing.
               VSOR_extenso = ExtGrupo[nMilhar]; 
               + TerminSing[nMilhar] 
            Elseif val(Grupo[nMilhar]) > 1 
               VSOR_extenso = ExtGrupo[nMilhar]; 
               + TerminPlur[nMilhar] 
            Endif 
            nMilhar = 0 
         Case nMilhar = 1 
            If int(VSOR_valor) = 1  // Prefixos plural e singular. 
               VSOR_extenso = ExtGrupo[nMilhar]; 
               + TerminSing[nMilhar] + VSOR_Extenso 
            Elseif int(VSOR_valor) > 1 
               VSOR_extenso = ExtGrupo[nMilhar]; 
               + TerminPlur[nMilhar] + VSOR_Extenso 
               If Int(VSOR_valor) > 999  // ", " ou " e ". 
                  If (val(Grupo[1]) > 99; 
                     .and. right(Grupo[1],2) <> "00") 
                     VSOR_extenso = ", " + VSOR_Extenso 
                  Elseif (val(Grupo[1]) > 99; 
                         .and. right(Grupo[1],2) = "00") 
                     VSOR_extenso = " e " + VSOR_Extenso 
                  Elseif (val(Grupo[1]) < 100; 
                         .and. val(Grupo[1]) > 0) 
                     VSOR_extenso = " e " + VSOR_Extenso 
                  Endif 
               Endif 
            Else 
               nMilhar = nMilhar + 1  // Se grupo=0 passa próximo. 
               Loop 
            Endif 
         Case nMilhar = 2 
            If val(Grupo[nMilhar]) > 0  // ", " " e " ou " de". 
               VSOR_extenso = ExtGrupo[nMilhar]; 
               + TerminSing[nMilhar] + VSOR_Extenso 
            Elseif val(Grupo[1]) > 0 
               nMilhar = nMilhar + 1   // Se grupo=0 passa próximo. 
               Loop 
            Else 
               VSOR_extenso = " de" + VSOR_Extenso 
               nMilhar = nMilhar + 1  // Se grupo=0 passa próximo. 
               Loop 
            Endif 
            If int(VSOR_valor) > 999999 // Escolhe ", " ou " e " 
               If (val(Grupo[2])>99 .and. right(Grupo[2],2)="00"; 
                  .and. Grupo[1]<>"000") 
                  VSOR_extenso = ", " + VSOR_Extenso 
               Elseif (val(Grupo[nMilhar]) > 99; 
                      .and. right(Grupo[2],2) <> "00") 
                  VSOR_extenso = ", " + VSOR_Extenso 
               Elseif (val(Grupo[nMilhar]) < 100; 
                      .and. val(grupo[nMilhar]) > 0) 
                  VSOR_extenso = " e " + VSOR_Extenso 
               Elseif (val(Grupo[2])>99; 
                      .and. right(Grupo[2],2)="00"; 
                      .and. Grupo[1]="000") 
                  VSOR_extenso = " e " + VSOR_Extenso 
               Endif 
            Endif 
         Case nMilhar >= 3 
            If val(Grupo[nMilhar]) > 1 //Plural e sing. Terminações. 
               VSOR_extenso = ExtGrupo[nMilhar]; 
               + TerminPlur[nMilhar] + VSOR_extenso 
            Elseif val(Grupo[nMilhar]) = 1 
               VSOR_extenso = ExtGrupo[nMilhar]; 
               + TerminSing[nMilhar] + VSOR_extenso 
            Else 
               nMilhar = nMilhar + 1  // Se grupo=0 passa próximo. 
               Loop
            Endif
            If (int(VSOR_valor) > 999 * nMilhar
               .and. nMilhar < nMilhares)
               If val(Grupo[nMilhar]) > 99 //", " ou " e " entre.
                  VSOR_extenso = ", " + VSOR_Extenso
               Elseif (val(Grupo[nMilhar]) < 100;
                      .and. val(Grupo[nMilhar]) > 0)
                  VSOR_extenso = " e " + VSOR_Extenso
               Endif
            Endif
      EndCase
      nMilhar = nMilhar + 1
   Enddo
Return (VSOR_extenso)
