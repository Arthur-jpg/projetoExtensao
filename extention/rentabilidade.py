# foram importados uma série de funções para que seus dados exportados fossem usados
from publicos import escolherMenorp
from privados import escolherMenor
from sharpe import variaveis

# foi criado uma variavel global para que fosse usada dentro das funções
aloca = variaveis()

# foi criada uma função para calcular a rentabilidade da carteira privada
def carteiraPrivada():
    # para acessar os ativos escolhidos foi usada a fução escolherMenor() 
    ativo1 = escolherMenor()
    ativo2 = escolherMenor()

    # foi criada variáveis para acessar os dados para que a função não seja rodada mais do que o necessário
    # essas variáveis retornam a função do ativo escolhido, para que os dados sejam usados posteriormente;
    ativo1 = ativo1[0]
    ativo2 = ativo2[1]
    
        # para acessar o rendimento diário do ativo foi retirado da função retornada pela variável de cima
    rdiario1 =  ativo1[3]
    rdiario2 = ativo2[3]

    # para acessar a rentabilidade do ativo foi retirado da função retornada pela variável acima
    rentabilidade1 = ativo1[4]
    rentabilidade2 = ativo2[4]

    # para acessar a porcentagem dos ativos na carteira foi usado a função global retornada no início 
    pAt1 = aloca[0]
    pAt2 = aloca[1]
    
    # o rendimento diário foi calculado com as variáveis criadas multiplicado pelas respectivas porcentagens  na carteira 
    rentabilidadeG1 = rentabilidade1*pAt1 + rentabilidade2*pAt2 

    # a rentabilidade geral foi calculada com as variáveis criadas multiplicando pelas respectivas porcentagens na carteira
    rendimentoDiario = rdiario1*pAt1 + rdiario2*pAt2

    # para que os dados calculados fossem usados em outras funções, foram exportados com o 'return'
    return rentabilidade1, rentabilidade2, rentabilidadeG1, rendimentoDiario,pAt1, pAt2

# foi criada uma função para calcular a rentabilidade da carteira pública 
def carteiraPublica():
    # para acessar os ativos escolhidos foi usada a fução escolherMenorp() 
    ativo10 = escolherMenorp()
    ativo20 = escolherMenorp()

    # foi criada funções para acessar os dados para que a função não seja rodada mais do que o necessário
    # essas variáveis retornam a função do ativo escolhido, para que os dados sejam usados posteriormente
    ativo1 = ativo10[0]
    ativo2 = ativo20[1]

    # para acessar o rendimento diário do ativo foi retirado da função retornada pela variável de cima
    rdiario1 =  ativo1[3]
    rdiario2 = ativo2[3]

    # para acessar a rentabilidade do ativo foi retirado da função retornada pela variável acima
    rentabilidade1 = ativo1[4]
    rentabilidade2 = ativo2[4]

    # para acessar a porcentagem dos ativos na carteira foi usado a função global retornada no início 
    pAt1 = aloca[2]
    pAt2 = aloca[3]
    
    # o rendimento diário foi calculado com as variáveis criadas multiplicado pelas respectivas porcentagen na carteira
    rendimentoDiario = rdiario1*pAt1 + rdiario2*pAt2

    # a rentabilidade geral foi calculada com as variáveis criadas multiplicando pelas respectivas porcentagens na carteira
    rentabilidadeG2 = rentabilidade1*pAt1 + rentabilidade2*pAt2

    # para que os dados calculados fossem usados em outras funções, foram exportados com o 'return'
    return rentabilidade1, rentabilidade2, rentabilidadeG2, rendimentoDiario, pAt1, pAt2


#  foi criada uma função para calcular a rentablidade geral da carteira
def rentabilidadeGeral():
    # para acessar os dados necessários foi utilizado a função carteiraPublica() e carteiraPrivada() que retornam os dados necessários
    rentPublica = carteiraPublica()[2]
    rentPrivada = carteiraPrivada()[2]

    # para acessar os dados necessários foi utilizado a função carteiraPublica() e carteiraPrivada() que retornam os dados necessários
    rendimentoDiarioPublico = carteiraPublica()[3]
    rendimentoDiarioPrivado = carteiraPrivada()[3]

    # para calcular o rendimento diário total foi feito a média dos rendimentos diários das duas carteiras
    rendimentoToalDiário = (rendimentoDiarioPrivado + rendimentoDiarioPublico) / 2

    # para calcular o rendimento geral da carteira foi feito a média dos rendimentos gerais das carteiras
    geral = (rentPublica+rentPrivada)/2


    # para que os dados calculados fossem usados em outras funções, foram exportados com o 'return
    return geral, rendimentoDiarioPublico, rendimentoDiarioPrivado, rendimentoToalDiário

