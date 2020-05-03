"""
May 3, 2020
Ransom Note
- Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false. 
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineList = list(magazine)
        noteList = list(ransomNote)
        copy = list(ransomNote)

        for letter in copy:
            if letter in magazineList:
                noteList.remove(letter)
                magazineList.remove(letter)
        if noteList == []:
            return True
        else:
            return False

        # @lc code=end
