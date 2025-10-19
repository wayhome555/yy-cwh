'''
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=0
        cnt=defaultdict(int)#当访问一个不存在的键时不报错，而是赋予一个默认的值0
        cnt[0]=1 
        def dfs(node,s):
            if node is None:
                return

            nonlocal ans
            s+=node.val
            ans+=cnt[s-targetSum]#如果当前节点的前缀和减去目标值在cnt中，即在出现过的前缀和中

            cnt[s]+=1 #将当前节点对应的前缀和记录在前缀和字典里
            dfs(node.left,s)
            dfs(node.right,s)
            cnt[s]-=1 #相当于这个节点的左右子树已经分析完毕，回退到上一个节点（路径是向下的，所以向上回退）
                      #同时删掉这个节点对应的前缀和数据（cnt[s] -= 1）
        dfs(root,0)
        return ans    
