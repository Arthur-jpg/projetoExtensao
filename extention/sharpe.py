# numpy foi usado para para ser possível utilizar uma função range() que aceite numeros float
import numpy as np
# os dados necessários para o cálculo do sharpe vieram dos respectivos arquivos públicos e privados
from privados import dadosSharp
from privados import escolherMenor
from publicos import escolherMenorp 
from publicos import dadosSharpp

# foi criado uma função para os privados para calcular separadamente o sharpe dos ativos selecionados
def calculoPrivados():
    # a variável alocação foi criada para guardar os valores da porcentagem da do ativo1 na carteira, essa porcentagem vai de 1% a 100%
    alocacao = np.arange(0, 1, 0.01)
    # a variável topAlocação foi criada para guardar o valor da melhor alocação, porém ela começa no valor zero
    topAlocacao = 0
    # a variável top sharpe foi criada para guradar o valor do melhor sharpe, porém ela começa no valor zero, como estado inicial, depois ela receberá um novo valor 
    topSharpe = 0
    
    # um for loop foi criado para poder iterar as diferentes alocações (porcentagens do ativo A na carteira) e fazer o cálculo com todas essas possibilidades 
    for x in alocacao:
        # a média da carteira foi calculada de acordo com a fórmula fornecida pelo professor e os dados usados foram puxados das planilhas e funções importadas
        mediaCarteira = (x*dadosSharp()[0])+((1-x)*dadosSharp()[1])
        # a variância da carteira foi calculada de acordo com a fórmula fornecida pelo professor e os dados usados foram puxados das planilhas e funções importadas
        varCarteira = ((x**2)*dadosSharp()[4])+(((1-x)**2)*dadosSharp()[5])+(2*x*(1-x)*dadosSharp()[7])
        # o desvio padrão da carteira foi calculado com a raiz da variância
        desvPadCarteira = varCarteira**0.5
        # a reff ou a taxa livre de risco foi puxada do arquivo importado, assim como as funções usadas
        reff = dadosSharp()[8]
        # o calculo do sharpe foi executado de acordo com a fórmula fornecida pelo professor 
        sharpe = (mediaCarteira-reff)/desvPadCarteira
        
        # como a função condicional if está dentro do i toda vez o program roda o sharpe será maior que o anterior, até não ser mais, onde a função break irá parar o loop
        if sharpe > topSharpe:
            #toda vez que o programa roda se o sharpe for maior que o anterior, o novo valor dele será guardado na variável, assim possibilitando a lógica, o mesmo
            # acontecerá com a alocação
            topSharpe = sharpe
            topAlocacao = x
        # se o sharpe for menor que o sharpe anterior o programa para, pois o resultado já teria sido encontrado
        elif sharpe < topSharpe:
            break
    Sharpe = topSharpe
    Alocacao = topAlocacao

    return Sharpe, Alocacao
    
# foi criado uma função para os privados para calcular separadamente o sharpe dos ativos selecionados
def calculoPublico():
    # a variável alocação foi criada para guardar os valores da porcentagem da do ativo1 na carteira, essa porcentagem vai de 1% a 100%
    alocacoes = np.arange(0, 1.00, 0.01)
    # a variável topAlocação foi criada para guardar o valor da melhor alocação, porém ela começa no valor zero
    topAlocacao = 0 
    # a variável top sharpe foi criada para guradar o valor do melhor sharpe, porém ela começa no valor zero, como estado inicial, depois ela receberá um novo valor
    topSharpe = 0

    # um for loop foi criado para poder iterar as diferentes alocações (porcentagens do ativo A na carteira) e fazer o cálculo com todas essas possibilidades 
    for i in alocacoes:
        # a média da carteira foi calculada de acordo com a fórmula fornecida pelo professor e os dados usados foram puxados das planilhas e funções importadas
        mediaCarteira = (i*dadosSharpp()[0])+((1-i)*dadosSharpp()[1])
        # a variância da carteira foi calculada de acordo com a fórmula fornecida pelo professor e os dados usados foram puxados das planilhas e funções importadas
        varCarteira = ((i**2)*dadosSharpp()[4])+(((1-i)**2)*dadosSharpp()[5])+(2*i*(1-i)*dadosSharpp()[7])
        # o desvio padrão da carteira foi calculado com a raiz da variância
        desvPadCarteira = varCarteira**0.5
        # a reff ou a taxa livre de risco foi puxada do arquivo importado, assim como as funções usadas
        reff = dadosSharpp()[8]
        # o calculo do sharpe foi executado de acordo com a fórmula fornecida pelo professor 
        sharpe = (mediaCarteira-reff)/desvPadCarteira
        # como a função condicional if está dentro do i toda vez o program roda o sharpe será maior que o anterior, até não ser mais, onde a função break irá parar o loop
        if sharpe > topSharpe:
            #toda vez que o programa roda se o sharpe for maior que o anterior, o novo valor dele será guardado na variável, assim possibilitando a lógica, o mesmo
            # acontecerá com a alocação
            topSharpe = sharpe
            topAlocacao = i
        # se o sharpe for menor que o sharpe anterior o programa para, pois o resultado já teria sido encontrado
        elif sharpe < topSharpe:
            break
    sharpMelhor = topSharpe
    alocacaoMelhor = topAlocacao
    

    return sharpMelhor, alocacaoMelhor


def main():
    
    # para poder printar e receber os resultados, as variáveis foram criadas para poder guardar os valores do sharpe e a
    # porcentagem dos ativos na carteira
    sharpe = calculoPrivados()[0]
    alocacao = calculoPrivados()[1]

    # para poder receber o nome dos ativos foi importado da função escolherMenor os nomes dos ativos selecionados
    ativo1 = escolherMenor()[2]
    ativo2 = escolherMenor()[3]

    # para printar os resultados foi usado a função print. Para arredondar os reultados, foi utilizado da função round
    # for fim, para receber os valores das porcentagens foi, os resultados foram multiplicados por 100

    print(f'O índice de sharp dos ativos de natureza privada foi de: {round(sharpe, 5)}')
    print(f'O primeiro ativo {ativo1} com {round(100* alocacao, 2)}% de alocação')
    print(f'O segundo ativo {ativo2} com alocação de {round(100*(1-alocacao), 2)}%')

    # para poder printar e receber os resultados, as variáveis foram criadas para poder guardar os valores do sharpe e a
    # porcentagem dos ativos na carteira
    sharpe2 = calculoPublico()[0]
    alocacao2 = calculoPublico()[1]

    # para poder receber o nome dos ativos foi importado da função escolherMenor os nomes dos ativos selecionados
    ativo10 = escolherMenorp()[2]
    ativo20 = escolherMenorp()[3]

    # para printar os resultados foi usado a função print. Para arredondar os reultados, foi utilizado da função round
    # for fim, para receber os valores das porcentagens foi, os resultados foram multiplicados por 100
    print('-----------------------------------------------')
    print(f'O índice de sharp dos ativos de natureza pública {round(sharpe2, 5)}')
    print(f'O primeiro ativo {ativo10} com {round(100* alocacao2, 2)}% de alocação')
    print(f'O segundo ativo {ativo20} com alocação de {round(100*(1-alocacao2), 2)}%')
    
    

main()




  


