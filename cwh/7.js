// 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function a(head){
    let arr = [];

    while(head){
        arr.push(head.val)
        head = head.next
    }

    return arr.join('') === arr.slice().reverse().join('')
}


const node4 = ListNode(1)
const node3 = ListNode(2,node4)
const node2 = ListNode(2,node3)
const node1 = ListNode(1,node2)

console.log(a(node1))
