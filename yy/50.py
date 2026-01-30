'''给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在恰好一个解。

示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        ans=inf
        for i in range(n-2):
            left,right=i+1,n-1
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            current_sum=nums[i]+nums[i+1]+nums[i+2]#最小的
            if current_sum>target:#后面无论怎么选，选出的三数之和都会比current_sum大
                if abs(current_sum-target)<abs(ans-target):
                    ans=current_sum
                break
            current_sum=nums[i]+nums[-2]+nums[-1]#最大的
            if current_sum<target:
                if abs(current_sum-target)<abs(ans-target):
                    ans=current_sum
            
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]
                if current_sum==target:
                    return target
                if abs(current_sum-target)<abs(ans-target):
                    ans=current_sum
                if current_sum>target:
                    right-=1
                else:
                    left+=1
        return ans