"""
May 1, 2020
First Bad Version 
- You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
- Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
- You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""


class Solution:
    def firstBadVersion(self, n):
        # l = list(range(1,n+1))
        # for i in l:
        #     if isBadVersion(i) == True:
        #         return i

        # while loop (the expression for the while loop is important too) --> while left < right
        # one case for when the function gives true
        # another case for when the function gives false

        # Binary Search Basic
        # left = 0
        # right = len(arr)
        # while (left < right):
        #     mid = left + (right-left)/2
        #     if arr[mid] == target:
        #         return mid
        #     elif arr[mid] > target:
        #         right = mid
        #     else:
        #         left = mid+1

        left = 1
        right = n
        while (left < right):
            mid = int(left + (right-left)/2)
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid+1
        return left


# @lc code=end
