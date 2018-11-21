#!/usr/bin/env python3
import sys
import csv


def main():
    print(readFile("test.txt"));
    #print(readFile(sys.argv[1]));


def readFile(filename):
    with open(filename) as f:
        next(f);
        content = f.read().splitlines();
        return content;


if __name__ == "main":
    main();
    exit(0);
