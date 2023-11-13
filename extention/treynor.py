# foram importadas funções para obter as informações necessárias para rodar o código
from beta import betaTotal
from rentabilidade import rentabilidadeGeral
from privados import cdb1


# foi criada uma função para poder exportar o dado gerado para outras funções
def treynor():
    # foram criadas variáveis com os dados necessários para o programa
    beta = betaTotal()
    rentabilidadeCarteira = rentabilidadeGeral()
    rentabilidadeCarteira = rentabilidadeCarteira[0]
    taxaLivreRisco = cdb1()
    taxaLivreRisco = taxaLivreRisco[4]

    # foram utilizadas as variáveis criadas para fazer o cálculo do índice 
    treynorr = (rentabilidadeCarteira - taxaLivreRisco)/beta

    # o índice foi exportado da função com o 'return'
    return treynorr