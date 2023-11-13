# foi importado as devidas funções e bibliotecas necessárias para a funcionalidade do programa
from sharpe import variaveis
import time
from rentabilidade import rentabilidadeGeral, carteiraPrivada, carteiraPublica
from graficos import main2
from beta import betaPrivado, betaPublico, betaTotal
from treynor import treynor


# foi feito um while loop para testar o input de aporte
while True:
    try:
        # para receber o valor foi chamado um input que recebe o casefold para deixar todos os caracteres minúculos
        # além disso, foi usado o replace para para ter consertar alguns erros que poderia ocorrer no input
        inp = input('Entre o valor aportado: ').casefold().replace('r$','').replace(',', '.')
        # o input foi transformado em float para ser utilizado para fazer conta
        inp = float(inp)
        # caso de tudo certo o while loop irá parar e o resto do código 
        break
    except:
        # caso o input não seja válido, será printado a mensagem abaixo e o user poderá entrar outro dado novamente
        print('Entrada não válida! Tente novamente!')
    
    
# após receber o a porte o programa mostra quanto foi o valor aportado
print(f'R${inp}')
    

# foi criado uma função sharpe para que todos os dados necessários fossem usados para mostrar informações com funções print
def sharpe():
    # foram criadas variáveis para retornarem os dados necessários para mostar as informações pedidas
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

# foi criada una função rentabilidade para receber e mostar todos os dados necessários 
def rentabilidade():
    # foram criadas variáveis para retornarem os dados necessários para mostar as informações pedidas
    rentGeral = rentabilidadeGeral()
    rentGeral = rentGeral[0]

    rentPriv = carteiraPrivada()
    rentPriv = rentPriv[2]

    rentPu = carteiraPublica()
    rentPu = rentPu[2]

    # para fazer as contas com o aporte os seus dados foram colocados em forma de uma variável
    aporte = inp
    # cada print tem uma função round para arrendondar o resultado para que não fique com mais de 2 casas decimais
    print(f'Rentabilidade Carteira Privada {round(rentPriv*100, 2)}%')
    print(f'Rentabilidade Carteira Pública {round(rentPu*100,2)}%')
    print(f'Rentabilidade geral da Carteira {round(rentGeral*100, 2)}%')
    # time sleep foi implementado para dar um tempo entre a geração de dados, para não ficar instantâneo
    time.sleep(2)
    print()
    print(f'O valor aportado foi de: R${aporte}')
    print(f'O juros recebido da carteira privada foi de: R${round((aporte/2)*rentPriv, 2)} ')
    print(f'O juros recebido da carteira publica foi de: R${round((aporte/2)*rentPu, 2)} ')
    print(f'O juros total recebido foi de: R${round(aporte*rentGeral, 2)} ')
    # time sleep foi implementado para dar um tempo entre a geração de dados, para não ficar instantâneo
    time.sleep(2)
    print('-'*60)
    print('RESULTADO')
    print()
    print(f'O valor final do investimento é de: R${round(aporte*rentGeral+aporte, 2)}')

# foi criada una função beta para receber e mostar todos os dados necessários 
def beta():
    # foram criadas variáveis para retornarem os dados necessários para mostar as informações pedidas
    betaA1 = betaPrivado()
    betaA2 = betaPublico()
    
    betaTotal1 = betaTotal()

    # foram criados funções print para mostar os resultados necessários
    print(f'O Beta da carteira privada é de: {betaA1} ')
    print(f'O Beta da carteira pública é de: {betaA2} ')
    print(f'O Beta total da carteira é de: {betaTotal1} ')
    print()

    # foi criado uma relação de if statements para poder testar e saber se o valor é maior, menor ou entre zero e um
    # assim que testado a mensagem muda de acordo com a condição que ela implica
    if betaTotal1 < 0:
        print('O beta da carteira é menor que Zero.')
        print('Isso quer dizer que a carteira tem o movimento contrário do mercado')
        print()
    elif betaTotal1 > 0 and betaTotal1 < 1 :
        print('O beta da carteira é maior que Zero e menor que Um.')
        print('Isso quer dizer que a carteira é de baixo risco, pois varia menos que o mercado')
        print()  
    elif  betaTotal1 > 1:     
        print('O beta da carteira é maior que Um.')
        print('Isso quer dizer que a carteira é de alto risco uma vez que varia mais que o mercado')  
    else:
        # caso o valor testado não cumpra nenhum dos requisitos será mostrado uma mensagem de erro
        print('Algo deu errado')

# foi criada una função Treynor para receber e mostar todos os dados necessários
def Treynor():
    # foi criada uma variável para retornar os dados pedidos
    treynorr = treynor()

    # foi usado uma função print() para mostar o resultado do índice
    print(f'O índice de Treynor da carteira é igual á {treynorr}')

    # foi feito uma relação condicional para demostra como interpretar o índice
    if treynorr > 0:
        print('Sendo o índice maior que zero, o investimento na carteira compensou em relação à taxa livre de risco')
    elif treynorr < 0:
        print('Sendo o índice menor que zero, o investimento na carteira não compensou em relação à taxa livre de risco')
    else: 
        print('Algo deu errado')
    
    
# foi criado uma função grafico para gerar os gráficos requisitados
def grafico():
    main2()


# foi feita uma função main (função principal) para poder rodar todas as funções acima na ordem necessária
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

    print('ÍNDICE DE TREYNOR')
    print()
    Treynor()
    time.sleep(2)
    print('-'*60)

    print('RENTABILIDADE')
    print()
    rentabilidade()
    time.sleep(2)
    print('-'*60)

    grafico()




if __name__ == '__main__':
    main()

    