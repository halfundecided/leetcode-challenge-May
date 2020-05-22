"""
May 22, 2020
Sort Characters By Frequency
"""


def frequencySort(s):
    seen = {}
    result = ''
    # Construct a dictionary char - freq pair
    for i in range(len(s)):
        if s[i] in seen:
            seen[s[i]] += 1
        else:
            seen[s[i]] = 1

    # Sort a dictionary by value
    sortedTuples = sorted(seen.items(), reverse=True, key=lambda x: x[1])
    for i in sortedTuples:
        for j in range(i[1]):
            result += i[0]
    return result


"""
Python sorted() function - Timsort

sorted(iterable, key=None, reverse=False)
iterable: A sequence (string, tuple, list) or collection(set, dictionary, frozen set) or any other iterator
reverse(Optional): If True, the sorted list is reversed(in descending order).
key(Optional): A function that serves a key for the sort comparison. 
"""
