from publicos import escolherMenorp
from privados import escolherMenor
from sharpe import variaveis

aloca = variaveis()

def carteiraPrivada():
    ativo1 = escolherMenor()[0]
    ativo2 = escolherMenor()[1]

    rdiario1 =  ativo1[3]
    rdiario2 = ativo2[3]

    ativo1 = ativo1
    ativo2 = ativo2

    rentabilidade1 = ativo1[4]
    rentabilidade2 = ativo2[4]

    pAt1 = aloca[0]
    pAt2 = aloca[1]

    rentabilidadeG1 = rentabilidade1*pAt1 + rentabilidade2*pAt2 

    rendimentoDiario = rdiario1*pAt1 + rdiario2*pAt2

    return rentabilidade1, rentabilidade2, rentabilidadeG1, rendimentoDiario


def carteiraPublica():
    ativo10 = escolherMenorp()[0]
    ativo20 = escolherMenorp()[1]

    ativo1 = ativo10
    ativo2 = ativo20

    rdiario1 =  ativo1[3]
    rdiario2 = ativo2[3]

    rentabilidade1 = ativo1[4]
    rentabilidade2 = ativo2[4]

    pAt1 = aloca[2]
    pAt2 = aloca[3]
    
    
    rendimentoDiario = rdiario1*pAt1 + rdiario2*pAt2
    rentabilidadeG2 = rentabilidade1*pAt1 + rentabilidade2*pAt2

    return rentabilidade1, rentabilidade2, rentabilidadeG2, rendimentoDiario



def rentabilidadeGeral():
    rentPublica = carteiraPublica()[2]
    rentPrivada = carteiraPrivada()[2]

    rendimentoDiarioPublico = carteiraPublica()[3]
    rendimentoDiarioPrivado = carteiraPrivada()[3]

    rendimentoDiarioPrivado = rendimentoDiarioPrivado
    rendimentoDiarioPublico = rendimentoDiarioPublico

    rendimentoToalDiário = (rendimentoDiarioPrivado + rendimentoDiarioPublico) / 2

    geral = (rentPublica+rentPrivada)/2



    # print(f'Rentabilidade Carteira Privada {round(carteiraPrivada()[2]*100, 2)}%')
    # print(f'Rentabilidade Carteira Pública {round(carteiraPublica()[2]*100,2)}%')
    # print(f'Rentabilidade geral da Carteira {round(geral*100, 2)}%')

    return geral, rendimentoDiarioPublico, rendimentoDiarioPrivado, rendimentoToalDiário

