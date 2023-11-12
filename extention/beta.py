import numpy as np
from rentabilidade import carteiraPublica
from rentabilidade import carteiraPrivada
from privados import cdb1
from publicos import escolherMenorp
from privados import escolherMenor

def betaPublico():
    rent1 = escolherMenorp()
    rent1 = rent1[0]
    rent1 = rent1[3]

    rent2 = escolherMenorp()
    rent2 = rent2[1]
    rent2 = rent2[3]

    pAt1 = carteiraPublica()
    pAt1 = pAt1[4]

    pAt2 = carteiraPublica()
    pAt2 = pAt2[5]

    Cdi = cdb1()
    rentCDI = Cdi[3]

    varCDI = (Cdi[2])**2

    beta = (np.cov(rent1, rentCDI)*pAt1 + np.cov(rent2, rentCDI)*pAt2)/varCDI

    beta = beta[0][1]
    return beta

def betaPrivado():
    rent1 = escolherMenor()
    rent1 = rent1[0]
    rent1 = rent1[3]

    rent2 = escolherMenor()
    rent2 = rent2[1]
    rent2 = rent2[3]

    pAt1 = carteiraPrivada()
    pAt1 = pAt1[4]

    pAt2 = carteiraPrivada()
    pAt2 = pAt2[5]

    Cdi = cdb1()
    rentCDI = Cdi[3]

    varCDI = (Cdi[2])**2

    beta = (np.cov(rent1, rentCDI)*pAt1 + np.cov(rent2, rentCDI)*pAt2)/varCDI
    beta2 = beta[0][1]
    return beta2

def betaTotal():
    beta1 = betaPublico()

    beta2 = betaPrivado()

    betaTotal = (beta1 + beta2)/2
    return betaTotal

betaTotal()
betaPrivado()
betaPublico()