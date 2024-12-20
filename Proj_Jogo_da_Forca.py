import random

def main():
    palavras = ["python", "programacao", "desenvolvimento", "tecnologia"]
    palavraSelecionada = random.choice(palavras)
    palavra_escondida = '_' * len(palavraSelecionada)
    tentativas = 5

    print("Bem-vindo ao jogo da forca!")
    print(f"Você tem {tentativas} chances de acertar a palavra: {palavra_escondida}")

    while tentativas > 0:
        letra = input("Escolha uma letra: ")

        if letra in palavraSelecionada:
            nova_palavra_escondida = ''
            for i in range(len(palavraSelecionada)):
                if palavraSelecionada[i] == letra:
                    nova_palavra_escondida += letra
                else:
                    nova_palavra_escondida += palavra_escondida[i]
            palavra_escondida = nova_palavra_escondida
            print(f"A letra '{letra}' está na palavra!")
        else:
            tentativas -= 1
            print(f"A letra '{letra}' não está na palavra escondida. Você ainda tem {tentativas} tentativas.")

        #Mostra a palavra coma letra certa
        print(f"Palavra: {palavra_escondida}")

        #Verifica se acertou a palavra
        if '_' not in palavra_escondida:
            print(f"Parabéns! Você acertou a palavra era: {palavraSelecionada}")
            break

    #Fim de jogo
    if tentativas == 0:
        print(f"Você perdeu! A palavra era: {palavraSelecionada}")

if __name__ == "__main__":
    main()