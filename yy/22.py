'''给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。'''

#动态规划，01背包问题
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # 总和为奇数时不可能分割成两个等和子集
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        # dp[i] 表示能否组成和为 i 的子集
        dp = [False] * (target + 1)
        dp[0] = True  #  base case：和为 0 可以通过不选任何元素实现
        
        for num in nums:
            # 从后往前遍历，避免重复使用同一个元素
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                #如果不选当前 num：dp[i] 保持之前的状态（即是否能通过之前的元素组成i）。
                #如果选当前 num：则需要判断「能否通过之前的元素组成 i - num」（因为加上当前 num 后总和为 i），即 dp[i - num]。
        
        return dp[target]
    
#记忆化搜索
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> bool:
            if i < 0:
                return j == 0
            return j >= nums[i] and dfs(i - 1, j - nums[i]) or dfs(i - 1, j)

        s = sum(nums)
        return s % 2 == 0 and dfs(len(nums) - 1, s // 2)