import oito_rainhas
import pytest
# Caso exista alguma posição de ataque o programa irá retornar 1, caso seja uma solução ao problema das 8 rainhas irá retornar 0, e caso não seja uma entrada válida ao teste o retorno será igual a -1
# Em suma:
# 0 = Não é solução para o problema das 8 rainhas
# 1 = É solução para o problema das 8 rainhas
# -1 = Entrada inválida, ou seja, tabuleiro não é 8x8, possui valores diferentes de 0 e 1, não possui 8 rainhas.

tabuleiro = '00001000','01000000','00010000','00000010','00100000','00000001','00000100','10000000'

def teste():
    assert oito_rainhas.monta(tabuleiro) == 1 # TABULEIRO COM SOLUÇÃO

tabuleiro1 = '00000100','01000000','00010000','00000010','00100000','00000001','00000100','10000000'

def teste1():
    assert oito_rainhas.monta(tabuleiro1) == 0 # TABULEIRO SEM SOLUÇÃO

tabuleiro2 = '00100100','01000000','00010000','00000010','00100000','00000001','00000100','10000000'

def teste2():
    assert oito_rainhas.monta(tabuleiro2) == -1 # TABULEIRO COM MAIS DE 8 RAINHAS

tabuleiro3 = '00000100','01000000','00010000','00000010','00100000','00000001','00000100'

def teste3():
    assert oito_rainhas.monta(tabuleiro3) == -1 # TABULEIRO NÃO É 8X8

tabuleiro4 = '00000500','05000000','00010600','00040010','00100000','00000001','00000200'

def teste4():
    assert oito_rainhas.monta(tabuleiro4) == -1 # TABULEIRO POSSUI VALORES DIFERENTES DE 0 E 1"