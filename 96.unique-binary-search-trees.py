#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for nodes in range(2, n+1):
            result = 0
            for root in range(1, nodes+1):
                left, right = root-1, nodes-root
                result += dp[left] * dp[right]
            dp[nodes] = result
        return dp[n]
        
        
        
# @lc code=end

