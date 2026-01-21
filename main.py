import random

def criar_tabuleiro():
    return [["~"] * 5 for _ in range(5)]


def posicionar_navios():
    navios = []
    while len(navios) < 3:
        posicao = (random.randint(0, 4), random.randint(0, 4))
        if posicao not in navios:
            navios.append(posicao)
    return navios


def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))


def jogo_batalha_naval():
    tabuleiro = criar_tabuleiro()
    navios = posicionar_navios()

    print("=== JOGO DE BATALHA NAVAL ===")

    while navios:
        mostrar_tabuleiro(tabuleiro)

        try:
            linha = int(input("Linha (0 a 4): "))
            coluna = int(input("Coluna (0 a 4): "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
            print("Posição inválida!")
            continue

        if tabuleiro[linha][coluna] != "~":
            print("Você já atacou essa posição!")
            continue

        if (linha, coluna) in navios:
            print("Acertou um navio!")
            tabuleiro[linha][coluna] = "X"
            navios.remove((linha, coluna))
        else:
            print("Água!")
            tabuleiro[linha][coluna] = "O"

    print("Parabéns! Você venceu o jogo!")


if __name__ == "__main__":
    jogo_batalha_naval()
