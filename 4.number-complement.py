"""
May 4, 2020
Number Complement
- Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""


class Solution:
    def findComplement(self, num: int) -> int:
        inputBin = "{0:b}".format(num)
        result = []
        for i in list(inputBin):
            if i == '0':
                result.append(1)
            else:
                result.append(0)
        result = ''.join(str(e) for e in result)
        result = int(result, 2)
        return result
