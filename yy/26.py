'''给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：

输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

示例 3 :
输入：nums = [3,3,3,3,3]
输出：3'''

#方法1(不符合题目所说的空间要求)
from collections import Counter
from typing import List  # 注意导入 List 类型（LeetCode 需显式导入）
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        # 筛选出现次数 > 1 的元素（题目保证只有一个）
        duplicate = [key for key, val in count_nums.items() if val > 1][0]
        return duplicate

#方法2(原地标记法)，比较巧妙，但是修改了原数组
#把 nums 中的元素当作「索引指针」：遍历数组时，用当前元素 num 作为索引，访问 nums[num]；
#用「标记 -1」表示该索引对应的元素已被访问过,如果访问到了一个已经被标记为 -1 的索引,则说明该索引对应的元素就是重复的元素
class Solution:
    def a(self, nums: List[int]) -> int:
        #因为nums的每一个数都小于len(nums)
        num=nums[0]
        while True:
            if nums[num]==-1:
                return num
            temp=nums[num]
            nums[num]=-1
            num=temp

#方法3（二分查找）
from typing import List

class Solution:
    def c(self, nums: List[int]) -> int:
        min_val = 1  # 元素取值的最小值（题目规定是1）
        max_val = len(nums) - 1  # 元素取值的最大值（n = len(nums)-1

        while min_val < max_val:  # 当范围缩小到一个数时，循环结束
            mid = (min_val + max_val) // 2  # 中间值（分割查找范围）
            
            # 统计 nums 中落在 [min_val, mid] 区间内的元素个数
            cnt = sum(min_val <= num <= mid for num in nums)  # 生成器表达式，效率高于列表推导式
            
            # 抽屉原理：区间内元素个数 > 区间长度 → 重复元素在左区间
            if cnt > mid - min_val + 1:
                max_val = mid  # 缩小范围到左区间 [min_val, mid]
            else:
                # 元素个数 ≤ 区间长度 → 重复元素在右区间
                min_val = mid + 1  # 缩小范围到右区间 [mid+1, max_val]
        
        # 最终 min_val == max_val，就是重复元素
        return min_val
    
#方法4（快慢指针）（Floyd 判环算法）最优解法
#原因：重复元素会导致「链表出现环」（因为重复元素会被多次指向，形成循环）
# 快慢指针：将数组视为链表，每个元素 nums[i] 指向 nums[nums[i]]
# 重复元素就是链表中环的入口
    def d(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            # fast 前进两次，slow 前进一次
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                break
        # ptr == slow 时说明检测到重复元素，两个重复元素同时指向环的入口。
        ptr = 0
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]
        return ptr


