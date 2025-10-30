'''给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 
示例 1：
输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。

示例 2：
输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。

示例 3：
输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。'''
#哈希表-----空间复杂度不符合
#二分查找-----时间复杂度不符合

#所以我们可以将数组视为哈希表，将每个数映射到数组的下标中，例如将1映射到下标0，将2映射到下标1，以此类推。
#再次遍历数组，检查每个数是否映射到了正确的下标中，如果没有映射到正确的下标中，那么这个数就是缺失的最小正整数。
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #3应该放在索引为2的地方，4应该放在索引为3的地方，......
        size=len(nums)
        for i in range(size):
            #先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1<=nums[i] <=size and nums[i] != nums[nums[i]-1]:
                self.__swap(nums,i,nums[i]-1)
        #再次遍历数组，检查每个数是否映射到了正确的下标中，如果没有映射到正确的下标中，那么这个数就是缺失的最小正整数。
        for i in range(size):
            if i+1 != nums[i]:
                return i+1
        return size+1
    #交换函数，用来交换数组中的两个元素，下标为i和下标为nums[i]-1的元素， git/github
    #例如将1映射到下标0，将2映射到下标1，以此类推。
    def __swap(self,nums,index1,index2):
        nums[index1],nums[index2]=nums[index2],nums[index1]