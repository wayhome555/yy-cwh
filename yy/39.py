'''
小欧在平面直角坐标系上有n个点（保证n是偶数），小欧想把这些点两两配对，一共可配n/2对。配对的两点连一条线段。
若该线段和坐标轴有一个交点，则视为有1的权值。因此，和x轴和y轴都有交点则有2的权值。（特殊的，若该线段经过原点，也视为有2的权值）。
小欧希望最终的权值之和尽可能大，你能帮帮她吗？
输入描述:
第一行输入一个正整数n，代表点的数量，n保证是偶数。
接下来的n行，每行输入两个非零整数xi​和yi。

输出描述:
输出一个整数，表示最大的权值。

示例1
输入
2
1 1
-1 -1
输出
2
说明
只有两个点，连一条线段经过原点，有2的权值。

示例2
输入
4
1 1
-1 1
2 1
-2 1
输出
2
说明
第一个点和第四个点连一条线段，和y轴交于(0,1)，贡献1的权值。
第二个点和第三个点连一条线段，和y轴交于(0,1)，贡献1的权值。'''

n = int(input())
cnt_O = 0  # 原点数量
cnt_A = 0  # 第一象限 (x>0,y>0)
cnt_B = 0  # 第二象限 (x<0,y>0)
cnt_C = 0  # 第三象限 (x<0,y<0)
cnt_D = 0  # 第四象限 (x>0,y<0)

for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        cnt_O += 1
    elif x > 0 and y > 0:
        cnt_A += 1
    elif x < 0 and y > 0:
        cnt_B += 1
    elif x < 0 and y < 0:
        cnt_C += 1
    else:  # x>0, y<0
        cnt_D += 1

# 步骤1：处理原点配对（原点与非原点配对，每对权值2）
total_non_O = cnt_A + cnt_B + cnt_C + cnt_D
pair_O = min(cnt_O, total_non_O)
total = pair_O * 2  # 原点配对的权值

# 计算配对后各象限剩余数量（原点配对消耗非原点，这里简化为平均分配，不影响最终结果）
# 核心逻辑：剩余非原点总数 = total_non_O - pair_O，且保持A/C、B/D组的内部比例
remaining_non_O = total_non_O - pair_O
ratio_A = cnt_A / total_non_O if total_non_O != 0 else 0
ratio_B = cnt_B / total_non_O if total_non_O != 0 else 0
ratio_C = cnt_C / total_non_O if total_non_O != 0 else 0
ratio_D = cnt_D / total_non_O if total_non_O != 0 else 0

a = round(remaining_non_O * ratio_A)
b = round(remaining_non_O * ratio_B)
c = round(remaining_non_O * ratio_C)
d = round(remaining_non_O * ratio_D)

# 修正：确保a+b+c+d = remaining_non_O（浮点数精度问题）
diff = (a + b + c + d) - remaining_non_O
if diff != 0:
    # 优先调整数量最多的象限（不影响配对逻辑）
    max_cnt = max(a, b, c, d)
    if a == max_cnt:
        a -= diff
    elif b == max_cnt:
        b -= diff
    elif c == max_cnt:
        c -= diff
    else:
        d -= diff

# 步骤2：处理对角配对（A-C、B-D，每对权值2）
pair_AC = min(a, c)
total += pair_AC * 2
a -= pair_AC
c -= pair_AC

pair_BD = min(b, d)
total += pair_BD * 2
b -= pair_BD
d -= pair_BD

# 步骤3：处理剩余点（跨组配对，每对权值1）
remaining = a + b + c + d
total += remaining // 2  # 剩余点必为偶数，每对贡献1

print(total)