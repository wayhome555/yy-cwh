'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 
示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

示例 2：
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。

示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s=Counter() #s子串字母出现次数
        cnt_t= Counter(t)  # t 中字母的出现次数
        ans_left, ans_right = -1, len(s)
        left=0
        for right, c in enumerate(s):  # 移动子串右端点
            cnt_s[c] += 1  # 右端点字母移入子串
            while cnt_s >= cnt_t:  # 涵盖
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                cnt_s[s[left]] -= 1  # 左端点字母移出子串
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]


#优化，用一个变量 less 记录子串内有多少种字母的出现次数 < t 中的字母出现次数，
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = defaultdict(int)  # 比 Counter 更快
        for c in t:
            cnt[c] += 1
        less = len(cnt)  # 有 less 种字母的出现次数 < t 中的字母出现次数

        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):  # 移动子串右端点
            cnt[c] -= 1  # 右端点字母移入子串
            if cnt[c] == 0:
                # 原来窗口内 c 的出现次数比 t 的少，现在一样多
                less -= 1
            while less == 0:  # 涵盖：所有字母的出现次数都是 >=
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                x = s[left]  # 左端点字母
                if cnt[x] == 0:
                    # x 移出窗口之前，检查出现次数，
                    # 如果窗口内 x 的出现次数和 t 一样，
                    # 那么 x 移出窗口后，窗口内 x 的出现次数比 t 的少
                    less += 1
                cnt[x] += 1  # 左端点字母移出子串
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
