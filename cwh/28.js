// 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

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
 * @return {number[][]}
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

var levelOrder = function(root) {
    if(!root) return [];

    let queue = [root];
    let res = [];
    while(queue.length){
        let len = queue.length; let ls = [];
        while(len--){
            const node = queue.shift()
            ls.push(node.val);

            node.left && queue.push(node.left);
            node.right && queue.push(node.right);

        }

        res.push(ls)
    }
    return res;
};

node4 = new TreeNode(4)
node5 = new TreeNode(5)
node2 = new TreeNode(2,node4,node5)
node3 = new TreeNode(3)
node1 = new TreeNode(1,node2,node3)

console.log(levelOrder(node1))