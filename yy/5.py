给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
输出：1

示例 2：
输入：grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
输出：3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])

        def dfs(i:int ,j:int):
            #如果越界或者数值不是1
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
                return 
            #是1则标记为2
            grid[i][j]='2'
            dfs(i,j-1)#往左走
            dfs(i,j+1)#往右走
            dfs(i-1,j)#往上走
            dfs(i+1,j)#往下走
        
        ans=0
        for i,row in enumerate(grid):#遍历岛屿的每一行
            for j,c in enumerate(row):#遍历当前行的每一列
                if c =='1':
                    dfs(i,j)
                    ans+=1
        return ans
    

    #最简单的DFS思路——发现有1就寻找所有相邻1全部填海为0，每个点都搜一遍
    def a(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(x, y):
            if grid[x][y] == '1':#如果是1,则将1周围的1都标记为0，这样一个岛屿只有一个1
                grid[x][y] = '0'
            else:
                return
            if x > 0:
                dfs(x - 1, y)
            if x < m - 1:
                dfs(x + 1, y)
            if y > 0:
                dfs(x, y - 1)
            if y < n - 1:
                dfs(x, y + 1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res