'''给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=tree=ListNode()
        val=tmp=0
        # 循环条件：进位不为0 或 l1 未遍历完 或 l2 未遍历完
        while tmp or l1 or l2:
            val=tmp
            if l1:
                val=l1.val+val
                l1=l1.next
            if l2:
                val=l2.val+val
                l2=l2.next
            tmp=val//10
            val=val%10

            tree.next=ListNode(val)
            tree=tree.next
        return head.next
    

#方法2：数学，将链表转成数字，两个链表的数字相加，最后将结果转成链表
    def a(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumber(listNode):
            n=0
            num=0
            while 1:
                num+=listNode.val*(10**n)
                n+=1
                listNode=listNode.next
                if listNode==None:
                    break
            return num
        sum=getNumber(l1)+getNumber(l2)
        sumStr=str(sum)
        sumListNoe=None
        for x in sumStr:
            sumListNoe=ListNode(int(x),sumListNoe)#将整数的每一位都转成链表的一个节点
        return sumListNoe
        