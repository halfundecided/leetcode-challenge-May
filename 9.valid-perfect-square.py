"""
May 9, 2020
Valid Perfect Square
- Given a positive integer num, write a function which returns True if num is a perfect square else False.
- Note: Do not use any built-in library function such as sqrt.
"""


def isPerfectSquare(num):
    if num == 1:
        return True
    i = 1
    j = int(num/2)
    while i <= j:
        mid = int(i + (j - i) / 2)  # (i + j)/2
        if mid*mid == num:
            return True
        elif mid*mid > num:
            j = mid - 1
        else:
            i = mid + 1
    return False
