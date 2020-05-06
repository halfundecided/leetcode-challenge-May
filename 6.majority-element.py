"""
May 6, 2020
Majority Element
- Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
- You may assume that the array is non-empty and the majority element always exist in the array.
"""
import math


def majorityElement(nums):
     dict = {}
      length = math.floor(len(nums)/2)
       for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        for key, value in dict.items():
            if value > length:
                return key
