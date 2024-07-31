# Escreva um algoritmo que faça com que o usuário tente adivinhar um número sorteado da Mega-Sena em até três tentativas. O número sorteado estará entre 1 e 30 (e não precisa ser aleatório. Você pode definir o seu valor em uma variável). Enquanto o usuário não acertar o número e ainda restarem tentativas, o programa deve continuar solicitando novos palpites. Ao final, se o usuário tiver acertado, o programa deve parabenizá-lo. Caso contrário, deve informar que ele esgotou suas tentativas.

tentativas = 3
numero_sorteado = 20
palpite = None

print("Adivinhe o número sorteado entre 1 e 30 ")
while (palpite != numero_sorteado and tentativas > 0):
    print(f"Você possui {tentativas} tentativas restantes")
    tentativas -= 1

    palpite = int(input("Digite o seu palpite: "))

if palpite == numero_sorteado:
    print("Parabéns! Você acertou.")
else:
    print(f"Poxa, você perdeu. O número correto era {numero_sorteado}.")
