// 给你一个二叉树的根节点 root ， 检查它是否轴对称。

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

var isSymmetric = function(root) {
    if(!root) return true;

    const symmetric = (left,right)=>{
        if(!left && !right) return true;
        if(!left || !right) return false;

        return (left.val === right.val) && symmetric(left.left,right.right) && symmetric(left.right,right.left)
    }

    return symmetric(root.left,root.right)
};

node5 = new TreeNode(1)
node4 = new TreeNode(1)
node3 = new TreeNode(2,node5,node4)

console.log(isSymmetric(node3))
