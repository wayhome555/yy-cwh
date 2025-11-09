'''编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

示例 2：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
'''

# 从矩阵的左下角开始搜索，（也可以从右上角开始搜索），特征：一边比目标值小，一边比目标值大（BST）
# BST树性质（二分搜索树）
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        i,j=m-1,0
        while i>=0 and j<n:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                j+=1
            else:
                i-=1
        return False

#方法2：二分查找
class Solution:
    def a(self, matrix: List[List[int]], target: int) -> bool:
        def binay_search(nums,target):
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
            return False
        L_l=len(matrix[0])#列
        L_r=len(matrix)#行
        for line in matrix:#一次排除一行
            if line[0] <= target and line[L_l - 1] >= target:#符合条件的行
                if binay_search(line,target):
                    return True
        return False
        
