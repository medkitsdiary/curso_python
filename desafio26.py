frase = str(input('Digite uma frase: ')).upper().strip()
print('a letra A aparece {} na frase.'.format(frase.count('A')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('a ultima letra A aparece na posição {}.'.format(frase.rfind('A')))
