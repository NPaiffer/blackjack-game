import random

valores_cartas = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def criar_baralho():
    baralho = []
    for naipe in ['Copas', 'Espadas', 'Ouros', 'Paus']:
        for carta in valores_cartas.keys():
            baralho.append((carta, naipe))
        random.shuffle(baralho)
        return baralho
    
def calcular_pontuacao(mao):
    pontuacao = 0
    ases = 0
    for carta, naipe in mao:
        pontuacao += valores_cartas[carta]
        if carta == 'A':
            ases += 1

    while pontuacao > 21 and ases:
        pontuacao -= 10
        ases -= 1
    return pontuacao

def mostrar_maos(jogador, dealer, esconder_carta_do_dealer=True):
    print("\nMão do Dealer:")
    if esconder_carta_do_dealer:
        print("<Carta oculta>", dealer[1])
    else:
        print(*dealer, sep=', ')
    print("Pontuação do Dealer:", calcular_pontuacao(dealer) if not esconder_carta_do_dealer else "?")

    print("\nSua Mão:")
    print(*jogador, sep=', ')
    print("Sua Pontuação:", calcular_pontuacao(jogador))

def jogar_blackjack():
    print("Bem-vindo ao Blackjack!")

    baralho = criar_baralho()

    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_dealer = [baralho.pop(), baralho.pop()]