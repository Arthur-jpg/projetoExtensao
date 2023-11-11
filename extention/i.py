from privados import dadosSharp
from publicos import dadosSharpp
import numpy as np

def calculoPrivados():
    alocacao = range(0, 100, 1)
    topAlocacao = 0
    topSharpe = -float('inf')

    for x in alocacao:
        mediaCarteira = (x * dadosSharp()[0]) + ((1 - x) * dadosSharp()[1])
        varCarteira = ((x ** 2) * dadosSharp()[4]) + (((1 - x) ** 2) * dadosSharp()[5]) + (2 * x * (1 - x) * dadosSharp()[7])
        desvPadCarteira = varCarteira ** 0.5
        reff = dadosSharp()[8]
        sharpe = (mediaCarteira - reff) / desvPadCarteira

        if sharpe > topSharpe:
            topSharpe = sharpe
            topAlocacao = x

    # Corrigindo a indentação do return
    Sharpe = topSharpe
    Alocacao = topAlocacao

    print(Sharpe, Alocacao)
    return Sharpe, Alocacao

calculoPrivados()
