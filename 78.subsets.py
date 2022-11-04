#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        def dfs(start, subsets):
            if start >= len(nums):
                return
            self.res.append(subsets)
            for i in range(start+1, len(self.nums)):
                dfs(i, subsets+[self.nums[i]])
        dfs(-1, [])
        return self.res
        
# @lc code=end

