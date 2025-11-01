// 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

// 有效 二叉搜索树定义如下：
// 节点的左子树只包含 严格小于 当前节点的数。
// 节点的右子树只包含 严格大于 当前节点的数。
// 所有左子树和右子树自身必须也是二叉搜索树。

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

var isValidBST = function(root) {
    const Valid = (root,low,up) => {
        if(!root) return true;

        let val = root.val;
        if(val > up || val < low) return false;

        if(!Valid(root.left,low,val)) return false;
        if(!Valid(root.right,val,up)) return false;

        return true;
    }
    return Valid(root,-Infinity,Infinity)
};

node4 = new TreeNode(4)
node5 = new TreeNode(5)
node2 = new TreeNode(2,node4,node5)
node3 = new TreeNode(3)
node1 = new TreeNode(1,node2,node3)

console.log(isValidBST(node1))