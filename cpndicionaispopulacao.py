cidade1 = input('Digite o nome da primeira cidade: ')
cidade2 = input('Digite o nome da segunda cidade: ')

hab1 = input(f'Digite a populaçao de {cidade1}:  ')
hab2 = input(f'Digite a populaçao de {cidade2}:  ')

if hab1 > hab2:
    print(f'A populaçao de {cidade1}, com {hab1} habitantes e maior que a populaçao de {cidade2}, com {hab2} habitantes.')
elif hab1 < hab2:
    print(f'A populaçao de {cidade2}, com {hab2} habitantes e maior que a populaçao de {cidade1}, com {hab1} habitantes.')

