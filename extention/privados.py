import pandas as pd
import statistics
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

arquivo = 'dadoscertos.csv'

planilha = pd.read_csv(arquivo, sep=';')


def ibov():
    ibov = planilha['IBOV'].str.replace(',', '.')
    
    ibov = ibov.astype(float)
    
    media = statistics.mean(ibov)
    desvPad = statistics.stdev(ibov)
    coefVar = desvPad/media

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


def contaMenores():

    coeficientes = []
    Citsa24 = Itsa24()[1]
    Ctaee26 = Taee26()[1]
    Ccpld26 = Cpld26()[1]
    Cpetr3 = petr36()[1]
    Ccdb = cdb1()[1]

    coeficientes.append(Citsa24)
    coeficientes.append(Ctaee26)
    coeficientes.append(Ccpld26)
    coeficientes.append(Cpetr3)
    coeficientes.append(Ccdb)
    menor = min(coeficientes)
    segundoMenor = min(n for n in coeficientes if n != menor)


    return menor, segundoMenor


def escolherMenor():
    menor = contaMenores()[0]
    segundoMenor = contaMenores()[1]
    
    dic = {
    Itsa24()[1] :[Itsa24(),'Itsa24'],
    Taee26()[1] : [Taee26(), 'Taee26'],
    Cpld26()[1] : [Cpld26(), 'Cpld26'],
    petr36()[1] : [petr36(), 'Petr36'],
    cdb1()[1] : [cdb1(), 'Cdb']
    }

    m = dic[menor][0]
    sm = dic[segundoMenor][0]

    nome1 = dic[menor][1]
    nome2 = dic[segundoMenor][1]


    return m, sm, nome1, nome2




def dadosSharp():
    # preciso fazer essa escolha automática do programa
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

