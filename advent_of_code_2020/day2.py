
print("hello day 2")

print('__file__:    ', __file__)
f = open("advent_of_code_2020/day2_input.txt", "r")

# fileLines = f.readlines()
# for line in fileLines:
#     print(f"file line: {line}")

def parseLine(line):
    parts = line.split(":")
    return parts[0].strip(), parts[1].strip()

#
# A range from-> to e.g. from 2 to 5
#
class Range:
    def __init__(self, fromInt, toInt):
        self.fromInt = fromInt
        self.toInt = toInt
    
    def __str__(self):
        return f"Range[from: {self.fromInt} to: {self.toInt}]"

    def contains(self, value):
        # could use this instead: x < y < z
        # DOCS: Comparisons can be chained arbitrarily, e.g., x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).
        return self.fromInt <= value and value <= self.toInt

#
# A password policy
# The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
#
class PasswordPolicy:
    def __init__(self, range, requiredCharacter):
        self.range = range
        self.requiredCharacter = requiredCharacter

    def __str__(self):
        return f"PasswordPolicy[range: {self.range}, requiredCharacter: {self.requiredCharacter}]"

    def isPasswordValid(self, password):
        # OLD POLICY
        # # count number of occurences of "requiredCharacter" in password
        # # valid if the number of required characters is in our policy's range
        # foundRequiredCharacters = password.count(self.requiredCharacter)
        # return self.range.contains(foundRequiredCharacters)

        # NEW POLICY - Range from/to is actually the 1-based position of a character inside password
        #              Either one of those positions must contain our required character, but not both
        char1 = self.checkChar(password, self.range.fromInt)
        char2 = self.checkChar(password, self.range.toInt)
        return (char1 or char2) and not (char1 and char2)

    def checkChar(self, password, letterNumber):
        return password[letterNumber-1] == self.requiredCharacter


# str is like this: 2-5
def parseRange(str):
    parts = str.split("-")
    fromInt = int(parts[0])
    toInt = int(parts[1])
    return Range(fromInt, toInt)

# str is like this: 2-5 q
def parsePasswordPolicy(str):
    parts = str.split(" ")
    rangeStr = parts[0]
    requiredCharacter = parts[1]
    range = parseRange(rangeStr)
    return PasswordPolicy(range, requiredCharacter)

validCount = 0
while True:
    line = f.readline()
    if line == "":
        break
    line = line.strip()
    print(f"line: {line}")

    # Parse every line
    passwordPolicyStr, password = parseLine(line)

    passwordPolicy = parsePasswordPolicy(passwordPolicyStr)

    print(f"  passwordPolicy: {passwordPolicy}")
    print(f"  password: {password}")

    # Check whether the 'password' is valid for the 'passwordPolicy'
    if passwordPolicy.isPasswordValid(password):
        validCount += 1

# Show final result, whatever it is
print(f"final result is validCount: {validCount}")
