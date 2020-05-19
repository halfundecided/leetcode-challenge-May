"""
May 18, 2020
Permutation in String 
"""
from collections import Counter


def checkInclusion(s1, s2):
    table1 = Counter(s1)
    for i in range(len(s2)):
        substr = s2[i:i+len(s1)]
        table2 = Counter(substr)
        if table1 == table2:
            return True
    return False


####### FIRST APPROACH ######
#         table = {}

#         def helper(substr):
#             helper_table = {}
#             for i in range(len(substr)):
#                 if substr[i] in helper_table:
#                     helper_table[substr[i]] += 1
#                 else:
#                     helper_table[substr[i]] = 1
#             for key in table:
#                 if key not in helper_table or table[key] != helper_table[key]:
#                     return False
#             return True

#         for i in range(len(s1)):
#             if s1[i] in table:
#                 table[s1[i]] += 1
#             else:
#                 table[s1[i]] = 1

#         for i in range(len(s2)):
#             result = helper(s2[i:i + len(s1)])
#             if result == True:
#                 return True
#         return False

# @lc code=end
