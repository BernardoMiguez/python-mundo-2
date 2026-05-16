nome = str(input("Nome do jogador: "))
overall = int(input("Overall do jogador: "))
idade = int(input("Idade do jogador: "))
preco = float(input("Digite o preço do jogador em milhões: "))
if overall >= 85 and idade <= 25:
    print(f"O jogador {nome} é prioridade máxima! Tente contratá-lo o quanto antes! ")
elif 75 <= overall < 85 and preco < 30:
    print(f"O jogador {nome} é uma boa opção para compor o elenco.")
elif overall > 80 and idade > 33:
    print("Esta é uma ótima opção, porém tome cuidado com a condição física")
else:
    print(f"O olheiro recomenda: o jogador {nome} não é uma boa opção para este time, procure por outro jogador.")
