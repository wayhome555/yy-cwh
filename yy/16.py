'''给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：
输入：root = [1,null,2]
输出：2'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS后序遍历
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1#加一为根节点

#BFS层序遍历
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        else:
            depth=0
            queue=[root]
            while queue:
                depth+=1#每遍历一层，深度加一
                for i in range(len(queue)):#遍历当前层的节点
                    node=queue.pop(0)#弹出当前层的节点
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return depth