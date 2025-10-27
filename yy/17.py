'''
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        queens=[0]*n #皇后放在(r,queens[r])
        col=[False]*n #检查列冲突
        diag1=[False]*(n*2-1) #检查主对角线冲突
        diag2=[False]*(n*2-1) #检查次对角线冲突
        def dfs(r:int)->None:
            #终止条件：当r==n时，说明所有行都放完了，这是一个合法解（已经放置了n个皇后）
            if r==n:
                ans.append(['.'*c+'Q'+'.'*(n-1-c) for c in queens])
                return
            #尝试在当前行的每一列放皇后，在（r,c）放皇后
            for c,ok in enumerate(col):
                #如果当前列c没有被占用，且(r,c)不在主对角线和次对角线上，说明可以放皇后
                if not ok and not diag1[r+c] and not diag2[r-c]:#判断能否放皇后
                    queens[r]=c#直接覆盖，无需恢复现场
                    col[c]=diag1[r+c]=diag2[r-c]=True #皇后占用了c列和两条斜线
                    dfs(r+1)#递归到下一行
                    col[c]=diag1[r+c]=diag2[r-c]=False #回溯：恢复现场，尝试其他列位置
        dfs(0)
        return ans
