'''给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        if n<3:
            return result
        nums.sort()
        #遍历每个元素作为三元组的第一个数
        for i in range(n):
            if nums[i]>0:
                break   
            if i>0 and nums[i] ==nums[i-1]:
                continue
            left=i+1
            right=n-1
            #双指针遍历，寻找满足条件的另外两个数
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]
                if current_sum==0:
                    result.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif current_sum<0:
                    #和太小，需要更大的数，左指针右移
                    left+=1
                else:
                    right-=1
        return result
            