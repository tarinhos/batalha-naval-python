import random

def criar_tabuleiro():
    # Cria um tabuleiro 5x5 com posições não atacadas
    return [["~"] * 5 for _ in range(5)]


def posicionar_navios():
    # Posiciona 3 navios em locais aleatórios sem repetir posição
    navios = []
    while len(navios) < 3:
        posicao = (random.randint(0, 4), random.randint(0, 4))
        if posicao not in navios:
            navios.append(posicao)
    return navios


def mostrar_tabuleiro(tabuleiro):
    # Exibe o tabuleiro atual para o jogador
    for linha in tabuleiro:
        print(" ".join(linha))


def jogo_batalha_naval():
    # Inicialização do jogo
    tabuleiro = criar_tabuleiro()
    navios = posicionar_navios()

    print("=== JOGO DE BATALHA NAVAL ===")

    # Loop principal do jogo: continua enquanto houver navios
    while navios:
        mostrar_tabuleiro(tabuleiro)

        try:
            linha = int(input("Linha (0 a 4): "))
            coluna = int(input("Coluna (0 a 4): "))
        except ValueError:
            print("Digite apenas números.")
            continue

        # Validação da posição escolhida
        if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
            print("Posição inválida!")
            continue

        # Verifica se a posição já foi atacada
        if tabuleiro[linha][coluna] != "~":
            print("Você já atacou essa posição!")
            continue

        # Verificação de acerto ou erro
        if (linha, coluna) in navios:
            print("Acertou um navio!")
            tabuleiro[linha][coluna] = "X"
            navios.remove((linha, coluna))
        else:
            print("Água!")
            tabuleiro[linha][coluna] = "O"

    # Condição de vitória
    print("Parabéns! Você venceu o jogo!")


if __name__ == "__main__":
    jogo_batalha_naval()
