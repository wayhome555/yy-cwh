'''
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__=lambda a,b:a.val < b.val#让堆可以比较节点大小,小根堆

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur=dummy=ListNode()
        h=[head for head in lists if head]#把所有非空链表的头节点都加上
        heapify(h)#堆化
        while h:
            node=heappop(h)#剩余节点中的最小节点
            if node.next:
                heappush(h,node.next)#链表节点下一个节点可能也是最小节点，入堆
            cur.next=node#添加到新链表中
            cur=cur.next
        return dummy.next


    #递归写法，先合并两个链表，再合并其他链表，对合并后的链表递归合并（分治法）
    def a(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2  # 拼接剩余链表
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        if m == 0:
            return None
        if m == 1:
            return lists[0]  # 无需合并，直接返回
        # 合并左半部分和右半部分
        left = self.mergeKLists(lists[:m // 2])  # 合并左半部分
        right = self.mergeKLists(lists[m // 2:])  # 合并右半部分
        return self.mergeTwoLists(left, right)  # 最后把左半和右半合并



    #迭代法，自底向上合并链表
    #先将两个小链表合并并排序成一个中链表
    def b(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2  # 拼接剩余链表
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)  
        if m == 0:      
            return None
        step = 1        # 初始步长为1，表示相邻链表两两合并
        # 当步长小于链表总数时，继续合并过程
        while step < m:
            # 遍历数组，每次合并两个相隔step的链表
            # 例如：step=1时合并(0,1),(2,3),...；step=2时合并(0,2),(4,6),...
            for i in range(0, m - step, step * 2):
                # 将合并后的链表存储回当前位置，减少空间使用
                lists[i] = self.mergeTwoLists(lists[i], lists[i + step])
            step *= 2   # 步长翻倍，进入下一轮合并
        return lists[0]  # 最终合并结果存储在数组第一个位置