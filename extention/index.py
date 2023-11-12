from sharpe import main
from sharpe import calculoPrivados
from sharpe import calculoPublico
import numpy as np
from tqdm import tqdm
from time import sleep

def sharpe():
    # para printar os resultados foi usado a função print. Para arredondar os reultados, foi utilizado da função round
    # for fim, para receber os valores das porcentagens foi, os resultados foram multiplicados por 100
    print(f'O índice de sharp dos ativos de natureza privada foi de: {round(sharpe, 5)}')
    print(f'O primeiro ativo {ativo1} com {round(100* alocacao, 2)}% de alocação')
    print(f'O segundo ativo {ativo2} com alocação de {round(100*(1-alocacao), 2)}%')

    # para printar os resultados foi usado a função print. Para arredondar os reultados, foi utilizado da função round
    # for fim, para receber os valores das porcentagens foi, os resultados foram multiplicados por 100
    print('-----------------------------------------------')
    print(f'O índice de sharp dos ativos de natureza pública {round(sharpe2, 5)}')
    print(f'O primeiro ativo {ativo10} com {round(100* alocacao2, 2)}% de alocação')
    print(f'O segundo ativo {ativo20} com alocação de {round(100*(1-alocacao2), 2)}%')