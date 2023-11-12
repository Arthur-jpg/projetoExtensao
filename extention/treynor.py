from beta import betaTotal
from rentabilidade import rentabilidadeGeral
from privados import cdb1

def treynor():
    beta = betaTotal()
    rentabilidadeCarteira = rentabilidadeGeral()
    rentabilidadeCarteira = rentabilidadeCarteira[0]
    taxaLivreRisco = cdb1()
    taxaLivreRisco = taxaLivreRisco[0]

    treynorr = (rentabilidadeCarteira - taxaLivreRisco)/beta

    print(treynorr)
    return treynorr

treynor()