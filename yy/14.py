'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2'''

#Boyer-Moore 算法,时间复杂度O(n),空间复杂度O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


#哈希表,时间复杂度O(n),空间复杂度O(n)
    def a(self, nums: List[int]) -> int:
        counts=collections.Counter(nums)
        return max(counts.keys(),key=counts.get)