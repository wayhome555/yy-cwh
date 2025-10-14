'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        #初始化dp数组，dp[i]表示组成金额i所需的最少硬币数
        #初始值设为amount+1，表示一个不可能的大值
        dp=[amount+1]*(amount+1)
        dp[0]=0 #初始化的dp，表示组成金额0需要0个硬币
        
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    #取“不使用当前硬币”和“使用当前硬币”两种情况的最小值
                    dp[i]=min(dp[i],dp[i-coin]+1)
        #如果最终结果还是amount+1，说明无法找到组成该金额
        return dp[amount] if dp[amount]<=amount else -1
    
    class Solution:
    def a(self, coins: List[int], amount: int) -> int:
        # 初始化
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for coin in coins:
            # 遍历背包
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1


    def b(self, coins: List[int], amount: int) -> int:
        # 初始化
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for j in range(1, amount + 1):
            # 遍历背包
            for coin in coins:
                if j >= coin:
                	dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1