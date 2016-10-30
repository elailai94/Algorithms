#!/usr/bin/env python

# =============================================================================
#  Computeregex
#
#  @description: Program for computing regular expressions for B(n, k)
#  @author: Elisha Lai
#  @version: 0.0.1 08/10/2016
# =============================================================================

import math
import sys


# Returns the string concatenation of x with y
def concat(x, y):
    return x + y


# Returns the regular expression for B(n, k)
def compute_regex(n, k):
    if k == 0:
        return n * "0"
    elif n == k:
        return n * "1"
    elif n < k:
        return ""
    else:
        left_subregex_n = int(math.floor(n / 2.0))
        right_subregex_n = int(math.ceil(n / 2.0))
        ret_regex = ""
        num_of_subregexes = 0

        for i in range(k + 1):
            left_subregex = compute_regex(left_subregex_n, i)
            right_subregex = compute_regex(right_subregex_n, k - i)

            if left_subregex != "" and right_subregex != "":
                merged_regex = concat(left_subregex, right_subregex)

                if num_of_subregexes > 0:
                    merged_regex = concat("+", merged_regex)

                ret_regex = concat(ret_regex, merged_regex)
                num_of_subregexes += 1

        if num_of_subregexes > 1:
            ret_regex = concat("(", ret_regex)
            ret_regex = concat(ret_regex, ")")

        return ret_regex


def main():
    regexes = []

    for line in sys.stdin:
        line = line.strip()
        n = int(line.split()[0])
        k = int(line.split()[1])
        regex = compute_regex(n, k)
        if regex.startswith("(") and regex.endswith(")"):
            regex = regex[1:-1]
        regexes.append(regex)

    for regex in regexes:
        print(regex)


if __name__ == "__main__":
    main()
