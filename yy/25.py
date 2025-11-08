'''一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6'''



#方法2
class Solution:
    def a(self, m: int, n: int) -> int:
        #数学排列组合,总共需要走m+n-2步，选出m-1步向下走
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
    

#动态规划
#方法3
    def b(self, m: int, n: int) -> int:
        #dp[i][j]表示机器人到达（i，j）时最多的路径数
        #当i=0或者j=0时（只有一行或者一列）,路径数都为1，所以下面那[1]*n表示第一行为1，[1]表示第一列为1
        dp=[[1]*n]+[[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    

#方法4
class Solution:
    def c(self, m: int, n: int) -> int:
        #空间优化O(2n),计算第 i 行的 dp[i][j] 时，只需要 上一行的结果（i-1 行，即 pre） 和 当前行已计算的左边结果（j-1 列，即 cur）；
        pre=[1]*n
        cur=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                 # 状态转移：当前格 = 上一行同列（pre[j]） + 当前行前一列（cur[j-1]）
                cur[j]=cur[j-1]+pre[j]
            pre=cur[:] #这里用切片复制，避免引用传递（否则 pre 和 cur 会指向同一个列表）
        # pre 最终是最后一行的 dp 结果，pre[-1] 就是右下角 (m-1,n-1) 的路径数
        return pre[-1]
    
    def d(self, m: int, n: int) -> int:
        #空间优化O(n)
        cur = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j]+=cur[j-1]
        return cur[-1]
