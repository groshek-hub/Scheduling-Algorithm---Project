from Generator_danych_czasu_procesora import *  # Wszystkie funkcje i stałe można importować za pomocą *

# generator_czas_trwania()
# generator()
# generator_czas_przybycia()

wartosci = open("wartosci.txt", "r")  # odczytywanie pliku
wartosci_czas_przybycia = open("wartosci_czas_przybycia.txt", "r")  # odczytywanie pliku
wynik = open("wynik.txt", "w")  # plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana


def funkcja_FCFS():
    class Proces:  # W poniższej klasie zawieramy informacje o dwóch wartościach
        # klasa z funkcjami
        def __init__(self, czas_przybycia, czas_trwania):  # __init__ metoda przypisana w klasach Pythona
            # init -konstruktor w terminologi obiektowej
            # self - używane do reprezentowania instancji klasy. Używając słowa kluczowego „self”,
            # uzyskujemy dostęp do atrybutów i metod klasy w Pythonie
            self.czas_trwania = czas_trwania  # Jedna z nich to czas_przybycia (jest on z zakresu od 0 do 100)
            self.czas_przybycia = czas_przybycia  # Druga wartość to czas_trwania (i jest on z zakresu od 1 do 20)

        def pokaz_wartosci(self):
            print(str(self.czas_przybycia), str(self.czas_trwania))  # funkcja drukująca dwie wartości: czas_pryzbycia
            # oraz czas_trwania

    tablica_100 = []  # lista ktora zawiera obiekty z procesami
    kolejka = []  # kolejka, w której dodawane są z godnie, z czasem przyjścia procesy (lista)
    czas_oczekiwania = []  # lista czasu oczekiwania
    czas_wykonywania = []  # lista czasu wykonywania
    sr_czas_oczekiwania = 0  # wyzerowanie zmiennej
    sr_czas_wykonywania = 0  # wyzerowanie zmiennej

    for z in range(100):
        kolejka = []  # pusta lista - kolejka
        zsr_czas_oczekiwania = 0  # konkretnie w z-tej probie
        zsr_czas_wykonywania = 0  # konktrenie w z-tej probie
        for i in range(100):
            # metoda list.insert() wstawia element na listę o określonym indeksie
            tablica_100.insert(i, Proces(int(wartosci_czas_przybycia.readline()), int(wartosci.readline())))
            # i - indeks, druga część to element
            czas_oczekiwania.insert(i, 0)  # tablica jest uzupełniana 100 wartościami równymi 0
            czas_wykonywania.insert(i, 0)  # tablica jest uzupełniana 100 wartościami równymi 0

        for i in range(101):
            for j in range(100):  # dodajemy procesy do kolejki j by osiągnąć = 101, ponieważ kolejka musi mieć 100
                # elementów w liście
                if i >= tablica_100[j].czas_przybycia and (tablica_100[j] not in kolejka):
                    kolejka.append(tablica_100[j])  # metoda append dodaje elementy na koniec listy - kolejka(pozycja)

        for j in range(1, 100):  # teraz obliczamy czas oczekiwania j-tego procesu,
            # a robimy to na podstawie czasu przybycia poprzednich procesów
            # oraz samego j-tego procesu
            for m in range(0, j):
                czas_oczekiwania[j] += kolejka[m].czas_trwania - (
                        kolejka[m + 1].czas_przybycia - kolejka[m].czas_przybycia)

            if czas_oczekiwania[j] < 0:  # ujemny czas oczekiwania oznacza, że proces wykonał się szybciej od
                # przybycia kolejnego procesu
                czas_oczekiwania[j] = 0  # wyzerowanie

            sr_czas_oczekiwania += czas_oczekiwania[j]
            zsr_czas_oczekiwania += czas_oczekiwania[j]

        for j in range(100):  # w tym miejscu obliczany jest czas wykonywania j-tego procesu, jako sumy
            # czasów jego trwania (czas oczekiwania)
            czas_wykonywania[j] = czas_oczekiwania[j] + kolejka[j].czas_trwania

            sr_czas_wykonywania += czas_wykonywania[j]  # wykonane dla 100 prób
            zsr_czas_wykonywania += czas_wykonywania[j]  # wykonane dla pojedyńczej próby

        wynik.write(str(z + 1) + ".Lokalny średni czas oczekiwania: " + str(zsr_czas_oczekiwania / 100) + "ms. "
                    + "Lokalny średni czas wykonywania: " + str(zsr_czas_wykonywania / 100) + "ms.\n")
        # wypisanie do pliku wartości

    del tablica_100[:]  # usunięcie wszystkich elementów z listy tablica_100
    wynik.write("\nSrednia czasu oczekiwania wynosi: " + str(
        sr_czas_oczekiwania / 10000) + "ms. " + "Lokalny średni czas wykonywania: " + str(
        sr_czas_wykonywania / 10000) + "ms.\n")  # wypisanie do pliku wartości sr_czas_oczekiwania oraz
    # sr_czas_wykonywania, dzielenie przez 10000 by osiągnąć wynik w ms
    wartosci.close()  # zamykanie pliku
    wartosci_czas_przybycia.close()  # zamykanie pliku
    wynik.close()  # zamykanie pliku


funkcja_FCFS()  # wywołanie funkcji
