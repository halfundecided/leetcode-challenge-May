"""
May 8, 2020
Check If It Is a Straight Line
- You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""


def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True

    slope = [(coordinates[1][1]-coordinates[0][1]),
             (coordinates[1][0]-coordinates[0][0])]
    for i in range(len(coordinates)-1):
        checkSlope = [(coordinates[i+1][1] - coordinates[i][1]),
                      (coordinates[i+1][0] - coordinates[i][0])]
        if slope[0] == 0 and checkSlope[0] == 0:
            continue
        if slope[1] == 0 and checkSlope[1] == 0:
            continue
        if ((slope[0] == 0) ^ (checkSlope[0] == 0)):
            return False
        if ((slope[1] == 0) ^ (checkSlope[1] == 0)):
            return False
        if slope[1]/slope[0] != checkSlope[1]/checkSlope[0]:
            return False
    return True
