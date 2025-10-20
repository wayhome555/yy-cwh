// 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */


function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}


// var getIntersectionNode = function(headA, headB) {
//     let arr1 = [];
//     let arr2 = [];

//     let current1 = headA;
//     let tag = headA;
//     let current2 = headB;

//     while(current1){
//         arr1.push(current1.val);
//         current1 = current1.next;
//     }

//     while(current2){
//         arr2.push(current2.val);
//         current2 = current2.next;
//     }

//     len = 0;
//     len1 = arr1.length;
//     len2 = arr2.length;

//     if(len1 > len2){
//         len = len1;
//     }else{
//         len = len2;
//     }

//     for(let i=0;i<len;i++){
//         if(arr1[i]==arr2[i]){
//             while(tag){
//                 if(tag.val == arr1[i]){
//                     return tag;
//                 }
//                 tag = tag.next;
//             }
//         }
//     }
//     return null;
// };

var getIntersectionNode = function(headA, headB) {
    if (!headA || !headB) return null; // 若任一链表为空，直接返回null
    
    let pA = headA, pB = headB; // 定义两个指针，分别从两个链表头出发
    while (pA !== pB) { // 当两指针未相遇时，继续循环
        // 指针走完当前链表后，切换到另一条链表的头部继续走
        pA = pA ? pA.next : headB; 
        pB = pB ? pB.next : headA;
    }
    return pA; // 相遇时，pA和pB要么是相交节点，要么都是null
};

function a(headA,headB){

    if(!headA || !headB) return null;

    let p1 = headA;
    let p2 = headB;

    while(p1!==p2){
        p1 = p1 ? p1.next : headB;
        p2 = p2 ? p2.next : headA
    }

    return p1;
}

// 1. 创建一个示例链表：1 -> 2 -> 3 -> null
const node3 = new ListNode(3);       // 最后一个节点（next默认null）
const node2 = new ListNode(2, node3); // 第二个节点，next指向node3
const node1 = new ListNode(1, node2); // 第一个节点（头节点），next指向node2

const node4 = new ListNode(4,node2)

console.log(a(node1,node4))