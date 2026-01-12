'''小红定义两个字符串同构，当且仅当对于每个 i , b[i] - a[i] 是定值。例如，"bacd" 和 "edfg" 是同构的。
现在小红拿到了一个长度为 n 的字符串 a，她想知道，有多少长度为n的字符串 b 同时满足以下两个条件：
1.b 的每一位都和a不同。
2.b 和 a不同构。

输入描述
输入一个仅由英文小写字母组成的字符串，代表字符串 a
输出描述
一个整数，代表合法的字符串b的数量。由于答案过大，请对(10^9 + 7) 取模。

示例 1
输入：
ab
输出：
601

示例 2（辅助理解）
输入：
a
输出：
0
'''
a = input().strip()
n = len(a)

if n == 0:
    print(0)
    exit()

# 计算 a 中字符的最大/最小 ASCII 码
ords = [ord(c) for c in a]
max_ord = max(ords)
min_ord = min(ords)

# 有效偏移量 d 的个数（exclude）
interval_length = max_ord - min_ord + 1
exclude = 26 - interval_length

# 总合法数：25^n（每一位与 a 不同）
mod = 10**9 + 7
total = pow(25, n, mod)

# 最终答案
ans = (total - exclude) % mod
print(ans)