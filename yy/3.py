'''
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，
下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #单调栈，从右到左
        n=len(temperatures)
        ans=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            t=temperatures[i]
            while st and t>=temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i]=st[-1]-i #如果st不为空，则找到了比t温度更高的，计算天数差中
            st.append(i)#将当前索引压入栈
        return ans


    def a(self, temperatures: List[int]) -> List[int]:
        #单调栈，从左到右
        n = len(temperatures)
        ans = [0] * n
        st = []  # todolist
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans