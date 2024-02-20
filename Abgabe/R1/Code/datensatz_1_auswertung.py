# importieren der Benötigten Libraries
import csv
import math
import os
import matplotlib.pyplot as plt


# main funktion wird beim Start aufgerufen
def main():
    # eingabe des Dateinamens
    print("dateiname: ", end="")
    filename = input()

    # wenn Datei existiert
    if os.path.isfile(filename):
        print()

        # öffnen der Datei
        with open(filename, "r") as file:
            reader = csv.reader(file, delimiter=';')

            x = ""
            y = ""

            werteX = []
            werteY = []

            # lesen der einzelnen Zeilen
            for row in reader:
                # ausgabe der eingelesenden Datei
                if reader.line_num == 1:
                    print(row[0] + " | " + row[1])
                    print("------------------")
                    x = row[0]
                    y = row[1]
                else:
                    print(row[0] + " | " + row[1])
                    werteX.append(float(row[0].replace(",", ".")))
                    werteY.append(float(row[1].replace(",", ".")))

            # ausgabe der Rangliste
            print_rangliste(x, werteX)
            print_rangliste(y, werteY)

            print()
            # berechnung arithmetischen Mittel
            arith_mittelwert_x = print_arithmetische_mittel(x, werteX, 2)
            arith_mittelwert_y = print_arithmetische_mittel(y, werteY, 2)

            print()
            # berechnung Median
            median_x = print_median(x, werteX)
            median_y = print_median(y, werteY)

            print()
            # berechnung Spannweite
            print_spannweite(x, werteX, 2)
            print_spannweite(y, werteY, 2)

            print()
            # berechnung mittlere Abweichung
            print_mittlere_abweichung_median(x, werteX, 2, median_x)
            print_mittlere_abweichung_median(y, werteY, 2, median_y)

            print()
            # berechnung Stichprobenvarianz
            varianz_x = print_stichprobenvarianz(x, werteX, 2, arith_mittelwert_x)
            varianz_y = print_stichprobenvarianz(y, werteY, 2, arith_mittelwert_y)

            print()
            # berechnung Variationskoeffizient
            print_variationskoeffizient(x, werteX, 2, arith_mittelwert_x, varianz_x)
            print_variationskoeffizient(y, werteY, 2, arith_mittelwert_y, varianz_y)

            print()
            # berechnung Quantile
            print_quantile(x, werteX)
            print_quantile(y, werteY)

            print()
            # berechnung Kovarianz
            kovarianz = print_kovarianz(werteX, werteY, 2)

            print()
            # berechnung Korrelationskoeffizienten
            print_korrelationskoeffizient(kovarianz, varianz_x, varianz_y, 2)

            # zeichnen des Boxplots für Y
            plt.figure(figsize=(7, 7))
            plt.boxplot(sorted(werteY))
            plt.ylabel(y)
            plt.savefig("boxplot_" + str(y) + ".png")

            # zeichnen des Boxplots für X
            plt.figure(figsize=(7, 7))
            plt.boxplot(sorted(werteX))
            plt.ylabel(x)
            plt.savefig("boxplot_" + str(x) + ".png")

            # zeichnen des Scatter plots
            plt.figure(figsize=(5, 5))
            plt.scatter(werteX, werteY)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.savefig("scatterplot.png")

    else:
        # wenn Datei nicht existiert
        print("datei existiert nicht!\n")
        main()


def print_rangliste(name, werte):
    print("\nRangliste " + name + ":")
    # sortieren der Werte
    werte = sorted(werte)

    # erstellen der Ranglistendatei
    ranglisteFile = open("rangliste_" + name + ".csv", "w")

    # schreiben der Rangliste
    for i in werte:
        print(str(i))
        ranglisteFile.write(str(i) + "\n")
    ranglisteFile.close()


def print_median(name, werte):
    # sortieren der Werte
    werte = sorted(werte)

    # wenn es eine ungerade Anzahl an Werten ist
    if (len(werte) % 2) == 1:
        # berechnen des Medians
        median_index = math.floor(len(werte) / 2)
        print("Median " + name + ": " + str(werte[median_index]))
        return werte[median_index]
    # wenn es eine gerade Anzahl an Werten ist
    else:
        # berechnung der Oberen und Unteren Medians
        median_unten_index = int(len(werte) / 2)
        median_oben_index = int(len(werte) / 2) + 1
        # berechnung des Mittelwertes aus Ober und Unter Median
        print("Median " + name + ": " + str((werte[median_unten_index] + werte[median_oben_index]) / 2))
        return (1 / 2) * (werte[median_unten_index] + werte[median_oben_index])


