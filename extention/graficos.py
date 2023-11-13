
import matplotlib.pyplot as plt
from privados import ibov, cdb1, petr36
from rentabilidade import rentabilidadeGeral

# foram criadas variáveis globais para serem usadas em todas as funções, retornando a rentabilidade média diária do Ibovspa e CDI respectivamente
Ibov = ibov()[3]
Cdi = cdb1()[3]

# foi criado uma função para gerar um gráfico específico necessário
def ibov():
    # para ter a rentabilidade geral do ibovespa a função ibov() foi chamada novamente em forma de váriavel  
    IBov = Ibov

    # as devidas funções necessárias para rodar o gráfico foram postas
    # a função plot, gera o gráfico
    plt.plot(IBov, '', color='g', label='IBOV')
    # a função title mostra o título do gráfico
    plt.title('Ibov')
    # a função legend mostra a legenda do gráfico
    plt.legend()
    # a função show mostra o gráfico
    plt.show()

# foi criado uma função para gerar um gráfico específico necessário
def ibovCarteiraT():
    # para acessar a rentabilidade geral da carteira foi utilizado a função rentabilidadeGeral() importada de outro aquivo
    rentTotal = rentabilidadeGeral()

    # para ter a rentabilidade geral do ibovespa a função ibov() foi chamada novamente em forma de váriavel
    IBov = Ibov

    # Para ter acesso a rentabilidade total foi usado o index [3] referente ao dado necessário
    RentTotal = rentTotal[3]

    # as devidas funções necessárias para rodar o gráfico foram postas
    # a função plot, gera o gráfico
    plt.plot(IBov, color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Carteira Total')
    # a função title mostra o título do gráfico
    plt.title('IBOV vs Carteira Total')
    # a função legend mostra a legenda do gráfico
    plt.legend()
    # a função show mostra o gráfico
    plt.show()


# foi criado uma função para gerar um gráfico específico necessário
def ibovPrivado():

    # para acessar a rentabilidade geral da carteira foi utilizado a função rentabilidadeGeral() importada de outro aquivo
    rentPrivado = rentabilidadeGeral()

    # para ter a rentabilidade geral do ibovespa a função ibov() foi chamada novamente em forma de váriavel
    IBov = Ibov

    # Para ter acesso a rentabilidade diária da carteira privada foi usado o index [2] referente ao dado necessário
    RentTotal = rentPrivado[2]

    # as devidas funções necessárias para rodar o gráfico foram postas
    # a função plot, gera o gráfico
    plt.plot(IBov, color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Privado')
    # a função title mostra o título do gráfico
    plt.title('IBOV vs Carteira Privada')
    # a função legend mostra a legenda do gráfico
    plt.legend()
    # a função show mostra o gráfico
    plt.show()

# foi criado uma função para gerar um gráfico específico necessário
def ibovPublico():
    # para acessar a rentabilidade geral da carteira foi utilizado a função rentabilidadeGeral() importada de outro aquivo
    rentPublico = rentabilidadeGeral()

    # para ter a rentabilidade geral do ibovespa a função ibov() foi chamada novamente em forma de váriavel
    IBov = Ibov

    # Para ter acesso a rentabilidade diária da carteira pública foi usado o index [1] referente ao dado necessário
    RentTotal = rentPublico[1]

    # as devidas funções necessárias para rodar o gráfico foram postas
    # a função plot, gera o gráfico
    plt.plot(IBov, color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Publico')
    # a função title mostra o título do gráfico
    plt.title('IBOV vs Publica')
    # a função legend mostra a legenda do gráfico
    plt.legend()
    # a função show mostra o gráfico
    plt.show()

# foi criado uma função para gerar um gráfico específico necessário
def cdiCarteiraTotal():
    # para acessar a rentabilidade geral da carteira foi utilizado a função rentabilidadeGeral() importada de outro aquivo
    rentTotal = rentabilidadeGeral()
    # Para ter acesso a rentabilidade total foi usado o index [3] referente ao dado necessário
    RentTotal = rentTotal[3]

    cdi = Cdi
    # as devidas funções necessárias para rodar o gráfico foram postas
    # a função plot, gera o gráfico
    plt.plot(cdi, color='r', label='CDI')
    plt.plot(RentTotal, color='b', label='Carteira Total')
    #   a função title mostra o título do gráfico
    plt.title('CDI vs Carteira Total')
    #   a função legend mostra a legenda do gráfico
    plt.legend()
    # a função show mostra o gráficov
    plt.show()





# foi criada uma função main (função geral) para rodar todos os gráficos, nessa função contém funções print() 
# para deixar mais organizada a saída de dados do no CMD
def main2():
    print('GRÁFICOS')
    print()
    print('Gráfico Ibov')   
    ibov()
    print('Ibov vs Carteira Total')    
    ibovCarteiraT()
    print('CDI vs Carteira Total')
    cdiCarteiraTotal()
    print('Ibov vs Carteira Privada')
    ibovPrivado()
    print('Ibov vs Carteira Pública')
    ibovPublico()
    

