#!/usr/bin/env python

# =============================================================================
#  Two-armed Bandit
#
#  @author: Elisha Lai
#  @description: Program for computing the greedy choice, optimal reward,
#     optimal choice or greedy reward for a two-armed bandit
#  @version: 0.0.1 30/10/2016
# =============================================================================

import sys


# Returns the expectation for a win on the next pull of an arm
def expectation(a, b):
    return (a + 1) / float(a + b + 2)


# Returns the greedy strategy's choice for the next pull
def greedy_choice(a1, b1, a2, b2, d):
    expectation1 = expectation(a1, b1)
    expectation2 = expectation(a2, b2)

    if expectation1 >= expectation2:
        return 1
    else:
        return 2


# Returns the expectation for the total reward (sum of the rewards
# obtained over the next d pulls) if the optimal strategy is followed
def optimal_reward(a1, b1, a2, b2, d):
    optimal_rewards = [[[[0 for h in range(d + 1)] for g in range(d + 1)]
                       for f in range(d + 1)] for e in range(d + 1)]

    for i in range(d + 1):
        for e in range(d - i + 1):
            for f in range(d - (i + e) + 1):
                for g in range(d - (i + e + f) + 1):
                    h = d - (i + e + f + g)

                    if i == 0:
                        optimal_rewards[e][f][g][h] = 0
                    else:
                        expectation1 = expectation(a1 + e, b1 + f)
                        reward1 = \
                            expectation1 * (1 + optimal_rewards[e + 1][f][g][h]) + \
                            (1 - expectation1) * optimal_rewards[e][f + 1][g][h]
                        expectation2 = expectation(a2 + g, b2 + h)
                        reward2 = \
                            expectation2 * (1 + optimal_rewards[e][f][g + 1][h]) + \
                            (1 - expectation2) * optimal_rewards[e][f][g][h + 1]
                        optimal_rewards[e][f][g][h] = max(reward1, reward2)

    return optimal_rewards[0][0][0][0]


# Returns the optimal strategy's choice for the next pull
def optimal_choice(a1, b1, a2, b2, d):
    expectation1 = expectation(a1, b1)
    reward1 = \
        expectation1 * (1 + optimal_reward(a1 + 1, b1, a2, b2, d - 1)) + \
        (1 - expectation1) * optimal_reward(a1, b1 + 1, a2, b2, d - 1)
    expectation2 = expectation(a2, b2)
    reward2 = \
        expectation2 * (1 + optimal_reward(a1, b1, a2 + 1, b2, d - 1)) + \
        (1 - expectation2) * optimal_reward(a1, b1, a2, b2 + 1, d - 1)

    if reward1 >= reward2:
        return 1
    else:
        return 2


# Returns the expectation for the total reward (sum of the rewards
# obtained over the next d pulls) if the greedy strategy is followed
def greedy_reward(a1, b1, a2, b2, d):
    greedy_rewards = [[[[0 for h in range(d + 1)] for g in range(d + 1)]
                      for f in range(d + 1)] for e in range(d + 1)]

    for i in range(d + 1):
        for e in range(d - i + 1):
            for f in range(d - (i + e) + 1):
                for g in range(d - (i + e + f) + 1):
                    h = d - (i + e + f + g)

                    if i == 0:
                        greedy_rewards[e][f][g][h] = 0
                    else:
                        expectation1 = expectation(a1 + e, b1 + f)
                        expectation2 = expectation(a2 + g, b2 + h)

                        if expectation1 >= expectation2:
                            reward = \
                                expectation1 * (1 + greedy_rewards[e + 1][f][g][h]) + \
                                (1 - expectation1) * greedy_rewards[e][f + 1][g][h]
                        else:
                            reward = \
                                expectation2 * (1 + greedy_rewards[e][f][g + 1][h]) + \
                                (1 - expectation2) * greedy_rewards[e][f][g][h + 1]

                        greedy_rewards[e][f][g][h] = reward

    return greedy_rewards[0][0][0][0]


# Returns the number truncated to exactly three digits after the
# decimal point
def truncate_number(n):
    number_parts = str(n).split(".")

    if len(number_parts) == 1:
        return n
    else:
        integer_part = number_parts[0]
        fractional_part = number_parts[1]
        truncated_fractional_part = fractional_part[:3]
        truncated_number = ".".join([integer_part, truncated_fractional_part])
        return truncated_number


def main():
    values = []

    for line in sys.stdin:
        line = line.strip()
        s = line.split()[0]
        a1 = int(line.split()[1])
        b1 = int(line.split()[2])
        a2 = int(line.split()[3])
        b2 = int(line.split()[4])
        d = int(line.split()[5])

        if s == "GC":
            value = greedy_choice(a1, b1, a2, b2, d)
        elif s == "OR":
            value = truncate_number(optimal_reward(a1, b1, a2, b2, d))
        elif s == "OC":
            value = optimal_choice(a1, b1, a2, b2, d)
        else:
            value = truncate_number(greedy_reward(a1, b1, a2, b2, d))

        values.append(value)

    for value in values:
        print(value)


if __name__ == "__main__":
    main()
