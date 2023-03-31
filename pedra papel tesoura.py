from random import choice
vit_jog = 0
vit_maq = 0

def Esc_jog():
  jogada = input("escolha Pedra, Papel ou Tesoura: ")
  print('-'*30)
  jogada.lower()
  print('jogada do jogador: ', jogada)
  if jogada == 'pedra':
    return jogada
  elif jogada == 'papel':
    return jogada
  elif jogada == 'tesoura':
    return jogada
  else:
    print('Digite novamente')
    print('--'*20)
    Esc_jog() 


def Esc_maq():
  jogada = choice(['pedra', 'papel', 'tesoura'])
  print('jogada da maquina: ', jogada)
  return jogada


while True:
  jogador = Esc_jog()
  maquina = Esc_maq()
  print('-'*30)
  if jogador == 'pedra' and maquina == 'tesoura' or jogador == 'papel' and maquina == 'pedra' or jogador == 'tesoura' and maquina == 'papel':
    vit_jog += 1
    print('Parabens, voce ganhou.')
    print('-'*30)
    print('Vitorias do jogador: ', vit_jog)
    print('Vitorias da maquina: ', vit_maq)
  elif jogador == maquina:
    print('Empate!')
    print('-'*30)
    print('Vitorias do jogador: ', vit_jog)
    print('Vitorias da maquina: ', vit_maq)
  else:
    vit_maq +=1
    print('Voce Perdeu.')
    print('-'*30)
    print('Vitorias do jogador: ', vit_jog)
    print('Vitorias da maquina: ', vit_maq)

  jog_nov = input('Voce quer jogar novamente? (s) ou (n): ')
  print('-'*30)
  if jog_nov == 's':
    pass
  elif jog_nov == 'n':
    print('Fim de jogo')
    if vit_jog > vit_maq:
      print("ganhador: Jogador")
    elif vit_jog < vit_maq:
      print("ganhador: Maquina")
    else:
      print('Nao houve ganhador')
    break
  else:
    print('Fim de jogo')
    if vit_jog > vit_maq:
      print("ganhador: Jogador")
    elif vit_jog < vit_maq:
      print("ganhador: Maquina")
    else:
      print('Nao houve ganhador')
    break