def print_arithmetische_mittel(name, werte, nachkommastelle):
    werte = sorted(werte)

    # berechnung des Mittels
    mittelwert = 0
    for i in werte:
        mittelwert += i
    mittelwert = mittelwert / len(werte)

    # ausgabe
    print("arithmetische Mittelwert " + name + ": " + str(round(mittelwert, nachkommastelle)))
    return round(mittelwert, nachkommastelle)


def print_spannweite(name, werte, nachkommastelle):
    werte = sorted(werte)

    # berechnung der Spannweite
    spannweite = round(float(werte[len(werte) - 1]) - float(werte[0]), nachkommastelle)

    print("Spannweite " + name + ": " + str(spannweite))


def print_mittlere_abweichung_median(name, werte, nachkommastelle, median):
    m_a_m = 0

    # berechnung der abweichung
    for i in werte:
        m_a_m = m_a_m + abs(median - i)
    m_a_m = m_a_m / len(werte)

    print("Mittlere Abweichung von Median " + name + ": " + str(round(m_a_m, nachkommastelle)))


def print_stichprobenvarianz(name, werte, nachkommastelle, mittelwert):
    varianz = 0
    # berechnung der Varianz
    for i in werte:
        varianz = varianz + (abs(mittelwert - i)) ** 2
    varianz = varianz / len(werte)
    # ausgabe
    print("Stichprobenvarianz " + name + ": " + str(round(varianz, nachkommastelle)))
    return varianz


def print_variationskoeffizient(name, werte, nachkommastellen, mittelwert, varianz):
    print("Variationskoeffizient " + name + ": " + str(round((math.sqrt(varianz) / mittelwert), nachkommastellen)))


def print_quantile(name, werte):
    werte = sorted(werte)
    # n p berechnung
    p = 0.1
    n = len(werte)
    print(name + ": \n")

    # Dezile
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
    quartil_25 = 0
    quartil_75 = 0
    while p <= 0.75:
        # wenn n · p ungerade ist
        if (n * p) % 2 != 0:
            print("Q" + str(round(p, 2)) + ": " + str(werte[math.floor(n * p)]))
            if p == 0.25:
                quartil_25 = werte[math.floor(n * p)]
            elif p == 0.75:
                quartil_75 = werte[math.floor(n * p)]
        # wenn n · p gerade ist
        else:
            print("Q" + str(round(p, 2)) + ": " + str((werte[n * p - 1] + werte[n * p]) / 2))
            if p == 0.25:
                quartil_25 = ((werte[n * p - 1] + werte[n * p]) / 2)
            elif p == 0.75:
                quartil_75 = ((werte[n * p - 1] + werte[n * p]) / 2)
        p = p + 0.25
    print()
    print("Quartilsabstand: " + str(round((quartil_75 - quartil_25), 2)))


def print_kovarianz(werte1, werte2, nachkommastelle):
    mittelwert1 = 0
    mittelwert2 = 0

    # berechnung der mittelwerte
    for i in werte1:
        mittelwert1 += i
    for i in werte2:
        mittelwert2 += i

    mittelwert1 = mittelwert1 / len(werte1)
    mittelwert2 = mittelwert2 / len(werte2)

    kovarianz = 0

    # berechnung der kovarianz
    for i in range(0, len(werte1)):
        kovarianz += (werte1[i] - mittelwert1) * (werte2[i] - mittelwert2)

    kovarianz = kovarianz / (len(werte2) - 1)

    print("Kovarianz: " + str(round(kovarianz, nachkommastelle)))
    return round(kovarianz, nachkommastelle)


def print_korrelationskoeffizient(kovarianz, varianz_x, varianz_y, nachkommastellen):
    korrelationskoeffizient = kovarianz / (math.sqrt(varianz_x) * math.sqrt(varianz_y))
    print("Korrelationskoeffizient: " + str(round(korrelationskoeffizient, nachkommastellen)))


if __name__ == "__main__":
    main()
