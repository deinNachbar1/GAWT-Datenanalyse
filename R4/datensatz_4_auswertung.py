import csv
import math
import os

from scipy import stats

import matplotlib.pyplot as plt


def main():
    print("dateiname: ", end="")
    filename = input()

    if os.path.isfile(filename):
        print()

        with open(filename, "r") as file:
            reader = csv.reader(file, delimiter=';')

            x = ""
            y = ""

            werteX = []
            werteY = []
            for row in reader:

                if reader.line_num == 1:
                    print(row[0] + " | " + row[1])
                    print("------------------")
                    x = row[0]
                    y = row[1]
                else:
                    print(row[0] + " | " + row[1])
                    werteX.append(float(row[0].replace(",", ".")))
                    werteY.append(float(row[1].replace(",", ".")))

            print_rangliste(y, werteY)

            print()

            arith_mittelwert_x = print_arithmetische_mittel(x, werteX, 2)
            arith_mittelwert_y = print_arithmetische_mittel(y, werteY, 2)

            print()

            median_y = print_median(y, werteY)

            print()

            print_spannweite(y, werteY, 2)

            print()

            print_mittlere_abweichung_median(y, werteY, 2, median_y)

            print()

            varianz_x = print_stichprobenvarianz(x, werteX, 2, arith_mittelwert_x)
            varianz_y = print_stichprobenvarianz(y, werteY, 2, arith_mittelwert_y)

            print()

            print_variationskoeffizient(y, werteY, 2, arith_mittelwert_y, varianz_y)

            print()

            print_quantile(y, werteY)

            print()

            kovarianz = print_kovarianz(werteX, werteY, 2)

            print()

            print_korrelationskoeffizient(kovarianz, varianz_x, varianz_y, 2)

            print()

            print_modus(werteY, 1)

            print()

            plt.figure(figsize=(7, 7))
            plt.boxplot(sorted(werteY))
            plt.ylabel(y)
            plt.savefig("boxplot_" + str(y) + ".png")

            plt.figure(figsize=(5, 5))
            plt.scatter(werteX, werteY)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.savefig("scatterplot.png")

    else:
        print("datei existiert nicht!\n")
        main()


def print_rangliste(name, werte):
    print("\nRangliste " + name + ":")
    werte = sorted(werte)
    ranglisteFile = open("rangliste_" + name + ".csv", "w")
    for i in werte:
        print(str(i))
        ranglisteFile.write(str(i) + "\n")
    ranglisteFile.close()


def print_median(name, werte):
    werte = sorted(werte)

    if (len(werte) % 2) == 1:
        median_index = math.floor(len(werte) / 2)
        print("Median " + name + ": " + str(werte[median_index]))
        return werte[median_index]
    else:
        median_unten_index = int(len(werte) / 2)
        median_oben_index = int(len(werte) / 2) + 1
        print("Median " + name + ": " + str((1 / 2) * (werte[median_unten_index] + werte[median_oben_index])))
        return (1 / 2) * (werte[median_unten_index] + werte[median_oben_index])


def print_arithmetische_mittel(name, werte, nachkommastelle):
    werte = sorted(werte)

    mittelwert = 0
    for i in werte:
        mittelwert += i
    mittelwert = mittelwert / len(werte)

    print("arithmetische Mittelwert " + name + ": " + str(round(mittelwert, nachkommastelle)))
    return round(mittelwert, nachkommastelle)


def print_spannweite(name, werte, nachkommastelle):
    werte = sorted(werte)

    spannweite = round(float(werte[len(werte) - 1]) - float(werte[0]), nachkommastelle)

    print("Spannweite " + name + ": " + str(spannweite))


def print_mittlere_abweichung_median(name, werte, nachkommastelle, median):
    m_a_m = 0
    for i in werte:
        m_a_m = m_a_m + abs(median - i)
    m_a_m = m_a_m / len(werte)

    print("Mittlere Abweichung von Median " + name + ": " + str(round(m_a_m, nachkommastelle)))


def print_stichprobenvarianz(name, werte, nachkommastelle, mittelwert):
    varianz = 0
    for i in werte:
        varianz = varianz + (abs(mittelwert - i)) ** 2
    varianz = varianz / len(werte)

    print("Stichprobenvarianz " + name + ": " + str(round(varianz, nachkommastelle)))
    return varianz


def print_variationskoeffizient(name, werte, nachkommastellen, mittelwert, varianz):
    print("Variationskoeffizient " + name + ": " + str(round((math.sqrt(varianz) / mittelwert), nachkommastellen)))


def print_quantile(name, werte):
    werte = sorted(werte)
    p = 0.1
    n = len(werte)
    print(name + ": \n")

    # Dezile:
    print("Dezile:")
    while p <= 0.9:
        if (n * p) % 2 != 0:
            print("Q" + str(round(p, 1)) + ": " + str(werte[math.floor(n * p)]))
        else:
            print("Q" + str(round(p, 1)) + ": " + str((werte[n * p - 1] + werte[n * p]) / 2))
        p = p + 0.1
    print("\n")
    p = 0.25

    # Quartile
    print("Quartile:")
    while p <= 0.75:
        if (n * p) % 2 != 0:
            print("Q" + str(round(p, 2)) + ": " + str(werte[math.floor(n * p)]))
        else:
            print("Q" + str(round(p, 2)) + ": " + str((werte[n * p - 1] + werte[n * p]) / 2))
        p = p + 0.25
    print()


def print_kovarianz(werte1, werte2, nachkommastelle):
    mittelwert1 = 0
    mittelwert2 = 0

    for i in werte1:
        mittelwert1 += i
    for i in werte2:
        mittelwert2 += i

    mittelwert1 = mittelwert1 / len(werte1)
    mittelwert2 = mittelwert2 / len(werte2)

    kovarianz = 0

    for i in range(0, len(werte1)):
        kovarianz += (werte1[i] - mittelwert1) * (werte2[i] - mittelwert2)

    kovarianz = kovarianz / (len(werte2) - 1)

    print("Kovarianz: " + str(round(kovarianz, nachkommastelle)))
    return round(kovarianz, nachkommastelle)


def print_korrelationskoeffizient(kovarianz, varianz_x, varianz_y, nachkommastellen):
    korrelationskoeffizient = kovarianz / (math.sqrt(varianz_x) * math.sqrt(varianz_y))
    print("Korrelationskoeffizient: " + str(round(korrelationskoeffizient, nachkommastellen)))


def print_modus(wert, genauigkeit):
    modusArray = [0]

    for i in range(0, len(wert)):
        modusArray.append(round(wert[i], genauigkeit))

    modus = stats.mode(modusArray)

    print("Modus mit Werten auf " + str(genauigkeit) + " Nachkommastellen")
    print("Modus: " + str(modus[0]))
    print("Haeufigkeit: " + str(modus[1]))

    return modus


if __name__ == "__main__":
    main()
