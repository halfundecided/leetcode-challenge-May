"""
May 5, 2020
First Unique Character in a String
- Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1. 
"""


def firstUniqChar(s):
    dict = {}
    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = 1
        else:
            dict[s[i]] += 1
    for i in range(len(s)):
        if dict.get(s[i]) == 1:
            return i

    return -1
