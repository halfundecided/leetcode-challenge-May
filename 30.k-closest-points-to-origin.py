"""
May 30, 2020
K Closest Points to Origin
"""


def kClosest(points, K):
    if len(points) == K:
        return points
    pointDic = {}
    for i, elem in enumerate(points):
        distance = (elem[0] ** 2) + (elem[1] ** 2)
        pointDic[i] = distance
    sortedDic = {k: v for k, v in sorted(
        pointDic.items(), key=lambda item: item[1])}
    counter = 0
    result = []
    for key, value in sortedDic.items():
        if counter >= K:
            return result
        result.append(points[key])
        counter += 1
