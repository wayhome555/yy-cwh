'''游游拿到了一个正整数，她希望你能重排这个正整数的数位，使得它变成偶数（不能有前导零）。你能帮帮她吗？
注：重排后可以和原数相等。
一共有 q 次询问。
输出q行，每行代表一次询问。
如果存在合法解，请输出一个重排后的正整数，务必保证其为偶数。有多解时输出任意即可。
如果不存在合法解，直接输出-1。
输入：
3
13
123
24
输出：
-1
132
24
'''
count=int(input())#访问次数
x=0
for i in range(count):
    flag=False
    str1=''
    s=''
    x=input()
    for ch in x:
        if int(ch)%2==0:
            flag=True
            s+=ch
        else:
            str1+=ch
    if flag==True:
            str1+=s
            print(str1)
    else:
        print('-1')
    
            