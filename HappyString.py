"""
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
"""
from itertools import product

n = 1
k = 4


def getHappyString(n,k):
    valid_letters = ['a','b','c']
    all_combinations = [''.join(p) for p in product(valid_letters,repeat=n) if no_repeats(p)]
    print(all_combinations)
    if len(all_combinations) > k:
        return all_combinations[k-1]

def no_repeats(s):
    return all(s[i] != s[i+1] for i in range(len(s)-1))

print(getHappyString(n,k))


