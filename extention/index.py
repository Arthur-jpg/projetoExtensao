from sharpe import variaveis
import time
from rentabilidade import rentabilidadeGeral, carteiraPrivada, carteiraPublica
from graficos import main2
from beta import betaPrivado, betaPublico, betaTotal


while True:
    try:
        inp = input('Entre o valor aportado: ').casefold().replace('r$','').replace(',', '.')
        inp = float(inp)
        break
    except:
        print('Entrada não válida! Tente novamente!')
    
    
   
print(inp)
    

def sharpe():
    alocacao = variaveis()
    ativo1 = variaveis()
    ativo2 = variaveis()
    sharpe1 = variaveis()
    alocacao, ativo1, ativo2, sharpe1 = alocacao[10], ativo1[6], ativo2[7], sharpe1[4]

    alocacao2 = variaveis()
    ativo10 = variaveis()
    ativo20 = variaveis()
    sharpe2 = variaveis()
    alocacao2, ativo10, ativo20, sharpe2 = alocacao2[11], ativo10[8], ativo20[9], sharpe2[5]

    

    # para printar os resultados foi usado a função print. Para arredondar os reultados, foi utilizado da função round
    # for fim, para receber os valores das porcentagens foi, os resultados foram multiplicados por 100
    print(f'O índice de Sharpe dos ativos de natureza privada foi de: {round(sharpe1, 5)}')
    print(f'O primeiro ativo {ativo1} com {round(100* alocacao, 2)}% de alocação')
    print(f'O segundo ativo {ativo2} com alocação de {round(100*(1-alocacao), 2)}%')

    # para printar os resultados foi usado a função print. Para arredondar os reultados, foi utilizado da função round
    # for fim, para receber os valores das porcentagens foi, os resultados foram multiplicados por 100
    print()
    print(f'O índice de Sharpe dos ativos de natureza pública foi de: {round(sharpe2, 5)}')
    print(f'O primeiro ativo {ativo10} com {round(100* alocacao2, 2)}% de alocação')
    print(f'O segundo ativo {ativo20} com alocação de {round(100*(1-alocacao2), 2)}%')

def rentabilidade():
    rentGeral = rentabilidadeGeral()
    rentGeral = rentGeral[0]

    rentPriv = carteiraPrivada()
    rentPriv = rentPriv[2]

    rentPu = carteiraPublica()
    rentPu = rentPu[2]

    aporte = inp
    print(f'Rentabilidade Carteira Privada {round(rentPriv*100, 2)}%')
    print(f'Rentabilidade Carteira Pública {round(rentPu*100,2)}%')
    print(f'Rentabilidade geral da Carteira {round(rentGeral*100, 2)}%')
    time.sleep(2)
    print()
    print(f'O valor aportado foi de: R${aporte}')
    print(f'O juros recebido da carteira privada foi de: R${round((aporte/2)*rentPriv, 2)} ')
    print(f'O juros recebido da carteira publica foi de: R${round((aporte/2)*rentPu, 2)} ')
    print(f'O juros total recebido foi de: R${round(aporte*rentGeral, 2)} ')
    time.sleep(2)
    print('-'*60)
    print('RESULTADO')
    print()
    print(f'O valor final do investimento é de: R${round(aporte*rentGeral+aporte, 2)}')

def beta():
    betaA1 = betaPrivado()
    betaA2 = betaPublico()
    
    betaTotal1 = betaTotal()


    print(f'O Beta da carteira privada é de: {betaA1} ')
    print(f'O Beta da carteira pública é de: {betaA2} ')
    print(f'O Beta total da carteira é de: {betaTotal1} ')
    print()


    if betaA1 or betaA2 < 0:
        print('O beta da carteira é menor que Zero.')
        print('Isso quer dizer que a carteira tem o movimento contrário do mercado')
        print()
    elif betaA1 or betaA2 > 0 and betaA1 or betaA2 < 1 :
        print('O beta da carteira é maior que Zero e maior que Um.')
        print('Isso quer dizer que a carteira é de baixo risco, pois varia menos que o mercado')
        print()  
    elif  betaA1 or betaA2 > 1:     
        print('O beta da carteira é maior que Um.')
        print('Isso quer dizer que a carteira é de alto risco uma vez que varia mais que o mercado')  

def grafico():
    main2()



def main():
    print('-'*60)
    print('SHARPE')
    print()
    sharpe()
    time.sleep(2)
    print('-'*60)

    print('COEFICIENTE BETA')
    print()
    beta()
    time.sleep(2)
    print('-'*60)

    print('RENTABILIDADE')
    print()
    rentabilidade()
    time.sleep(2)
    print('-'*60)

    grafico()

main()

    