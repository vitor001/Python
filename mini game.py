palpite = 0
numero = 89

while True:  # executando o while antes da verificação como se fosse um do while
    palpite = int(input('Tente acertar o numero: '))
    if palpite == numero:  # verificação do código
        print('Parabens, voce acertou!')
        break
    else:
        print('Voce errou, tente novamente')
else:
    print('Erro na aplicação')
