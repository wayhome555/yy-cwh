// 给你一棵二叉树的根节点，返回该树的 直径 。

// 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

// 两节点之间路径的 长度 由它们之间边数表示。

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

var diameterOfBinaryTree = function(root) {
    let max = 0;

    const dfs = (root) => {
        if(!root) return 0;
        const l = dfs(root.left);
        const r = dfs(root.right);

        max = Math.max(max,l+r)

        return Math.max(l,r) + 1;
    }

    dfs(root);

    return max;
};

node4 = new TreeNode(1)
node5 = new TreeNode(1)
node2 = new TreeNode(1,node4,node5)
node3 = new TreeNode(1)
node1 = new TreeNode(1,node2,node3)

console.log(diameterOfBinaryTree(node1))