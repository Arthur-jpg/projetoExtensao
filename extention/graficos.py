
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
    
    rentTotal = rentabilidadeGeral()[3]

    IBov = Ibov
    RentTotal = rentTotal

    plt.plot(IBov, '', color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Carteira Total')
    plt.title('Ibov vs Carteira Total')
    plt.legend()
    plt.show()

def ibovPrivado():
    rentPrivado = rentabilidadeGeral()[2]

    IBov = Ibov
    RentTotal = rentPrivado

    plt.plot(IBov, '', color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Privado')
    plt.title('Ibov vs Carteira Privada')
    plt.legend()
    plt.show()

def ibovPublico():
    rentPublico = rentabilidadeGeral()[1]

    IBov = Ibov
    RentTotal = rentPublico

    plt.plot(IBov, '', color='r', label='IBOV')
    plt.plot(RentTotal, color='b', label='Publico')
    plt.title('Ibov vs publica')
    plt.legend()
    plt.show()

def cdiCarteiraTotal():
    rentTotal = rentabilidadeGeral()[3]

    RentTotal = rentTotal
    cdi = Cdi
    plt.plot(cdi, '', color='r', label='CDI')
    plt.plot(RentTotal, color='b', label='Carteira Total')
    plt.title('CDI vs Carteira Total')
    plt.legend()
    plt.show()





def main():
    ibov()
    ibovCarteiraT()
    cdiCarteiraTotal()
    ibovPrivado()
    ibovPrivado()

main()