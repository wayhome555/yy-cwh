'''leafee 最近爱上了 abb 型语句，比如“叠词词”、“恶心心”
leafee 拿到了一个只含有小写字母的字符串，她想知道有多少个 "abb" 型的子序列？
定义： abb 型字符串满足以下条件：

字符串长度为 3 。
字符串后两位相同。
字符串前两位不同。
'''

n = int(input())
s = input()
suffix = [[0] * 26 for _ in range(n + 1)]
# 预处理后缀和数组
for i in range(n - 1, -1, -1):
    for j in range(26):
        suffix[i][j] = suffix[i + 1][j]
    suffix[i][ord(s[i]) - ord('a')] += 1

count = 0
for i in range(n):
    for j in range(26):
        if ord(s[i]) - ord('a') != j:
            # 计算以 s[i] 为 a，字母 j 为 b 的 "abb" 型子序列数量
            num_b = suffix[i + 1][j]
            count += num_b * (num_b - 1) // 2
print(count)