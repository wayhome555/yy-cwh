// 给定一个二叉树 root ，返回其最大深度。

// 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

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
 * @return {number}
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

var maxDepth = function(root) {
    if(!root) return 0;
    return 1+Math.max(maxDepth(root.left),maxDepth(root.right))
};

const node3 = new TreeNode(3);
const node2 = new TreeNode(2, node3, null);
const node1 = new TreeNode(1, null, node2);

console.log(maxDepth(node1))