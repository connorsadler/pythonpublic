
print("hello day 3")

def doCount(horizSpeed, vertSpeed):
    f = open("advent_of_code_2020/day3_input.txt", "r")

    lineNum = 0
    colIdx = 0
    lineMult = 1
    treeCount = 0
    while True:
        # FIRST TIME - read one line always
        # SUBSEQUENT TIMES - read 'verical speed' lines
        if colIdx == 0:
            line = f.readline()
            lineNum += 1
        else:
            for index in range(vertSpeed):
                line = f.readline()
                lineNum += 1
                if line == "":
                    break
        if line == "":
            break

        line = line.strip()
        print(f"line {lineNum}")
        print(f"{line}")

        # Check line, except first one
        if colIdx == 0:
            print(f"first line so doing nothing, not checking any trees")
        else:
            if colIdx >= len(line):
                colIdx = colIdx - len(line)

            # mark underneath the line which char we're checking
            spaces = " " * colIdx
            print(f"{spaces}^")

            # Check position
            print(f"  colIdx: {colIdx}")
            ch = line[colIdx]
            if ch == "#":
                print("Hit")
                treeCount += 1

        colIdx += horizSpeed

    # Show final result, whatever it is
    print(f"final result is treeCount: {treeCount}")
    return treeCount

results = []
results.append(doCount(1,1))
results.append(doCount(3,1))
results.append(doCount(5,1))
results.append(doCount(7,1))
results.append(doCount(1,2))

print(f"results: {results}")
finalResult = 1
for i in results:
    finalResult *= i
print(f"final result: {finalResult}")
# Connor: My correct finalResult is: 5813773056
