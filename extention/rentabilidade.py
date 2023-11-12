from publicos import escolherMenorp
from privados import escolherMenor
from sharpe import main

def carteiraPrivada():
    ativo1 = escolherMenor()[0]
    ativo2 = escolherMenor()[1]

    rentabilidade1 = ativo1[4]
    rentabilidade2 = ativo2[4]

    pAt1 = main()[0]
    pAt2 = main()[1]

    rentabilidadeG1 = rentabilidade1*pAt1 + rentabilidade2*pAt2 

    return rentabilidade1, rentabilidade2, rentabilidadeG1


def carteiraPublica():
    ativo1 = escolherMenorp()[0]
    ativo2 = escolherMenorp()[1]

    rentabilidade1 = ativo1[4]
    rentabilidade2 = ativo2[4]

    pAt1 = main()[2]
    pAt2 = main()[3]

    rentabilidadeG2 = rentabilidade1*pAt1 + rentabilidade2*pAt2

    return rentabilidade1, rentabilidade2, rentabilidadeG2



def rentabilidadeGeral():
    rentPublica = carteiraPublica()[2]
    rentPrivada = carteiraPrivada()[2]

    geral = (rentPublica+rentPrivada)/2

    print(geral)

rentabilidadeGeral()