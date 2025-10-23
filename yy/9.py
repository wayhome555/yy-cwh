'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([])"
输出：true

示例 5：
输入：s = "([)]"
输出：false'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)%2!=0:
            return False
        for char in s:
            if char=='(':stack.append(')')
            elif char=='[':stack.append(']')
            elif char=='{':stack.append('}')
            elif len(stack)==0 or char!=stack.pop():#当符号为右括号时进行判断是否匹配
                return False
        return len(stack)==0
    

    def a(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        pairs={")":"(","]":"[","}":"{"}
        stack=list()
        for ch in s:
            if ch in pairs:#判断ch是不是字典里面的键
                if not stack or stack[-1]!=pairs[ch]:#stack[-1]表示栈顶
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0