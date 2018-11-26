#!/usr/bin/env python3
import sys
import csv
import re


def readFile(filename):
    obj = {}
    previous_from = ""
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if not row[0][0] == '#':
                try:
                    if previous_from != row[0].strip() or not previous_from:
                        obj[row[0].strip()] = {}
                    if row[1]:
                        obj[row[0].strip()][row[1].strip()] = {'from': row[0].strip(),
                                                               'new_letter': row[2].strip(),
                                                               'direction': row[3].strip(),
                                                               'to': row[4].strip()
                                                               }
                except IndexError:
                    obj[row[0].strip()] = {'from': row[0].strip()}
                previous_from = row[0].strip()
    return obj


def runWord(obj, word):
    if not word:
        print("No word provided")
        return False

    print_head = step_counter = 0
    word = list(word)
    cur_state = halt_state = None

    for state in obj:
        if re.search(r'start', state, re.I):
            cur_state = state
        if re.search(r'halt', state, re.I):
            halt_state = state

    #print("Start:" + cur_state + "\nFinish:" + halt_state)

    while True:
        try:
            to_state = obj[cur_state][word[print_head]]["to"]
            if re.search(r'halt', to_state, re.I): # In case halt doesn't have it's own transition line
                return True
        except KeyError:
            if cur_state == halt_state:
                return True
            print(word[print_head] + " doesn't transition anywhere at state " + cur_state)
            return False

        new_letter = obj[cur_state][word[print_head]]["new_letter"]

        direction = obj[cur_state][word[print_head]]["direction"]

        # print("-------------------- Start Loop ------------------")
        # print("Print Head: " + str(print_head))
        # print("Word Letter: " + word[print_head])
        # print("Word Letter: " + word[print_head])
        # print("State: " + cur_state)
        # print(word)

        word[print_head] = new_letter

        if direction == 'R':
            print_head += 1
            # print("Print head moved right to " + str(print_head))
            if print_head + 1 > len(word):
                word.extend("_")

        elif direction == 'L':
            print_head -= 1
            # print("Print head moved left to " + str(print_head))
            if print_head < 0:
                print("Print head moved before 0")
                return False
        else:
            print(direction + " is not a valid direction at state " + cur_state)
            return False

        step_counter += 1

        if step_counter >= 500:
            print("This word exceeded 500 steps to process")
            return False

        cur_state = to_state

        if cur_state == halt_state:
            return True

        # print(word)
        # print("-------------------- End Loop ------------------")


def main():
    try:
        obj = readFile(sys.argv[1])

        if runWord(obj, sys.argv[2]):

            print("Accepted: " + sys.argv[2])
        else:
            print("Rejected: " + sys.argv[2])
    except IndexError:
        print("Rejected: Please provide a valid filename and word")


if __name__ == "__main__":
    main()
    exit(0)
