#!/usr/bin/env python

# =============================================================================
#   Computeregex
#
#   @description: Program for computing regular expressions for B(n, k)
#   @author: ahlai
#   @version: 0.0.1 08/10/2016
# =============================================================================

import math
import sys


# Returns the string concatenation of x with y
def concat(x, y):
    return x + y


# Returns the regular expression for B(n, k)
def computeregex(n, k):
    if k == 0:
        return n * "0"
    elif n == k:
        return n * "1"
    elif n < k:
        return ""
    else:
        leftsubregexn = int(math.floor(n / 2.0))
        rightsubregexn = int(math.ceil(n / 2.0))
        retregex = ""
        numofsubregexes = 0

        for i in range(k + 1):
            leftsubregex = computeregex(leftsubregexn, i)
            rightsubregex = computeregex(rightsubregexn, k - i)

            if leftsubregex != "" and rightsubregex != "":
                mergedregex = concat(leftsubregex, rightsubregex)

                if numofsubregexes > 0:
                    mergedregex = concat("+", mergedregex)

                retregex = concat(retregex, mergedregex)
                numofsubregexes += 1

        if numofsubregexes > 1:
            retregex = concat("(", retregex)
            retregex = concat(retregex, ")")

        return retregex


def main():
    regexes = []

    for line in sys.stdin:
        line = line.strip()
        n = int(line.split()[0])
        k = int(line.split()[1])
        regex = computeregex(n, k)
        if regex.startswith("(") and regex.endswith(")"):
            regex = regex[1:-1]
        regexes.append(regex)

    for regex in regexes:
        print(regex)


if __name__ == '__main__':
    main()
