// 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
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

var sortList = function(head) {
    let cur = head;
    let arr = [];
    while(cur){
        arr.push(cur.val);
        cur = cur.next;
    }
    // console.log(arr)
    arr.sort((a,b)=>a-b)
    console.log(arr)

    let i = 0;
    cur = head

    while(cur){
        cur.val = arr[i];
        cur = cur.next;
        i++;
    }

    // console.log(arr)

    return head;
};

const node3 = new ListNode(2);
const node2 = new ListNode(3, node3);
const node1 = new ListNode(1, node2);

console.log(sortList(node1))

