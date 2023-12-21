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
        # T: O(n^2)
        # for i, num in enumerate(nums):
        #     if target - num in nums[i + 1:]:
        #         # find next index of the same number
        #         return [i, nums.index(target - num, i+1)]

        # T: O(n)
        # use a map to store previous numbers
        prev_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i


solution = Solution()
print(solution.twoSum([3, 3], 6))
# @lc code=end
