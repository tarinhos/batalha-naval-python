# Batalha Naval – Lógica do Jogo

## Descrição
O objetivo do projeto é demonstrar a lógica por trás do funcionamento do jogo Batalha Naval, utilizando Python e programação estruturada.

## Lógica do Jogo

### 1. Criação do tabuleiro
O tabuleiro é representado por uma matriz 5x5, inicialmente preenchida com "~", indicando posições ainda não atacadas.

### 2. Posicionamento dos navios
Os navios são posicionados aleatoriamente no tabuleiro, garantindo que não ocupem a mesma posição.

### 3. Loop principal do jogo
O jogo funciona em um laço de repetição que continua enquanto existirem navios não destruídos.

### 4. Entrada do jogador
O jogador informa a linha e a coluna para realizar um ataque.

### 5. Validação das jogadas
O sistema verifica:
- Se a posição está dentro do tabuleiro
- Se a posição já foi atacada anteriormente

### 6. Verificação de acerto
- Se a posição contém um navio, ele é marcado como destruído
- Caso contrário, a jogada é considerada água

### 7. Condição de vitória
O jogo termina quando todos os navios forem destruídos.
