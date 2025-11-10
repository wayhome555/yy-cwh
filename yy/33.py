'''给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。
左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0'''

# 栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        max_L=0
        n=len(s)
        tmp=[0]*n #标记数组
        cur=0
        for i in range(n):
            if s[i]=='(':
                stack.append(i)
            else:
                if stack:
                    j=stack.pop()
                    tmp[i],tmp[j]=1,1 #匹配成功，标记为1，i为')'的下标，j为'('的下标

        for num in tmp:
            if num==1:
                cur+=1
                if max_L<cur:
                    max_L=cur
            else:
                cur=0
        return max_L
    
# 动态规划
# 动态规划解法：计算字符串中最长有效括号子串的长度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp[i] 表示以索引i结尾的最长有效括号子串的长度
        # 注意：因为有效括号必须以右括号结尾，所以所有以左括号结尾的位置，其dp值必定为0
        n = len(s)  # 获取字符串长度
        if n == 0:  # 处理空字符串的边界情况
            return 0
        dp = [0] * n  # 初始化dp数组，所有位置初始值为0
        res = 0  # 用于记录全局最长有效括号子串长度
        
        # 从第二个字符开始遍历（第一个字符即使是括号也无法形成有效括号对）
        for i in range(n):
            # 只需要考虑右括号的情况，因为左括号结尾的位置无法形成有效括号
            if i > 0 and s[i] == ')':
                # 情况1：如果前一个字符是左括号，形成了 "...()" 的结构
                if s[i-1] == '(':
                    # 当前有效长度为：前面两个位置的有效长度 + 2（当前这对括号）
                    # i-2 >= 0 时，dp[i-2] 存在，否则加0
                    dp[i] = dp[i-2] + 2 if i-2 >= 0 else 2
                
                # 情况2：如果前一个字符也是右括号，需要检查是否存在能与当前右括号匹配的左括号
                elif s[i-1] == ')':
                    # 计算与当前右括号可能匹配的左括号位置：跳过i-1位置的最长有效括号长度
                    left_index = i - dp[i-1] - 1
                    # 检查left_index是否有效且对应的字符是否为左括号
                    if left_index >= 0 and s[left_index] == '(':
                        # 当前有效长度 = i-1位置的有效长度 + 2（新匹配的括号对）
                        dp[i] = dp[i-1] + 2
                        # 如果新匹配的左括号前面还有有效括号（left_index-1 >= 0），则需要加上前面的有效长度
                        if left_index - 1 >= 0:
                            dp[i] += dp[left_index - 1]
                
                # 更新全局最长有效括号长度
                if dp[i] > res:
                    res = dp[i]
        
        # 返回找到的最长有效括号子串长度
        return res