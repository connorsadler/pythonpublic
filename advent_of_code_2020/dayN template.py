
print("hello day 3")

print('__file__:    ', __file__)
f = open("advent_of_code_2020/dayN_input.txt", "r")

treeCount = 0
while True:
    line = f.readline()
    if line == "":
        break
    line = line.strip()
    print(f"line: {line}")

    # TODO: Parse every line
    
    # TODO: Check line
    if True:
        treeCount += 1

# Show final result, whatever it is
print(f"final result is treeCount: {treeCount}")
