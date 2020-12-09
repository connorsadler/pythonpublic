
# can't read from URL as it needs you to login
#import urllib.request
#url = "https://adventofcode.com/2020/day/1/input"
#filecontents = urllib.request.urlopen(url)

print("hello day 1")

f = open("advent_of_code_2020/day1_input.txt", "r")
fileLines = f.readlines()

# strip every entry and convert to int
fileLinesAsInts = list(map(lambda l: int(l.strip()), fileLines))


def findNumbersWhichSumTo(requiredSum, numberCount):
    prefix = "----" * (5-numberCount)
    print(f"{prefix}findNumbersWhichSumTo: {requiredSum} ... {numberCount}")

    if numberCount == 1:
        matchingEntryPresent = requiredSum in fileLinesAsInts
        if matchingEntryPresent:
            print(f"{prefix}Found search number:")
            print(f"{prefix}  requiredSum: {requiredSum}")
            return [requiredSum]
        else:
            return None

    # iterate every int and recurse for the remainder
    for currentNum in fileLinesAsInts:
        print(f"{prefix}currentNum: {currentNum}")
        newRequiredSum = requiredSum - currentNum
        subResult = findNumbersWhichSumTo(newRequiredSum, numberCount-1)
        if subResult != None:
            return [currentNum] + subResult

    print(f"{prefix}Could not find requiredSum: {requiredSum}")
    return None


resultList = findNumbersWhichSumTo(2020, 3)
print(f"resultList: {resultList}")

result = 1
for r in resultList:
    result *= r

print(f"final result: {result}")


