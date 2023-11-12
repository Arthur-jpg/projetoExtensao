import numpy as np
from rentabilidade import carteiraPublica
from privados import cdb1

def betaPublico():
    rent1 = carteiraPublica()
    rent1 = rent1[0]

    rent2 = carteiraPublica()
    rent2 = rent2[1]

    pAt1 = carteiraPublica()
    pAt1 = pAt1[4]

    pAt2 = carteiraPublica()
    pAt2 = pAt2[5]

    Cdi = cdb1()
    rentCDI = Cdi[4]

    varCDI = (Cdi[2])**2

    beta = (np.cov(rent1, rentCDI)*pAt1 + np.cov(rent2, rentCDI)*pAt2)/varCDI

    print(rentCDI)
    print(beta)


betaPublico()