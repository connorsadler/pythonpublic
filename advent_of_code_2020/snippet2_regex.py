import re

#
# regex help: https://docs.python.org/3/library/re.html
#

def banner(str):
    print("-" * 80)
    print(str)
    print("-" * 80)


#
# Check whether 'str' matches 'pattern'
# If it does, it must pass 'postMatchFunction' also
#
def checkPatternMatch(pattern, str, postMatchFunction = None):
    # searchResult = re.search(pattern, str)
    # print(f"  searchResult: {searchResult}")
    # matchResult = re.match(pattern, str)
    # print(f"  matchResult: {matchResult}")
    fullMatchResult = re.fullmatch(pattern, str)
    #print(f"  fullMatchResult: {fullMatchResult != None}")
    matchResult = fullMatchResult != None
    
    finalResult = matchResult
    # postMatchFunction?
    # Only called if 
    # - function is specified
    # - we got a POSITIVE match result
    secondaryResult = None
    if postMatchFunction is not None:
        if matchResult:
            secondaryResult = postMatchFunction(fullMatchResult)
            finalResult = secondaryResult

    return (finalResult, matchResult, secondaryResult)


#
# Tests the pattern on every "key" in valueToExpectedValidMap
# The value of each entry tells us True/False whether we expect that "key" to match the pattern
#
# postMatchFunction - optional
#                     If specified, only runs when the "key" value matches the regex
#                     i.e. the regex is the first "gate" and the postMatchFunction is the second "gate"
#                     The result value is only True if it passes BOTH gates
#
def testPattern(pattern, valueToExpectedValidMap, postMatchFunction = None):
    # find longest string in args, so we can format the output with padding to line all results up in a column
    ###strLengths = map(lambda x : len(x), args)
    maxStrLen = len(max(valueToExpectedValidMap.keys(), key=len))

    print(f"testPattern:  {pattern}")
    for str in valueToExpectedValidMap:
        # Call the checkPatternMatch to get the Final result, and intermediate results
        finalResult, matchResult, secondaryResult = checkPatternMatch(pattern, str, postMatchFunction)

        #
        # Format a line in a neat table with the results
        #

        matchResultStr = "Pass" if matchResult else "Fail"
        # Check expected result
        expectedResult = valueToExpectedValidMap[str]
        check = "AS EXPECTED" if finalResult==expectedResult else "*** UNEXPECTED RESULT ***"

        # secondary
        secondaryCheck = "n/a "
        if secondaryResult != None:
            secondaryCheck = "Pass" if secondaryResult else "Fail"

        # padding to line all results up in a column
        padding = " " * (maxStrLen - len(str))
        # result line
        print(f"  {str}{padding} ->   {matchResultStr} + {secondaryCheck}   -> {check}")



# matchResult must contain an int as group(0)
def checkIntInRange(matchResult, rangeFrom, rangeTo):
    #print(f"checkIntInRange: {matchResult}, {rangeFrom}, {rangeTo}")
    intFound = int(matchResult.group(0))
    return rangeFrom <= intFound <= rangeTo

def checkGroupInRange(matchResult, groupForValue, groupForRangeSelectionKey, rangeSelectionToRange):
    #print(f"checkGroupInRange: {matchResult}, {groupForValue}, {groupForRangeSelectionKey}")
    value = int(matchResult.group(groupForValue))
    rangeSelectionKey = matchResult.group(groupForRangeSelectionKey)
    #print(f"  value: {value}")
    #print(f"  rangeSelectionKey: {rangeSelectionKey}")

    rangeTuple = rangeSelectionToRange[rangeSelectionKey]
    return rangeTuple[0] <= value <= rangeTuple[1]


if __name__ == "__main__":
    banner("PATTERN 1A")
    testPattern("[0-9]{2}", {"a":False, "01":True, "012": False})
    # # banner("PATTERN 1B")
    # # testPattern("^[0-9]{2}$", "a", "01", "012")

    # banner("PATTERN 2A")
    # testPattern("(abc){2}", {"a":False, "abc":False, "abcabc":True} )

    # banner("PATTERN 3A")
    # testPattern("Mon|Tue|Wed|Thu", {"a":False, "Mon":True, "MonTue":False, "xMon":False, "Thu":True})



# if __name__ == "__main__":
#     #     byr (Birth Year) - four digits; at least 1920 and at most 2002.
#     banner("PATTERN DAY 4 - ITEM 1")
#     testPattern(
#         "[0-9]{4}",
#         {"a":False, "01":False, "1900": False, "1920": True, "1950":True, "2002":True, "2003":False},
#         lambda matchResult : checkIntInRange(matchResult, 1920,2002)
#     )

