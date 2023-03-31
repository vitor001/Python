palpite = 0
numero = 89

while True:  
    palpite = int(input('Tente acertar o numero: '))
    if palpite == numero:  
        print('Parabens, voce acertou!')
        break
    else:
        print('Voce errou, tente novamente')
else:
    print('Erro na aplicação')
