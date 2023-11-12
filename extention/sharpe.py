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
    
    media1 = dadosSharp()[0]
    media2 = dadosSharp()[1]

    var1 = dadosSharp()[4]
    var2 = dadosSharp()[5]

    covar = dadosSharp()[7]

    reff = dadosSharp()[8]

    # um for loop foi criado para poder iterar as diferentes alocações (porcentagens do ativo A na carteira) e fazer o cálculo com todas essas possibilidades 
    for x in alocacao:
        # a média da carteira foi calculada de acordo com a fórmula fornecida pelo professor e os dados usados foram puxados das planilhas e funções importadas
        mediaCarteira = (x*media1)+((1-x)*media2)
        # a variância da carteira foi calculada de acordo com a fórmula fornecida pelo professor e os dados usados foram puxados das planilhas e funções importadas
        varCarteira = ((x**2)*var1)+(((1-x)**2)*var2)+(2*x*(1-x)*covar)
        # o desvio padrão da carteira foi calculado com a raiz da variância
        desvPadCarteira = varCarteira**0.5
        # a reff ou a taxa livre de risco foi puxada do arquivo importado, assim como as funções usadas
        
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

    media1 = dadosSharpp()[0]
    media2 = dadosSharpp()[1]

    var1 = dadosSharpp()[4]
    var2 = dadosSharpp()[5]

    covar = dadosSharpp()[7]

    reff = dadosSharpp()[8]


    # um for loop foi criado para poder iterar as diferentes alocações (porcentagens do ativo A na carteira) e fazer o cálculo com todas essas possibilidades 
    for i in alocacoes:
        # a média da carteira foi calculada de acordo com a fórmula fornecida pelo professor e os dados usados foram puxados das planilhas e funções importadas
        mediaCarteira = (i*media1)+((1-i)*media2)
        # a variância da carteira foi calculada de acordo com a fórmula fornecida pelo professor e os dados usados foram puxados das planilhas e funções importadas
        varCarteira = ((i**2)*var1)+(((1-i)**2)*var2)+(2*i*(1-i)*covar)
        # o desvio padrão da carteira foi calculado com a raiz da variância
        desvPadCarteira = varCarteira**0.5
        # a reff ou a taxa livre de risco foi puxada do arquivo importado, assim como as funções usadas
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



def variaveis():
    privados = calculoPrivados()
    publicos = calculoPublico()
    
    # para poder printar e receber os resultados, as variáveis foram criadas para poder guardar os valores do sharpe e a
    # porcentagem dos ativos na carteira
    sharpe = privados[0]
    alocacao = privados[1]


    # para poder receber o nome dos ativos foi importado da função escolherMenor os nomes dos ativos selecionados
    ativo1 = escolherMenor()[2]
    ativo2 = escolherMenor()[3]



    # para poder printar e receber os resultados, as variáveis foram criadas para poder guardar os valores do sharpe e a
    # porcentagem dos ativos na carteira
    sharpe2 = publicos[0]
    alocacao2 = publicos[1]


    # para poder receber o nome dos ativos foi importado da função escolherMenor os nomes dos ativos selecionados
    ativo10 = escolherMenorp()[2]
    ativo20 = escolherMenorp()[3]

    alocacaoAt1 = alocacao
    alocacaoAt2 = 1 - alocacao
    alocacaoAt10 = alocacao2
    alocacaoAt20 = 1 - alocacao2

    return alocacaoAt1, alocacaoAt2, alocacaoAt10, alocacaoAt20





variaveis()


  


