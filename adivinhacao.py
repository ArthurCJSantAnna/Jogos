def jogar():
    import random

    print("Bem vindo ao jogo de Adivinhação")

    numero_secreto = random.randrange(1,101) # 0.0 e 1.0
    total_de_tentativas = 0
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Qual o nível de dificuldade? "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    rodada = 1

    for rodada in range (1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")

        chute_str = input("Digite o seu número entre 1 e 100: ")

        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute

        maior = chute > numero_secreto


        print("Você digitou ", chute)

        if (acertou):
            print(f"você Acertou e fez {pontos} pontos!")
            break
        else:
            if(maior):
                print("Você Errou. O seu chute foi maior que o número secreto")
            else:
                print("Você Errou. O seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



    print("Fim do Jogo")
if(__name__ == "__main__"):
    jogar()

