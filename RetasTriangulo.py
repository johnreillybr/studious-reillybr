r1 = float(input('Comprimento da 1ª reta: '))
r2 = float(input('Comprimento da 2ª reta: '))
r3 = float(input('Comprimento da 3ª reta: '))
maior = max(r1, r2, r3)
menor = min(r1, r2, r3)
meio = (r1 + r2 + r3) - maior - menor
print('\033[7;32mA reta maior mede {:.1f}cm.\033[m'
      '\n\033[7;32mA reta menor mede {:.1f}cm.\033[m'
      '\n\033[7;32mA reta com medida entre a maior e a menor mede {:.1f}cm.\033[m'
      .format(maior, menor, meio))
print('\033[7;30m┌' + '─' * 44 + '┐\033[m')
if maior < meio + menor:
    print('\033[7;30m│ Essas retas podem formar um tríângulo!     │\033[m')
else:
    print('\033[7;30m│ Essas retas NÃO podem formar um tríângulo! │\033[m')
print('\033[7;30m└' + '─' * 44 + '┘\033[m')
