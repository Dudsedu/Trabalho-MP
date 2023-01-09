def verifica():
    pass

def monta(tabuleiro):
    rainhas = 0
    if len(tabuleiro) != 8:
        return -1
    if len(tabuleiro) == 8:
        for linha in range(8):
            for coluna in range(8):
                if tabuleiro[linha][coluna] == '1':
                    rainhas += 1
                if tabuleiro[linha][coluna] != '1' and tabuleiro[linha][coluna] != '0':
                    return -1
        if rainhas == 8 and len(tabuleiro) == 8:
            return verifica(tabuleiro)
        if rainhas != 8:
            return -1