#     #     iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#     banner("PATTERN DAY 4 - ITEM 2")
#     testPattern(
#         "[0-9]{4}",
#         {"a":False, "01":False, "1900": False, "2009": False, "2010":True, "2012":True, "2020":True, "2021":False},
#         lambda matchResult : checkIntInRange(matchResult, 2010,2020)
#     )

#     #     eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#     banner("PATTERN DAY 4 - ITEM 3")
#     testPattern(
#         "[0-9]{4}",
#         {"a":False, "01":False, "1900": False, "2019":False, "2020":True, "2025":True, "2030":True, "2050":False, "20505":False },
#         lambda matchResult : checkIntInRange(matchResult, 2020,2030)
#     )

#     #     hgt (Height) - a number followed by either cm or in:
#     #         If cm, the number must be at least 150 and at most 193.
#     #         If in, the number must be at least 59 and at most 76.
#     banner("PATTERN DAY 4 - ITEM 4")
#     testPattern(
#         "([0-9]*)(cm|in)",
#         {"a":False, "01":False, 
#         "33cm": False, "150cm": True, "160cm": True, "193cm": True, "194cm": False,
#         "01in": False, "59in": True, "60in": True, "76in": True, "77in": False
#         },
#         lambda matchResult : checkGroupInRange(matchResult, 1, 2, { "cm":(150,193), "in":(59,76)  })
#     )

#     #     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#     banner("PATTERN DAY 4 - ITEM 5")
#     testPattern(
#         "#[0-9a-f]{6}",
#         {"a":False, "01":False, 
#         "#123": False, "#1234ff": True, "#1234fg": False, "#1234fff": False
#         },
#         None
#     )

#     #     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#     banner("PATTERN DAY 4 - ITEM 6")
#     testPattern(
#         "amb|blu|brn|gry|grn|hzl|oth",
#         {"a":False, "01":False, 
#         "amb": True, "blublu": False, "blu": True, "am": False, "grn": True
#         },
#         None
#     )

#     #     pid (Passport ID) - a nine-digit number, including leading zeroes.
#     banner("PATTERN DAY 4 - ITEM 7")
#     testPattern(
#         "[0-9]{9}",
#         {"a":False, "01":False, 
#         "000000000": True, "002004005": True, "00000000": False,
#         },
#         None
#     )

#     #     cid (Country ID) - ignored, missing or not.





# def checkFieldValueWithRegex(key, value):
#     print(f"checkFieldValueWithRegex: {key} = {value}")

#     if key == "byr":
#         #     byr (Birth Year) - four digits; at least 1920 and at most 2002.
#         return checkPatternMatch(
#             "[0-9]{4}", value,
#             lambda matchResult : checkIntInRange(matchResult, 1920,2002)
#         )

#     #     iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#     if key == "iyr":
#         return checkPatternMatch(
#             "[0-9]{4}", value,
#             lambda matchResult : checkIntInRange(matchResult, 2010,2020)
#         )

#     #     eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#     if key == "eyr":
#         return checkPatternMatch(
#             "[0-9]{4}", value,
#             lambda matchResult : checkIntInRange(matchResult, 2020,2030)
#         )

#     #     hgt (Height) - a number followed by either cm or in:
#     #         If cm, the number must be at least 150 and at most 193.
#     #         If in, the number must be at least 59 and at most 76.
#     if key == "hgt":
#         return checkPatternMatch(
#             "([0-9]*)(cm|in)", value,
#             lambda matchResult : checkGroupInRange(matchResult, 1, 2, { "cm":(150,193), "in":(59,76)  })
#         )

#     #     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#     if key == "hcl":
#         return checkPatternMatch(
#             "#[0-9a-f]{6}", value,
#             None
#         )

#     #     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#     if key == "ecl":
#         return checkPatternMatch(
#             "amb|blu|brn|gry|grn|hzl|oth", value,
#             None
#         )

#     #     pid (Passport ID) - a nine-digit number, including leading zeroes.
#     if key == "pid":
#         return checkPatternMatch(
#             "[0-9]{9}", value,
#             None
#         )

#     #     cid (Country ID) - ignored, missing or not.
#     if key == "cid":
#         return (True, True, True)

#     print("************ This should never happen - check your data!!!!!!!!!")
#     print("************ This should never happen - check your data!!!!!!!!!")
#     print("************ This should never happen - check your data!!!!!!!!!")
#     return (False, False, False)