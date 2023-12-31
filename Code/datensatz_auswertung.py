import csv
import math


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
    else:
        median_unten_index = int(len(werte) / 2) - 1
        print("unterer Median " + name + ": " + str(werte[median_unten_index]))
        median_oben_index = int(len(werte) / 2)
        print("oberer Median " + name + ": " + str(werte[median_oben_index]))


def print_arithmetische_mittel(name, werte, nachkommastelle):
    werte = sorted(werte)

    mittelwert = 0
    for i in werte:
        mittelwert += i
    mittelwert = mittelwert / len(werte)

    print("arithmetische Mittelwert " + name + ": " + str(round(mittelwert, nachkommastelle)))


def print_spannweite(name, werte, nachkommastelle):
    werte = sorted(werte)

    spannweite = round(float(werte[len(werte) - 1]) - float(werte[0]), nachkommastelle)

    print("Spannweite " + name + ": " + str(spannweite))


def main():
    print("dateiname: ")
    filename = input()

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

        print_rangliste(x, werteX)
        print_rangliste(y, werteY)

        print()

        print_median(x, werteX)
        print_median(y, werteY)

        print()

        print_arithmetische_mittel(x, werteX, 3)
        print_arithmetische_mittel(y, werteY, 3)

        print()

        print_spannweite(x, werteX, 3)
        print_spannweite(y, werteY, 3)


if __name__ == "__main__":
    main()
