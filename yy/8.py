给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #创建虚拟头节点，简化头节点处理
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy#前一个结点的指针
        while prev.next and prev.next.next:
            node1=prev.next
            node2=prev.next.next
            #交换
            prev.next=node2
            node1.next=node2.next
            node2.next=node1

            prev=node1

        return dummy.next