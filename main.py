#!/usr/bin/env python3
import sys
import csv


def readFile(filename):
    obj = dict()
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if not row[0][0] == '#':
                # print(row)
                try:
                    if row[1]:
                        obj[row[0].strip()][row[0].strip()] = {'new_letter': row[2].strip(),
                                                               'direction': row[3].strip(),
                                                               'to': row[4].strip()
                                                              }
                except IndexError:
                    obj[row[0].strip()] = {'from': row[0].strip()}
    return obj


def runWord(obj, word):
    if not word:
        print("No word provided")
        return False
    printHead = obj['1 Start']
    return True


def main():
    obj = readFile('test.csv')
    # print(readFile(sys.argv[0]))
    # print(runWord(obj, sys.argv[1]))
    testword = ""
    if runWord(obj, testword):
        print("Accepted: " + testword)
    else:
        print("Rejected: " + testword)


if __name__ == "__main__":
    main()
    exit(0)
