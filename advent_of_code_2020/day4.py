
import day4_regex

print("hello day 4")

print('__file__:    ', __file__)
#f = open("advent_of_code_2020/day4_input_sample_part2.txt", "r")
f = open("advent_of_code_2020/day4_input.txt", "r")


requiredPassportFields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"
}


# line is something like: ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
def parseLine(line):
    result = {}
    entries = line.split(" ")
    for entry in entries:
        #print(f"entry: {entry}")
        entryParts = entry.split(":")
        key = entryParts[0]
        value = entryParts[1]
        result[key] = value
    return result

def checkValid(passportDict):
    print(f"CHECK VALID: {passportDict}")

    passportKeys = passportDict.keys()
    print(f"passportKeys: {passportKeys}")
    difference = requiredPassportFields - passportKeys
    print(f"difference: {difference}")

    # Passport is valid if either:
    # - all the required keys are present
    # - one key is missing and it is the "cid" key
    valid = len(difference) == 0 or (difference == { "cid" } )
    print(f"valid (phase 1): {valid}")

    # If valid, check fields valid
    if valid:
        valid = checkFieldValuesValid(passportDict)
        print(f"valid (phase 2): {valid}")

    return 1 if valid else 0


# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!
#
# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:
#
#     byr (Birth Year) - four digits; at least 1920 and at most 2002.
#     iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#     eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#     hgt (Height) - a number followed by either cm or in:
#         If cm, the number must be at least 150 and at most 193.
#         If in, the number must be at least 59 and at most 76.
#     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#     pid (Passport ID) - a nine-digit number, including leading zeroes.
#     cid (Country ID) - ignored, missing or not.
#
def checkFieldValue(key, value):
    print(f"checking key {key} = {value}")
    result = day4_regex.checkFieldValueWithRegex(key, value)
    # We're only interested in the OVERALL result, which comes first in the list
    result = result[0]
    print(f"result: {result}")
    return result


def checkFieldValuesValid(passportDict):
    print(f"checkFieldValuesValid: {passportDict}")
    for key in passportDict:
        value = passportDict[key]
        result = checkFieldValue(key, value)
        if not result:
            print(f"-> Failing on {key} = {value}")
            return False

    print(f"-> Passing!")
    return True



currentPassport = {}
validCount = 0
while True:
    line = f.readline()
    if line == "":
        if len(currentPassport) > 0:
            validCount += checkValid(currentPassport)
        break
    line = line.strip()
    print(f"line: {line}")

    if line == "":
        if len(currentPassport) > 0:
            validCount += checkValid(currentPassport)
            print("-------------------- BREAK --------------------")
            currentPassport = {}
    else:
        # Parse this line and add to current passport
        lineDict = parseLine(line)
        print(f"lineDict: {lineDict}")
        currentPassport.update(lineDict)
        print(f"currentPassport: {currentPassport}")

# Show final result
print(f"final result is validCount: {validCount}")
# Part 1 - correct answer is: 226
# Part 2 - correct answer is: 160
