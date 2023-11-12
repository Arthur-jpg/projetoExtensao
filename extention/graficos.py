
import matplotlib.pyplot as plt
from privados import ibov, cdb1, petr36
from rentabilidade import rentabilidadeGeral

Ibov = ibov()[3]
Cdi = cdb1()[3]
def ibov():
    IBov = Ibov
    plt.plot(IBov, '', color='g', label='IBOV')
    plt.title('Ibov')
    plt.legend()
    plt.show()

def ibovCarteiraT():
    
    rentTotal = rentabilidadeGeral()

    IBov = Ibov
    RentTotal = rentTotal[3]

    plt.plot(IBov, '', color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Carteira Total')
    plt.title('Ibov vs Carteira Total')
    plt.legend()
    plt.show()

def ibovPrivado():
    rentPrivado = rentabilidadeGeral()

    IBov = Ibov
    RentTotal = rentPrivado[2]

    plt.plot(IBov, '', color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Privado')
    plt.title('Ibov vs Carteira Privada')
    plt.legend()
    plt.show()

def ibovPublico():
    rentPublico = rentabilidadeGeral()

    IBov = Ibov
    RentTotal = rentPublico[1]

    plt.plot(IBov, '', color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Publico')
    plt.title('Ibov vs publica')
    plt.legend()
    plt.show()

def cdiCarteiraTotal():
    rentTotal = rentabilidadeGeral()

    RentTotal = rentTotal[3]
    cdi = Cdi
    plt.plot(cdi, '', color='r', label='CDI')
    plt.plot(RentTotal, color='b', label='Carteira Total')
    plt.title('CDI vs Carteira Total')
    plt.legend()
    plt.show()





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
    

