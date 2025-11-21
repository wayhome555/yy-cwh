''' 
小红拿到了一个数组，她每次可以进行如下操作：
选择一个数，使其减去x。
小红希望k 次操作之后，该数组的最大值尽可能小。请你求出这个尽可能小的最大值。
'''

#最大堆
import heapq
n, k, x = map(int, input().split())
a = list(map(int, input().split()))

# 将数组转换为负数，以利用 heapq 实现最大堆
max_heap = [-num for num in a]
heapq.heapify(max_heap) # 将列表构建成一个堆

for _ in range(k):
    # 取出当前最大值（即堆顶元素的相反数）
    current_max = -heapq.heappop(max_heap)
    
    # 执行减 x 操作
    new_value = current_max - x
    
    # 将新值插回堆中（注意要取负）
    heapq.heappush(max_heap, -new_value)

# 最终堆顶元素的相反数就是答案
print(-max_heap[0])


#优化
#（数学优化 + 最大堆）
import heapq
n, k, x = map(int, input().split())
a = list(map(int, input().split()))

# 转换为最大堆
max_heap = [-num for num in a]
heapq.heapify(max_heap)

while k > 0:
    # 取出当前最大值
    current_max = -max_heap[0]
    
    # 如果堆中只有一个元素
    if len(max_heap) == 1:
        # 直接计算最终值
        current_max -= k * x
        heapq.heappop(max_heap)
        heapq.heappush(max_heap, -current_max)
        break
    
    # 取出第二大的值
    heapq.heappop(max_heap)
    second_max = -max_heap[0]
    heapq.heappush(max_heap, -current_max)
    
    # 计算最多可以减的次数
    diff = current_max - second_max
    if diff == 0:
        # 如果最大值和第二大值相等，只能减一次
        t = 1
    else:
        t = diff // x + 1
    
    # 确定实际要减的次数
    t = min(t, k)
    
    # 更新最大值
    current_max -= t * x
    heapq.heappop(max_heap)
    heapq.heappush(max_heap, -current_max)
    
    # 更新 k
    k -= t
# 输出最终的最大值
print(-max_heap[0])