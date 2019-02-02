import pandas as pd
import sys

if len(sys.argv) != 2:
    print("Usage: python main.py filePath")
    sys.exit()

def parseExcel(fileName):
    worksheet = pd.read_excel(fileName)
    return worksheet

def getSleepOldAvg(data):
    N, D = data.shape
    total = 0
    endIndex = N - 10
    for i in range(1, endIndex):
        total += data.at[i, "Sleep"]
    count = N - 11
    return total / float(count) 

def getSleepRecentAvg(data):
    N, D = data.shape
    total = 0
    for i in range(N - 10, N):
        total += data.at[i, "Sleep"] 
    return total / float(10)

def getDeepSleepOldAvg(data):
    N, D = data.shape
    total = 0
    endIndex = N - 10
    for i in range(1, endIndex):
        total += data.at[i, "Deep Sleep"]
    count = N - 11
    return total / float(count) 

def getDeepSleepRecentAvg(data):
    N, D = data.shape
    total = 0
    for i in range(N - 10, N):
        total += data.at[i, "Deep Sleep"] 
    return total / float(10)

def main():
    data = parseExcel(sys.argv[1])
    recentSleepAvg = getSleepRecentAvg(data)
    recentDeepSleepAvg = getDeepSleepRecentAvg(data)
    oldSleepAvg = getSleepOldAvg(data)
    oldDeepSleepAvg = getDeepSleepOldAvg(data)
    sleepDiff = oldSleepAvg / recentSleepAvg
    deepSleepDiff = oldDeepSleepAvg / recentDeepSleepAvg
    if oldSleepAvg > recentSleepAvg:
        sleepDiff = oldSleepAvg - recentSleepAvg
        percentage = 100 * (sleepDiff / oldSleepAvg)
        print("Your sleep decreased by " + str(round(percentage, 2)) + "% in the last 10 days")
    else:
        sleepDiff = recentSleepAvg - oldSleepAvg
        percentage = 100 * (sleepDiff / oldSleepAvg)
        print("Your sleep increased by " + str(round(percentage, 2)) + "% in the last 10 days")

    if oldDeepSleepAvg > recentDeepSleepAvg:
        sleepDiff = oldDeepSleepAvg - recentDeepSleepAvg
        percentage = 100 * (sleepDiff / oldDeepSleepAvg)
        print("Your deep sleep decreased by " + str(round(percentage, 2)) + "% in the last 10 days")
    else:
        sleepDiff = recentDeepSleepAvg - oldDeepSleepAvg
        percentage = 100 * (sleepDiff / oldDeepSleepAvg)
        print("Your deep sleep increased by " + str(round(percentage, 2)) + "% in the last 10 days")


if __name__ == '__main__':
    main()
