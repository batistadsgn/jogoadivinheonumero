print("*********************************")
print("bem vindos ao jogo da adivinhação")
print("*********************************")

numero_secreto = 43
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas +1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 100:")
    print("Você Digitou", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("você deve digitar um numero entre 1 e 100!")
        continue

    acertou     = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if(acertou):
        print("parabens você acertou")
        break
    else:
        if(chute_maior):
            print("Seu chute foi maior que o numero secreto")
        if(chute_menor):
            print("Seu chute foi menor que o numero secreto")

print("Fim do jogo")