import random
lugar = ["esquerda", "direita", "meio"]
computador = random.choice(lugar).strip().capitalize()
jogador = str(input("Digite o nome do jogador: ")).capitalize()
option = str(input("Escolha onde bater o pênalti:"))
if option == computador:
    print("O goleiro defendeu!")
else:
    print(f"O jogador {jogador} marcou o gol!")
