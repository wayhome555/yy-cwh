// 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

var sortedArrayToBST = function(nums) {
    const build = (l,r) => {
        if(l>r) return null
        const m = (l+r)>>1;
        const node = new TreeNode(nums[m])

        node.left = build(l,m-1)
        node.right = build(m+1,r)
        return node
    }
    return build(0,nums.length-1)
};
