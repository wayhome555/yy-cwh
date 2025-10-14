'''
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
'''
# 动态规划
import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n==0:
            return 0
        dp=[float('inf')]*(n+1)
        dp[0]=0
        cands=[i**2 for i in range(1,int(sqrt(n)+1))]
        for i in range(1,n+1):
            for cand in cands:
                dp[i]=min(dp[i],dp[i-cand]+1)
        return dp[n]

'''
import math

class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化dp数组，dp[i]表示构成i所需的最少完全平方数数量
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 构成0需要0个完全平方数
        
        # 遍历所有可能的完全平方数
        for i in range(1, int(math.sqrt(n)) + 1):
            square = i * i
            # 更新dp数组，对于每个可以用当前平方数构成的数
            for j in range(square, n + 1):
                dp[j] = min(dp[j], dp[j - square] + 1)
        
        return dp[n]
'''

        