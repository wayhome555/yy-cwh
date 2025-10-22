// 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val === undefined ? 0 : val)
 *     this.next = (next === undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var mergeTwoLists = function(l1, l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    if (l1.val < l2.val) {
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else {
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
};

function a(list1, list2) {
    if (!list1) return list2;
    if (!list2) return list1;
    // 比较符号修正：选择较小的节点
    if (list1.val < list2.val) { 
        list1.next = a(list1.next, list2);
        return list1;
    } else {
        list2.next = a(list1, list2.next);
        return list2;
    }
}

// 测试用例：确保输入是升序链表
// list1: 1 -> 2 -> 3（升序）
const node3 = new ListNode(3);
const node2 = new ListNode(2, node3);
const node1 = new ListNode(1, node2);

// list2: 4 -> 5（升序）
const node5 = new ListNode(5);
const node4 = new ListNode(4, node5);

// 合并结果应为 1->2->3->4->5
console.log(a(node1, node4)); 