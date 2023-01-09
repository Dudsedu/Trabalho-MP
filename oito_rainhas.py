def verifica():
    flag = True
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna] == '1':
                if tabuleiro[linha].count('1') > 1: #################### Verifica posições horizontais.
                    flag = False
                for linha1 in range(8): ################################ Verifica posições verticais.
                    if linha1 != linha:                 
                        if tabuleiro[linha1][coluna] == '1':
                            flag = False
                        diferenca = abs(linha-linha1) ################## Verifica diagonais.
                        if coluna-diferenca >= 0:
                            if tabuleiro[linha1][coluna-diferenca] == '1':
                                flag = False
                        if coluna+diferenca <= 7:
                            if tabuleiro[linha1][coluna+diferenca] == '1':
                                flag = False
    if flag is True:
        return 1
    else:
        return 0

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