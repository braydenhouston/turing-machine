#!/usr/bin/env python3
import sys
import csv


def readFile(filename):
    obj = {}
    previous_from = ""
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if not row[0][0] == '#':
                # print(row)
                try:
                    if previous_from != row[0].strip() or not previous_from:
                        obj[row[0].strip()] = {}
                    if row[1]:
                        obj[row[0].strip()][row[1].strip()] = {'new_letter': row[2].strip(),
                                                               'direction': row[3].strip(),
                                                               'to': row[4].strip()
                                                               }
                except IndexError:
                    obj[row[0].strip()] = {'from': row[0].strip()}
                previous_from = row[0].strip()
    return obj


def runWord(obj, word):
    print(obj)
    if not word:
        print("No word provided")
        return False

    state = '1 Start'
    printHead = 0
    word = list(word)

    word[printHead] = obj[state][word[printHead]]["new_letter"]

    if obj[state][word[printHead]]["direction"] == 'R':
        printHead += 1
    elif obj[state][word[printHead]]["direction"] == 'L':
        printHead -= 1

    if printHead < 0:
        print("Print head moved before 0")
        return False

    print(word)

    return True


def main():
    obj = readFile('test.csv')
    # print(readFile(sys.argv[0]))
    # print(runWord(obj, sys.argv[1]))
    testword = "abba"
    if runWord(obj, testword):
        print("Accepted: " + testword)
    else:
        print("Rejected: " + testword)


if __name__ == "__main__":
    main()
    exit(0)
