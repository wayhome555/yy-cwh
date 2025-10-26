// 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var removeNthFromEnd = function(head, n) {
    let cur = head;
    let m = 0;
    while(cur){
        cur = cur.next;
        m++;
    }
    let k = m-n;

    if(k === 0){
        return head.next;
    }

    cur = head;
    for(let i=1;i<=k;i++){
        if(i === k){
            cur.next = cur.next.next
            break;
        }else{
            cur = cur.next;
        }
    }

    return head;
};

const node3 = new ListNode(2);
const node2 = new ListNode(3, node3);
const node1 = new ListNode(1, node2);

console.log(removeNthFromEnd(node1,2))