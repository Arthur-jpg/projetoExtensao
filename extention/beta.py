# foi importado a biblioteca numpy para poder fazer a conta de covariância
import numpy as np
# foram importadas as funções de outros arquivos .py que são necessárias para rodar o programa
from rentabilidade import carteiraPublica
from rentabilidade import carteiraPrivada
from privados import cdb1
from publicos import escolherMenorp
from privados import escolherMenor

def betaPublico():
    # para acessar a rentabilidade do primeiro ativo público foi usada a função escolherMenorp() que retorna o valor desejado
    rent1 = escolherMenorp()
    rent1 = rent1[0]
    rent1 = rent1[3]

    # para acessar a rentabilidade do segundo ativo público foi usada a função escolherMenorp() que retorna o valor desejado
    rent2 = escolherMenorp()
    rent2 = rent2[1]
    rent2 = rent2[3]

    # para acessar a porcentagem do primeiro ativo público foi usada a função carteiraPublica() que retorna o valor desejado 
    pAt1 = carteiraPublica()
    pAt1 = pAt1[4]

    # para acessar a porcentagem do segundo ativo público foi usada a função carteiraPublica() que retorna o valor desejado 
    pAt2 = carteiraPublica()
    pAt2 = pAt2[5]

    # para acessar a taxa livre de risco foi usado a função cdb1() que replica o cdi  
    Cdi = cdb1()
    rentCDI = Cdi[3]

    # para acessar a variância da taxa livre de risco foi usada a mesma função cdb1() porém com outro index para acessar a informação desejada
    varCDI = (Cdi[2])**2

    # foi calculado o beta de acordo com a formula geral do índice e com as variáveis que foram criadas com dados importado anteriormente
    beta = (np.cov(rent1, rentCDI)*pAt1 + np.cov(rent2, rentCDI)*pAt2)/varCDI

    # para exportar o beta foi usado index para acessar a iformação deseja gerada pelo calculo acima
    beta = beta[0][1]

    # o beta público foi exportado com o return para poder ser usado em outras funções
    return beta

def betaPrivado():
    # para acessar a rentabilidade do primeiro ativo privado foi usada a função escolherMenor() que retorna o valor desejado
    rent1 = escolherMenor()
    rent1 = rent1[0]
    rent1 = rent1[3]

    # para acessar a rentabilidade do segundo ativo privado foi usada a função escolherMenor() que retorna o valor desejado
    rent2 = escolherMenor()
    rent2 = rent2[1]
    rent2 = rent2[3]

    # para acessar a porcentagem do primeiro ativo privado foi usada a função carteiraPrivada() que retorna o valor desejado
    pAt1 = carteiraPrivada()
    pAt1 = pAt1[4]

    # para acessar a porcentagem do segundo ativo privado foi usada a função carteiraPrivada() que retorna o valor desejado
    pAt2 = carteiraPrivada()
    pAt2 = pAt2[5]

    # para acessar a taxa livre de risco foi usado a função cdb1() que replica o cdi 
    Cdi = cdb1()
    rentCDI = Cdi[3]

    # para acessar a variância da taxa livre de risco foi usada a mesma função cdb1() porém com outro index para acessar a informação desejada
    varCDI = (Cdi[2])**2


    # foi calculado o beta de acordo com a formula geral do índice e com as variáveis que foram criadas com dados importado anteriormente
    beta = (np.cov(rent1, rentCDI)*pAt1 + np.cov(rent2, rentCDI)*pAt2)/varCDI

    # para exportar o beta foi usado index para acessar a iformação deseja gerada pelo calculo acima
    beta2 = beta[0][1]

    # o beta privado foi exportado com o return para poder ser usado em outras funções
    return beta2

def betaTotal():
    # para ter acesso ao beta público foi usado a função betaPublico() que retorna o valor desejado
    beta1 = betaPublico()

    # para ter acesso ao beta privado foi usado a função betaPrivado() que retorna o valor desejado
    beta2 = betaPrivado()

    # para calcular o beta total da carteira foi feita a média entre os dois betas
    betaTotal = (beta1 + beta2)/2

    # para utilizar o valor do beta total da carteira em outras funções ele foi exportado com 'return'
    return betaTotal

