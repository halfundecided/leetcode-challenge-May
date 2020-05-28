"""
May 28, 2020
Counting Bits
"""


def countBits(num):
    arr = [0]
    result = []

    def helper(arr):
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
                break
        if arr[0] == 0:
            arr.insert(0, 1)
        return arr
    for i in range(num+1):
        result.append(arr.count(1))
        helper(arr)
    return result
