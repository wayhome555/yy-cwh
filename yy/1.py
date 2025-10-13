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