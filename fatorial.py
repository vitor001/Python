num = int(input('Digite o numero que voce quer saber o fatorial: '))
fatorial = 1

if num < 0:
    print('Nao existe fatorial de numero negativo')
elif num == 0:
    print(f'O fatorial de {num} eh 1')
else:
    for x in range(1, num + 1):
        fatorial *= x  # mesma coisa que "fatorial = fatorial * x"
    print(f'O valor do fatorial de {num} é: {fatorial}')
