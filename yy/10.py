'''
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

示例 2:
输入: numRows = 1
输出: [[1]]'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        dp=[[1]]
        for i in range(1,numRows):
            current=[1]*(i+1)
            #填充中间元素（1-~i-1）
            for j in range(1,i):
                current[j]=dp[i-1][j-1]+dp[i-1][j]
            dp.append(current)
        return dp

