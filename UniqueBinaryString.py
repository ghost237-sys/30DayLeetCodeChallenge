"""
1980

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
"""


from itertools import product

nums = ["111","011",'001']
def findDifferentBinaryString(nums):
    binary = ['1','0']
    for i in (''.join(p) for p in product(binary,repeat=len(nums))):
        if i not in nums:
            return i

print(findDifferentBinaryString(nums))