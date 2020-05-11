"""
May 10, 2020
Find the Town Judge
"""


def findJudge(N, trust):
    if N == 1:
        return 1
    dic = {}
    for x, y in trust:
        if y in dic:
            dic[y] = dic[y] + 1
        else:
            dic[y] = 1
        if dic[y] == (N-1):
            for i, j in trust:
                if i == y:
                    return -1
            return y
    return -1
