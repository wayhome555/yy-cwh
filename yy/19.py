'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9'''

# 思路：
# 1. 找到最高的柱子，最高的柱子左边的柱子高度都可以计算积水，最高的柱子右边的柱子高度都不可以计算积水
# 2. 从最高的柱子开始，每次遍历一个柱子，判断是否可以积水，如果可以积水，就计算积水的高度，累加起来
# 3. 最高的柱子的高度是 max(height)，最高的柱子的索引是 height.index(max(height))
# 4. 从最高的柱子的索引开始，遍历左边的柱子，判断是否可以积水，如果可以积水，就计算积水的高度，累加起来
# 5. 从最高的柱子的索引开始，遍历右边的柱子，判断是否可以积水，如果可以积水，就计算积水的高度，累加起来
# 6. 返回累加起来的积水高度


##前两种都会超时，for循环嵌套会超时
#按行计算积水，一层一层判断能否积水，一层高度为一
class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        max_height=max(height)

        for i in range(1,max_height+1):
            is_start=False #标记是否开始计算临时积水
            temp_sum=0
            for j in range(len(height)):
                if is_start and height[j]<i:
                    temp_sum+=1
                if height[j]>=i: #例如101的情况
                    total+=temp_sum
                    temp_sum=0
                    is_start=True
        return total

#按列计算积水，每次遍历一个柱子，判断是否可以积水，如果可以积水，就计算积水的高度，累加起来
    def a(self, height: List[int]) -> int:
        total = 0
        # 最两端的列不用考虑，因为一定不会有水，所以下标从 1 到 len(height) - 2
        for i in range(1, len(height) - 1):
            max_left = 0
            # 找出左边最高
            for j in range(i - 1, -1, -1):
                if height[j] > max_left:
                    max_left = height[j]
            max_right = 0
            # 找出右边最高
            for j in range(i + 1, len(height)):
                if height[j] > max_right:
                    max_right = height[j]
            # 找出两端较小的
            min_val = min(max_left, max_right)
            # 只有较小的一段大于当前列的高度才会有水，其他情况不会有水
            if min_val > height[i]:
                total += (min_val - height[i])
        return total

#对max_left和max_right进行优化，避免重复遍历
#使用动态规划，提前计算好每个柱子左边最高的柱子高度和右边最高的柱子高度
    def b(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        if n == 0:
            return 0
        
        max_left = [0] * n
        max_right = [0] * n
        
        # 计算左侧最大值数组
        for i in range(1, n - 1):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        
        # 计算右侧最大值数组
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        
        # 计算总积水量
        for i in range(1, n - 1):
            min_val = min(max_left[i], max_right[i])
            if min_val > height[i]:
                total += (min_val - height[i])
        
        return total


#双指针，因为前面动态规划的max_left和max_right都是只使用一次，所以可以使用双指针优化
    def c(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        if n <= 2:
            return 0  # 长度小于等于2时无法积水
        
        max_left = 0
        max_right = [0] * n  # 存储每个位置右侧的最大高度
        
        # 先计算右侧最大值数组
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        
        # 计算总积水量
        for i in range(1, n - 1):
            # 更新左侧最大值（当前位置左边的最大高度）
            max_left = max(max_left, height[i - 1])
            # 取左右两侧最大值中的较小值
            min_val = min(max_left, max_right[i])
            # 若较小值大于当前高度，则可积水
            if min_val > height[i]:
                total += (min_val - height[i])
        
        return total


#栈，栈中存储的是柱子的索引，从栈顶到栈底的高度是单调递减的
    def d(self, height: List[int]) -> int:
        total = 0
        stack = []
        current = 0
        while current < len(height):
            # 当栈不为空且当前高度大于栈顶索引对应的高度时
            while stack and height[current] > height[stack[-1]]:
                h = height[stack[-1]]  # 取出栈顶元素的高度
                stack.pop()  # 栈顶元素出栈
                if not stack:  # 栈为空则跳出循环
                    break
                # 计算两堵墙之间的距离
                distance = current - stack[-1] - 1
                # 取左右两堵墙的最小高度
                min_height = min(height[stack[-1]], height[current])
                # 累加积水量
                total += distance * (min_height - h)
            # 当前索引入栈
            stack.append(current)
            # 移动当前指针
            current += 1
        return total