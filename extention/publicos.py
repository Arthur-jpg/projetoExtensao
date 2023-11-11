import pandas as pd
import statistics
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from privados import cdb1

arquivo = 'dadoscertos.csv'

planilha = pd.read_csv(arquivo, sep=';')


def Selic2026():
    Selic2026 = planilha['Selic2026'].str.replace(',', '.')

    Selic2026 = Selic2026.astype(float)
    
    media = statistics.mean(Selic2026)
    desvPad = statistics.stdev(Selic2026)
    coefVar = desvPad/media
    

    return media, coefVar, desvPad, Selic2026







def Selic2028():
    Selic2028 = planilha['Selic2028'].str.replace(',', '.')
    Selic2028 = Selic2028.astype(float)
    media = statistics.mean(Selic2028)
    desvPad = statistics.stdev(Selic2028)
    coefVar = desvPad/media 
    return media, coefVar, desvPad, Selic2028



def Pre2024Primeiro():
    Pre2024Primeiro = planilha['Pre2024Primeiro'].str.replace(',', '.')
    Pre2024Primeiro = Pre2024Primeiro.astype(float)
    media = statistics.mean(Pre2024Primeiro)
    desvPad = statistics.stdev(Pre2024Primeiro)
    coefVar = desvPad/media
    return media, coefVar, desvPad, Pre2024Primeiro

def Pre2024Segundo():
    Pre2024Segundo = planilha['Pre2024Segundo'].str.replace(',', '.')
    Pre2024Segundo = Pre2024Segundo.astype(float)
    media = statistics.mean(Pre2024Segundo)
    desvPad = statistics.stdev(Pre2024Segundo)
    coefVar = desvPad/media
    return media, coefVar, desvPad, Pre2024Segundo


def Ipca2026():
    Ipca2026 = planilha['Ipca2026'].str.replace(',', '.')
    Ipca2026 = Ipca2026.astype(float)
    media = statistics.mean(Ipca2026)
    desvPad = statistics.stdev(Ipca2026)
    coefVar = desvPad/media
    return media, coefVar, desvPad, Ipca2026



def contaMenores():

    coeficientes = []
    Selic26 = Selic2026()[1]
    Selic28 = Selic2028()[1]
    Prp24 = Pre2024Primeiro()[1]
    Prs24 = Pre2024Segundo()[1]
    Ipca26 = Ipca2026()[1]

    coeficientes.append(Selic26)
    coeficientes.append(Selic28)
    coeficientes.append(Prp24)
    coeficientes.append(Prs24)
    coeficientes.append(Ipca26)
    menor = min(coeficientes)
    segundoMenor = min(n for n in coeficientes if n != menor)


    return menor, segundoMenor


def escolherMenorp():
    menor = contaMenores()[0]
    segundoMenor = contaMenores()[1]
    
    dic = {
    Selic2026()[1] :[ Selic2026(), 'Selic 2026'],
    Selic2028()[1] : [Selic2028(), 'Selic 2028'],
    Pre2024Primeiro()[1] : [Pre2024Primeiro(), 'Prefixado 2024 Primeiro Semestre'],
    Pre2024Segundo()[1] : [Pre2024Segundo(), 'Prefixado 2026 Segundo Semestre'],
    Ipca2026()[1] : [Ipca2026(), 'Ipca 2026']
    }


    m = dic[menor][0]
    sm = dic[segundoMenor][0]


    nome1 = dic[menor][1]
    nome2 = dic[segundoMenor][1]

    return m, sm, nome1, nome2






def dadosSharpp():
    # preciso fazer essa escolha automática do programa
    ativo1 = escolherMenorp()[0]
    ativo2 = escolherMenorp()[1]

    mediaativo1 = ativo1[0]
    mediaativo2 = ativo2[0]


    
    desvPadativo1 = ativo1[2]
    desvPadativo2 = ativo2[2]


    varativo1 = desvPadativo1**2
    varativo2 = desvPadativo2**2

    correl = stats.pearsonr(ativo1[3], ativo2[3])
    correl = correl[0]

    covar = desvPadativo1*desvPadativo2*correl
    

    reff = cdb1()[0]
    

    return mediaativo1, mediaativo2, desvPadativo1, desvPadativo2, varativo1, varativo2, correl, covar, reff

