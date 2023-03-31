# descobrir se o numero é primo
print(30 * '-')

num = int(input('Digite um numero: '))

if num > 1:
    for x in range(2, num):
        if num % x == 0:
            print('Esse numero nao eh primo.')
            break
        else:
            print('Esse numero eh primo.')
            break
else:
    print('Esse numero nao eh primo: numero menor ou igual a 1.')
