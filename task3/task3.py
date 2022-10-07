from io import StringIO
import csv


def task(csvString):
    input = []
    rslt = []
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        input.append(row)


    realation1 = []
    realation2 = []
    realation3 = []
    realation4 = []
    realation5 = []
    def directR(idx, strg):
        for row in input:
            if row[idx] not in strg:
                strg.append(row[idx])

    directR(0, realation1)
    directR(1, realation2)

    def indirectlyR(idx1, idx2, strg):
        for row in input:
            for nextRow in input:
                if row[idx1] not in strg and nextRow[idx1] == row[idx2]:
                    strg.append(row[idx1])

    indirectlyR(0, 1, realation3)
    indirectlyR(1, 0, realation4)

    for row in input:
        for nextRow in input:
            if row[1] not in realation5 and nextRow[0] == row[0] and nextRow != row:
                realation5.append(row[1])

    rslt.append(realation1)
    rslt.append(realation2)
    rslt.append(realation3)
    rslt.append(realation4)
    rslt.append(realation5)
    return rslt


with open('graph.csv') as file:

    csvString = file.read()

    rslt = task(csvString)

    print(rslt)