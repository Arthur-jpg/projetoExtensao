from privados import dadosSharp
import numpy as np
from privados import escolherMenor
from publicos import escolherMenorp 
from publicos import dadosSharpp

def calculoPrivados():

    alocacao = np.arange(0, 1, 0.01)
    topAlocacao = 0
    topSharpe = 0
    reff = dadosSharp()[8]
    for x in alocacao:
        mediaCarteira = (x*dadosSharp()[0])+((1-x)*dadosSharp()[1])
        varCarteira = ((x**2)*dadosSharp()[4])+(((1-x)**2)*dadosSharp()[5])+(2*x*(1-x)*dadosSharp()[7])
        desvPadCarteira = varCarteira**0.5
        sharpe = (mediaCarteira-reff)/desvPadCarteira

        if sharpe > topSharpe:
            topSharpe = sharpe
            topAlocacao = x
    Sharpe = topSharpe
    Alocacao = topAlocacao

    return Sharpe, Alocacao
    

def calculoPublico():

    alocacoes = np.arange(0, 1.00, 0.01)
    topAlocacao = 0 
    topSharpe = 0

    for i in alocacoes:
        mediaCarteira = (i*dadosSharpp()[0])+((1-i)*dadosSharpp()[1])
        varCarteira = ((i**2)*dadosSharpp()[4])+(((1-i)**2)*dadosSharpp()[5])+(2*i*(1-i)*dadosSharpp()[7])
        desvPadCarteira = varCarteira**0.5
        reff = dadosSharpp()[8]
        sharpe = (mediaCarteira-reff)/desvPadCarteira
        if sharpe > topSharpe:
            topSharpe = sharpe
            topAlocacao = i
    sharpMelhor = topSharpe
    alocacaoMelhor = topAlocacao
    

    return sharpMelhor, alocacaoMelhor


def main():
    
    
    sharpe = calculoPrivados()[0]
    alocacao = calculoPrivados()[1]


    ativo1 = escolherMenor()[2]
    ativo2 = escolherMenor()[3]

    print(f'O índice de sharp deu igual a {round(sharpe, 5)}')
    print(f'O primeiro ativo {ativo1} com {round(100* alocacao, 2)}% de alocação')
    print(f'O segundo ativo {ativo2} com alocação de {round(100*(1-alocacao), 2)}%')


    sharpe2 = calculoPublico()[0]
    alocacao2 = calculoPublico()[1]


    ativo10 = escolherMenorp()[2]
    ativo20 = escolherMenorp()[3]
    print('-----------------------------------------------')
    print(f'O índice de sharp deu igual a {round(sharpe2, 5)}')
    print(f'O primeiro ativo {ativo10} com {round(100* alocacao2, 2)}% de alocação')
    print(f'O segundo ativo {ativo20} com alocação de {round(100*(1-alocacao2), 2)}%')
    
    


# if __name__ == '__main__':
#     main()




  


