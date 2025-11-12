'''给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
输出：true

示例 2：
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
输出：true

示例 3：
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
输出：false'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        def dfs(i,j,k):
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            board[i][j]=''#标记访问过
            for x,y in (i,j-1),(i,j+1),(i-1,j),(i+1,j):#相邻格子
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True
            board[i][j]=word[k]#恢复现场
            return False
        return any(dfs(i,j,0) for i in range(m) for j in range(n))

'''2步优化：
1.如果 word 的某个字母的出现次数，比 board 中的这个字母的出现次数还要多，可以直接返回 false
2.设 word 的第一个字母在 board 中出现了 x 次，word 的最后一个字母在 board 中出现了 y 次。
如果 y<x，我们可以把 word 反转，相当于从 word 的最后一个字母开始搜索，这样更容易在一开始就满足 board[i][j] != word[k]，
不会往下递归，递归的总次数更少。
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):  # 优化一
            return False
        if cnt[word[-1]] < cnt[word[0]]:  # 优化二
            word = word[::-1]

        m, n = len(board), len(board[0])
        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:  # 匹配失败
                return False
            if k == len(word) - 1:  # 匹配成功！
                return True
            board[i][j] = ''  # 标记访问过
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 相邻格子
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True  # 搜到了！
            board[i][j] = word[k]  # 恢复现场
            return False  # 没搜到
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
