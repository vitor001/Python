'''
# a senha precisa de:
# maiuscilas e minusculas
# simbolos e espaços

# a senha terá uma base chave, por exemplo:
# Security = base
# 5ecur1ty = senha
'''
chave = input('Digite a base da sua senha: ')

senha = ''

for letra in chave:
    if letra in "Aa":  # onde houver a letra 'Aa' na chave ocorrerá a substituição da letra por '3'
        senha += '3'
    elif letra in "Dd":
        senha += '7'
    elif letra in "Ss":
        senha += '2'
    elif letra in "Vv":
        senha += 'ç'
    elif letra in "Oo":
        senha += '6'
    else:
        senha += letra

print(senha)
