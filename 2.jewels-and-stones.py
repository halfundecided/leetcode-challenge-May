"""
May 2, 2020
Jewels and Stones 
- You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
- The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        listOfJewel = list(J)
        stones = list(S)
        numOfJewel = 0
        for i in listOfJewel:
            for j in stones:
                if i == j:
                    numOfJewel += 1

        return numOfJewel

# @lc code=end
