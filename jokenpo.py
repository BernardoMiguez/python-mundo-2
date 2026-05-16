import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jog = int(input('Qual é a sua jogada? '))
if 0 <= jog <= 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=' * 11)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jog]}')
    print('-=' * 11)

if computador == jog:
    print("EMPATE")
elif computador == 0 and jog == 1:
    print("Jogador venceu!")
elif computador == 0 and jog == 2:
    print("Computador venceu!")
elif computador == 1 and jog == 0:
    print("Computador venceu!")
elif jog == 1 and computador == 0:
    print("Jogador venceu!")
elif jog == 2 and computador == 0:
    print("Computador venceu!")
elif jog == 2 and computador == 1:
    print("Jogador venceu!")
elif computador == 2 and jog == 1:
    print("Computador venceu!")
else:
    print("\033[31mJogada inválida!\033[m")
print("-=" * 15)
