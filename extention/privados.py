# pandas foi importado para importar os dados do arquivo .csv
import pandas as pd
# statistics foi importado para fazer contas de média e desvio padrão
import statistics
# SciPy foi importado para fazer a conta de correlação de pearson
import scipy.stats as stats



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



# as demais funções de ativos abaixo seguem a mesma estrutura do comentado acima
def cdb1():
    # foi guardado a serie de dados do CDB  em uma variável para posteriormente tratarmos esses dados
    # além disso, foi necessário substituir as ',' com '.' para ser possível tratar os dados
    cdb = planilha['CDB'].str.replace(',', '.')
    # para poder tratar os dados como números, foram transformados em float
    cdb = cdb.astype(float)
    # usando a biblioteca statistics, foi calculado a média dos dados 
    media = statistics.mean(cdb)
    # usando a biblioteca statistics, foi calculado o desvio padrão amostral dos dados
    desvPad = statistics.stdev(cdb)
    # foi calculado o coeficiente de variação com a formula que foi ensidada
    coefVar = desvPad/media
    ## foi guardado a serie de dados do CDB  em uma variável para posteriormente tratarmos esses dados
    # além disso, foi necessário substituir as ',' com '.' para ser possível tratar os dados
    pu = planilha['puCdb'].str.replace(',', '.')
    # para poder tratar os dados como números, foram transformados em float
    pu = pu.astype(float)
    # calculo de rentabilidade do título
    rentabilidade = (pu.iloc[-1]-pu.iloc[0])/pu.iloc[0]
    #  todos os dados calculados foram exportados com o 'return' para poderem ser usados em outras funções 
    return media, coefVar, desvPad, cdb, rentabilidade




# as demais funções de ativos abaixo seguem a mesma estrutura do comentado acima
def petr36():
    petr36 = planilha['PETR36'].str.replace(',', '.')
    petr36 = petr36.astype(float)
    media = statistics.mean(petr36)
    desvPad = statistics.stdev(petr36)
    coefVar = desvPad/media
    pu = planilha['puPet'].str.replace(',', '.')
    pu = pu.astype(float)
    rentabilidade = (pu.iloc[-1]-pu.iloc[0])/pu.iloc[0] 

    return media, coefVar, desvPad, petr36, rentabilidade



def Cpld26():
    Cpld26 = planilha['CPLD26'].str.replace(',', '.')
    Cpld26 = Cpld26.astype(float)
    media = statistics.mean(Cpld26)
    desvPad = statistics.stdev(Cpld26)
    coefVar = desvPad/media
    pu = planilha['puCp'].str.replace(',', '.')
    pu = pu.astype(float)
    rentabilidade = (pu.iloc[-1]-pu.iloc[0])/pu.iloc[0] 
    return media, coefVar, desvPad, Cpld26, rentabilidade



def Taee26():
    Taee26 = planilha['TAEE26'].str.replace(',', '.')
    Taee26 = Taee26.astype(float)
    media = statistics.mean(Taee26)
    desvPad = statistics.stdev(Taee26)
    coefVar = desvPad/media
    pu = planilha['puTae'].str.replace(',', '.')
    pu = pu.astype(float)
    rentabilidade = (pu.iloc[-1]-pu.iloc[0])/pu.iloc[0] 
    return media, coefVar, desvPad, Taee26, rentabilidade



def Itsa24():
    Itsa24 = planilha['ITSA24'].str.replace(',', '.')
    Itsa24 = Itsa24.astype(float)
    media = statistics.mean(Itsa24)
    desvPad = statistics.stdev(Itsa24)
    coefVar = desvPad/media
    pu = planilha['puIt'].str.replace(',', '.')
    pu = pu.astype(float)
    rentabilidade = (pu.iloc[-1]-pu.iloc[0])/pu.iloc[0] 
    return media, coefVar, desvPad, Itsa24, rentabilidade


# a função contaMenores() foi usada para localizar os dois menores coeficientes de variação entre os ativos selecionados
def contaMenores():
    
    # foi criado uma lista para que para guardar os coeficientes de cada um dos ativos
    coeficientes = []

    # foram criado variaveis para guardar cada coeficiente de variação de cada ativo
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

    # a variavel m e n foram criadas para acessar as funções que estão no index[0] que correspondem aos dois menores coeficientes
    m = dic[menor][0]
    sm = dic[segundoMenor][0]

    # a variavel nome1 e nome3 foram criadas para acessar os nomes dos ativos que estão no index[1] que correspondem aos dois menores coeficientes
    nome1 = dic[menor][1]
    nome2 = dic[segundoMenor][1]

    # as variáveis foram exportadas com 'return' para serem usadas em outras funções
    return m, sm, nome1, nome2




def dadosSharp():
    # froam criadas as variáveis ativo1 e ativo2 para guardarem a função dos ativos selecionados com os menores coeficientes de variação
    ativo1 = escolherMenor()[0]
    ativo2 = escolherMenor()[1]

    # foram criadas as variáveis mediaativo1 e mediaativo2 para guardarem as médias dos ativos 1 e 2
    # como ativo1 e ativo2 são funções, as médias foram buscadas com o index[0], sendo o primeiro elemento exportado de cada função a média do ativo
    mediaativo1 = ativo1[0]
    mediaativo2 = ativo2[0]

    
    # foram criadas as variáveis desvPadativo1 e desvPadativo2 para guardarem os desvios padrão dos ativos 1 e 2
    # como ativo1 e ativo2 são funções, os desvios padrão foram buscadas com o index[2], sendo o terceiro elemento exportado de cada função o desvio padrão do ativo
    desvPadativo1 = ativo1[2]
    desvPadativo2 = ativo2[2]

    # foram criadas as variáveis varativo1 e varativo2 para guardarem as variâncias dos ativos 1 e 2
    # como a variância é o quadrado do desvio padrão, foi feito isso para cada um dos dados
    varativo1 = desvPadativo1**2
    varativo2 = desvPadativo2**2

    # foi calculada a correlação dos ativos com a biblioteca SciPy que calcula a correlação de perarson. Como o resultado dessa função é um objeto, foi feita a procura do
    # dado que era necessário, assim o novo valor da variável correl foi setado para o index[0], ou seja, o primeiro elemento do resultado da conta de pearson
    correl = stats.pearsonr(ativo1[3], ativo2[3])
    correl = correl[0]
    
    # a covariância foi calculada de acordo com a fórmula fornecida pelo professor
    covar = desvPadativo1*desvPadativo2*correl
    
    # a refencia de ativo livre de risco (reff) foi a média dos retornos diários do CDI e como o CDB replica o CDI, a média do mesmo foi usada
    reff = cdb1()[0]
    
    # os devidos dados necessários para o sharpe foram exportados para serem usados em outras funções
    return mediaativo1, mediaativo2, desvPadativo1, desvPadativo2, varativo1, varativo2, correl, covar, reff

