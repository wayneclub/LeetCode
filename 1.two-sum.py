#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """use difference to find the other number"""
        for i, num in enumerate(nums):
            if target - num in nums:
                return [i, nums.index(target - num)]


# @lc code=end
