import random  # potrzebne do uzycia choice() i randint()
from numpy import random  # generowanie losowych liczb z pomocą bilbioteki numpy


def generator():
    wartosci = open("wartosci.txt", "w")  # plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana
    for x in range(
            100):  # range()generuje liczby całkowite między podaną liczbą całkowitą początkową a liczbą całkowitą
        # zatrzymania , tj. Zwraca obiekt zakresu(100).
        wartosci.write(str(random.randint(1,
                                          21)) + "\n")  # wypisywane sa wartości od 1-20, random.randint() zwraca
        # losowy element całkowity wybrany z danego przedziału
    wartosci.close()  # zamykanie pliku


def numpy_generator_1():
    wartosci = open("wartosci.txt", "w")  # plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana
    for x in range(
            100):  # range()generuje liczby całkowite między podaną liczbą całkowitą początkową a liczbą całkowitą
        # zatrzymania , tj. Zwraca obiekt zakresu(100).
        wartosci.write(str(random.choice([2, 4, 6, 8, 10], p=[0.02, 0.08, 0.4, 0.2,
                                                              0.35])) + "\n")  # random.choice() zwraca element
        # losowo wybrany z określonej sekwencji
    wartosci.close()  # zamykanie pliku


def numpy_generator_2():
    wartosci = open("wartosci.txt", "w")  # plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana
    for x in range(
            100):  # range()generuje liczby całkowite między podaną liczbą całkowitą początkową a liczbą całkowitą
        # zatrzymania , tj. Zwraca obiekt zakresu(100).
        wartosci.write(str(random.choice([1, 3, 5, 9, 11], p=[0.02, 0.08, 0.4, 0.2,
                                                              0.35])) + "\n")  # random.choice() zwraca element
        # losowo wybrany z określonej sekwencji
    wartosci.close()  # zamykanie pliku


def normalna_dystr():
    wartosci = open("wartosci.txt", "w")  # plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana
    for x in range(
            10000):  # range()generuje liczby całkowite między podaną liczbą całkowitą początkową a liczbą całkowitą
        # zatrzymania , tj. Zwraca obiekt zakresu(10000).
        wartosci.write(str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                         p=[0.01, 0.045, 0.1, 0.16, 0.2, 0.2, 0.16, 0.1, 0.045,
                                            0.01])) + "\n")  # random.choice() zwraca element losowo wybrany z
        # określonej sekwencji
    wartosci.close()  # zamykanie pliku


generator()  # tutaj wybieramy sposób generowania strony i wywołujemy ową funkcję
