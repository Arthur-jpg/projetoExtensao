import pandas as pd
import statistics
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


# o endereço do arquivo principal dos dados coletados foi posto dentro de uma vriaval
arquivo = 'dadoscertos.csv'

# o pandas está lendo o arquivo .csv para o programa poder analisar os dados
planilha = pd.read_csv(arquivo, sep=';')

# foi criado uma função para cada um dos 5 ativos privados selecionados mais o índice principal do mercado
# para que os devidos dados fossem coletados e tratados, todas as funções possuem a mesma estrutura
def ibov():
    # foi guardado a serie de dados do ibovespa em uma variável para posteriormente tratarmos esses dados
    # além disso, foi necessário substituir as ',' com '.' para ser possível tratar os dados
    ibov = planilha['IBOV'].str.replace(',', '.')
    
    # para poder tratar os dados como números, foram transformados em float
    ibov = ibov.astype(float)

    # usando a biblioteca statistics, foi calculado a média dos dados 
    media = statistics.mean(ibov)

    # usando a biblioteca statistics, foi calculado o desvio padrão amostral dos dados
    desvPad = statistics.stdev(ibov)

    # foi calculado o coeficiente de variação com a formula que foi ensidada
    coefVar = desvPad/media

    #  todos os dados calculados foram exportados com o 'return' para poderem ser usados em outras funções
    return media, coefVar, desvPad, ibov




def cdb1():
    cdb = planilha['CDB'].str.replace(',', '.')
    cdb = cdb.astype(float)
    media = statistics.mean(cdb)
    desvPad = statistics.stdev(cdb)
    coefVar = desvPad/media
    return media, coefVar, desvPad, cdb




def petr36():
    petr36 = planilha['PETR36'].str.replace(',', '.')
    petr36 = petr36.astype(float)
    media = statistics.mean(petr36)
    desvPad = statistics.stdev(petr36)
    coefVar = desvPad/media
    return media, coefVar, desvPad, petr36

def Cpld26():
    Cpld26 = planilha['CPLD26'].str.replace(',', '.')
    Cpld26 = Cpld26.astype(float)
    media = statistics.mean(Cpld26)
    desvPad = statistics.stdev(Cpld26)
    coefVar = desvPad/media
    return media, coefVar, desvPad, Cpld26


def Taee26():
    Taee26 = planilha['TAEE26'].str.replace(',', '.')
    Taee26 = Taee26.astype(float)
    media = statistics.mean(Taee26)
    desvPad = statistics.stdev(Taee26)
    coefVar = desvPad/media
    return media, coefVar, desvPad, Taee26

def Itsa24():
    Itsa24 = planilha['ITSA24'].str.replace(',', '.')
    Itsa24 = Itsa24.astype(float)
    media = statistics.mean(Itsa24)
    desvPad = statistics.stdev(Itsa24)
    coefVar = desvPad/media
    return media, coefVar, desvPad, Itsa24

# a função contaMenores() foi usada para localizar os dois menores coeficientes de variação entre os ativos selecionados
def contaMenores():
    
    # foi criado uma lista para que para guardar os coeficientes de cada um dos ativos
    coeficientes = []

    # foi criado variaveis para guardar cada coeficiente de variação de cada ativo
    # como o segundo item exportado das funções foram os coeficientes de variação foi usado o index [1] para ter acesso a esse dado
    Citsa24 = Itsa24()[1]
    Ctaee26 = Taee26()[1]
    Ccpld26 = Cpld26()[1]
    Cpetr3 = petr36()[1]
    Ccdb = cdb1()[1]

    # para inserir os valores dentro da lista foi usada a função append
    coeficientes.append(Citsa24)
    coeficientes.append(Ctaee26)
    coeficientes.append(Ccpld26)
    coeficientes.append(Cpetr3)
    coeficientes.append(Ccdb)

    # para achar o menor coeficiente de variação foi usado a função min que procura dentro da lista o menor valor
    menor = min(coeficientes)

    # para achar o segundo menor valor foi usado a função min, porém utilizando um diferencial dentro para que fosse achado
    # o menor coeficinete de variação que fosse diferente do menor de todos
    segundoMenor = min(n for n in coeficientes if n != menor)

    # para que os dados de menor e segundo menor coeficientes fossem usados, eles foram exportados com o 'return'
    return menor, segundoMenor




# para ter acesso ao nome e a função dos menores coeficientes foi feita a função escolherMenor()
def escolherMenor():
    # para ter acesso ao dados de menores coeficientes foi usado o index [0] para o menor e [1] para o maior
    # uma vez que foram exportados dessa maneira na função contaMenores()
    menor = contaMenores()[0]
    segundoMenor = contaMenores()[1]


    # foi criado um dicionário com o valor dos coeficientes de variação como chaves, e a função e o nome do ativo como valores das chaves
    dic = {
    Itsa24()[1] :[Itsa24(),'Itsa24'],
    Taee26()[1] : [Taee26(), 'Taee26'],
    Cpld26()[1] : [Cpld26(), 'Cpld26'],
    petr36()[1] : [petr36(), 'Petr36'],
    cdb1()[1] : [cdb1(), 'Cdb']
    }


    # assim foi possível que novas variáveis fossem criadas para guardar os valores dos nomes e das funções dos dois menores coeficientes

    # a variavel m e n foram 
    m = dic[menor][0]
    sm = dic[segundoMenor][0]

    nome1 = dic[menor][1]
    nome2 = dic[segundoMenor][1]


    return m, sm, nome1, nome2




def dadosSharp():

    ativo1 = escolherMenor()[0]
    ativo2 = escolherMenor()[1]

    mediaativo1 = ativo1[0]
    mediaativo2 = ativo2[0]

    

    desvPadativo1 = ativo1[2]
    desvPadativo2 = ativo2[2]

    varativo1 = desvPadativo1**2
    varativo2 = desvPadativo2**2

    correl = stats.pearsonr(ativo1[3], ativo2[3])
    correl = correl[0]
    
    covar = desvPadativo1*desvPadativo2*correl
    

    reff = ativo1[0]
    
    return mediaativo1, mediaativo2, desvPadativo1, desvPadativo2, varativo1, varativo2, correl, covar, reff

