#Module with functions to record stats about games of craps and plot probabilities of a win or loss for n rolls
#Author: Ben Sakac <bisakac>


import craps as craps


#Global variable list
n = 0
xList = []
winList = []
lossList = []
plotWins = []
plotLoss = []


#Gathers results for n amount of simulated craps games
def tallyResults():
    global n, playerWins, xList, winList, lossList
    craps.playOneGame()
    if craps.playerWins is True:
        winList.append(craps.numRolls)
    elif craps.playerWins is False:
        lossList.append(craps.numRolls)


#Generates list for x-axis of plot
def xAxis():
      global n, playerWins, xList, winList, lossList
      winMax = max(winList)
      lossMax = max(lossList)
      if winMax > lossMax:
          for i in range(winMax):
                xList.append(i + 1)
      elif winMax < lossMax:
            for i in range(lossMax):
                xList.append(i + 1)
      elif winMax == lossMax:
            for i in range(winMax):
                xList.append(i + 1)


def yLists():
    global xList, winList, lossList, plotWins, plotLoss
    for i in xList:
        winCount = winList.count(i) / n
        lossCount = lossList.count(i) / n
        plotWins.append(winCount)
        plotLoss.append(lossCount)


def plotting():
    import matplotlib.pyplot as plt
    global xList, plotWins, plotLoss
    plt.plot(xList, plotWins, xList, plotLoss)
    plt.suptitle("Craps Monte Carlo Simulation by Ben Sakac")
    plt.xlabel("Number of Throws")
    plt.ylabel("Percentage of Games Won or Lost per Number of Rolls \n Wins in Blue | Losses in Orange")
    plt.autoscale()
    plt.show()
