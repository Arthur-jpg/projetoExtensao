
import matplotlib.pyplot as plt
from privados import ibov, cdb1, petr36

def comp3():
    Ibov = ibov()[3]
    Cdb = cdb1()[3]
    Petr36 = petr36()[3]

    plt.plot(Ibov, '', color='g', label='IBOV')
    plt.plot(Cdb, '', color='r', label='CDB')
    plt.plot(Petr36, color='b', label='PETR36')
    plt.title('Ibov vs CDB vs Petr36')
    plt.legend()
    plt.show()

def comp2():
    Cdb = cdb1()[3]
    Petr36 = petr36()[3]

    plt.plot(Cdb, '', color='r', label='CDB')
    plt.plot(Petr36, color='b', label='PETR36')
    plt.title('Ibov vs CDB vs Petr36')
    plt.legend()
    plt.show()

def main():
    comp3()
    comp2()

if __name__ == "__main__":
    main()