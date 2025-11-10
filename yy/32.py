'''给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]'''

#切片（切片会产生额外的空列表，导致内存占用增加）
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]#python特有方法

# 反转数组（反转数组会改变数组的顺序，但是不会改变数组的元素）
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i,j):
            while i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        n=len(nums)
        k%=n
        # 先将整个数组反转
        reverse(0,n-1)
        # 再将前k个元素反转
        reverse(0,k-1) #if k=3,->(0,2)
        # 最后将后n-k个元素反转
        reverse(k,n-1) #if k=3,->(3,n-1)
    
