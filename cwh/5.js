// 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val === undefined ? 0 : val)
 *     this.next = (next === undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}
var reverseList = function(head) {
    let prev = null;    // 初始化前一个节点为null
    let current = head; // 当前节点从头部开始
    
    while (current !== null) {
        const next = current.next; // 保存下一个节点的引用
        current.next = prev;       // 反转当前节点的指针
        prev = current;            // 移动prev到当前节点
        current = next;            // 移动current到下一个节点
    }
    
    // 循环结束后，prev就是新的头节点
    return prev;
};

// 1. 创建一个示例链表：1 -> 2 -> 3 -> null
const node3 = new ListNode(3);       // 最后一个节点（next默认null）
const node2 = new ListNode(2, node3); // 第二个节点，next指向node3
const node1 = new ListNode(1, node2); // 第一个节点（头节点），next指向node2

console.log(reverseList(node1))

function a(head){
    let prev = null;
    let current = head;

    while(!current){
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

console.log(a(node1))