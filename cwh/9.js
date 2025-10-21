// 给你一个链表的头节点 head ，判断链表中是否有环。

// 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

// 如果链表中存在环 ，则返回 true 。 否则，返回 false 

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

// floyd 判圈算法 fast相对于slow以速度1移动
function a(head){
    let slow = head,fast = head;

    while(fast && fast.next){
        slow = slow.next;
        fast = fast.next.next;
        if(slow == fast) return true;
    }

    return false;
}

// 1. 创建一个示例链表：1 -> 2 -> 3 -> null
var node3 = new ListNode(3,node2);       // 最后一个节点（next默认null）
var node2 = new ListNode(2, node3); // 第二个节点，next指向node3
var node1 = new ListNode(1, node2); // 第一个节点（头节点），next指向node2
node3.next = node2;

console.log(a(node1))