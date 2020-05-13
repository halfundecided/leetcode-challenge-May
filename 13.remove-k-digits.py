"""
May 13, 2020
Remove K Digits 
***** Use STACK ****
"""


def removeKdigits(self, num, k):
    if len(num) <= k:
        return "0"

    stack = []
    for digit in num:
        while k > 0 and stack and int(stack[-1]) > int(digit):
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    result = ''.join(stack).lstrip('0') or '0'
    return result


##################### My Previous Answer #####################
#         # if length of num is same as k
#         if len(num) <= k:
#             return "0"
#         if k == 0:
#             return num
#         num = list(num)
#         num = [int(x) for x in num]

#         if num[1] == 0:
#             del num[0]
#             k = k - 1

#         for i in range(k):
#             maximum = max(num[:3])
#             maxind = num[:3].index(maximum)
#             del num[maxind]

#         # remove leading zeros
#         while num[0] == 0 and len(num) > 1:
#             num = num[1:]

#         num = [str(x) for x in num]

#         result = ''.join(num)
#         return result
