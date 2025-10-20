'''
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans_left=ans_right=0
        #奇回文串
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            #循环结束后，s[l+1]到s[r-1]是回文串（因为当最后一次s[l]==s[r]时，l-1，r+1了）
            if r-l-1>ans_right-ans_left:
                ans_left=l+1
                ans_right=r-1
        #偶回文串
        for i in range(n-1):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>ans_right-ans_left:
                ans_left=l+1
                ans_right=r-1
        return s[ans_left:ans_right+1] 
    

    #合并奇回文串和偶回文串的代码
    def a(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0

        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2 #当i为偶数时，l=r=i//2，在枚举奇数回文串；当i为奇数时，在枚举偶数回文串时，l=i//2，r=i//2+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # 循环结束后，s[l+1] 到 s[r-1] 是回文串
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开区间

        return s[ans_left: ans_right]
    