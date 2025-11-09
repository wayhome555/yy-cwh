'''给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last=len(nums)-1
        for i in range(last-1,-1,-1): #倒序遍历
            if i+nums[i]>=last: #当前位置+现在元素是否大于长度
                last=i #将终点设置为当前下标，表示考虑前面的是否能到达当前下标
        return last==0 #表示整个数组可以从0到len(nums)-1

#方法2：
class Solution:
    def a(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)-1):
            if nums[i]==0:#看非最后位置是否有0，且0前面没有任何一个值可以直接跳过0
                j=0
                while j<i:
                    if nums[j]>i-j: #i-j表示i和j的距离，如果大于则表示可以跳过0
                        break
                    j+=1
                if j==i:
                    return False
        return True