#Wrapper module for Craps Monte Carlo Simulation
#Author: Ben Sakac <bisakac>


import stats
import random as r


def main():
    stats.n = eval(input("How many games of craps do you want to simulate? "))
    s = input("[To skip seeding, simply hit enter]\nEnter a seed for the random number generator: ")
    if len(s) == 0:
        r.seed()
    else:
        r.seed(s)
    for i in range(stats.n):
        stats.tallyResults()
    stats.xAxis()
    stats.yLists()
    stats.plotting()

if __name__ == '__main__':
    main()
