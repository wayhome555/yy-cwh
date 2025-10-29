// 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

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
 * @return {number[]}
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

var inorderTraversal = function(root) {
    let result = [];

    let traversal = (root) => {
        if(!root) return;
        traversal(root.left);
        result.push(root.val);
        traversal(root.right)
    }

    traversal(root);
    return result;
};

const node3 = new TreeNode(3);
const node2 = new TreeNode(2, node3, null);
const node1 = new TreeNode(1, null, node2);

console.log(inorderTraversal(node1))