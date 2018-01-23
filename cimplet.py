#!/usr/bin/env python3

import pickle
import sys
import os

class Person:
    def __init__(self, name):
        self.name = name
        self.income = 0
        self.outcome = 0
        self.total = 0
    def addIncome(self, value):
        self.income += value
        self.total -= value
    def getIncome(self):
        return(self.income)
    def addOutcome(self, value):
        self.outcome += value
        self.total += value
    def getOutcome(self):
        return(self.outcome)
    def getTotal(self):
        return(self.total)
    def getName(self):
        return(self.name)

def printStatus(persons):
    print("Persons status:")
    for person in persons:
        print("  Name: ", person.getName())
        print("  Income: ", person.getIncome())
        print("  Outcome: ", person.getOutcome())
        print("  Total: ", person.getTotal())
        print()

def addValues(persons):
    print("Adding values:")
    for person in persons:
        income = float(input("  Add Income for " + person.getName() + ": "))
        person.addIncome(income)
        outcome = float(input("  Add Outcome for " + person.getName() + ": "))
        person.addOutcome(outcome)

def printHelp():
    print("Help message:")
    print("  p|P for print persons status")
    print("  a|A for add persons income and outcome")
    print("  h|H for help")

def main(persons):
    print("Welcome to Cimplet balance app v0.1.")

    while True:
        key = input("Enter your command (h for help): ")
        if (key in ['p', 'P']): printStatus(persons)
        if (key in ['a', 'A']): addValues(persons)
        if (key in ['h', 'H']): printHelp()


if __name__ == "__main__":
    try:
        try:
            persons = pickle.load( open( "cimplet.p", "rb" ) )
        except:
            persons = [Person("Mare"), Person("Luce"), Person("Stef")]
        main(persons)
    except KeyboardInterrupt:
        pickle.dump( persons, open( "cimplet.p", "wb" ) )
        print('Goodbye.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
