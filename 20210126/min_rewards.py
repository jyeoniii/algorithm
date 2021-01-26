# https://www.algoexpert.io/questions/Min%20Rewards


def minRewards(scores):
    rewards = [1] * len(scores)
    for i in range(1, len(scores)):
        if scores[i - 1] < scores[i]:
            rewards[i] = rewards[i - 1] + 1

    for i in range(len(scores) - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i + 1] + 1, rewards[i])

    return sum(rewards)





