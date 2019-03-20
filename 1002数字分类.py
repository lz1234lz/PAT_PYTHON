# 题目描述
# 给定一系列正整数，请按要求对数字进行分类，并输出以下5个数字：

# A1 = 能被5整除的数字中所有偶数的和；
# A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；
# A3 = 被5除后余2的数字的个数；
# A4 = 被5除后余3的数字的平均数，精确到小数点后1位；
# A5 = 被5除后余4的数字中最大数字。

# 输入描述:
# 每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N，随后给出N个不超过1000的待分类的正整数。数字间以空格分隔。


# 输出描述:
# 对给定的N个正整数，按题目要求计算A1~A5并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。
# 若其中某一类数字不存在，则在相应位置输出“N”。

# 输入例子:
# 13 1 2 3 4 5 6 7 8 9 10 20 16 18

# 输出例子:
# 30 11 2 9.7 9
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
data  = [int(x) for x in input().split()][1:]
for x in data:
    if x % 5 == 0 and x % 2 == 0:
        list_1.append(x)
    elif x % 5 == 1:
        list_2.append(pow(-1,len(list_2))*x)
    elif x % 5 == 2:
        list_3.append(x)
    elif x % 5 == 3:
        list_4.append(x)
    elif x % 5 == 4:
        list_5.append(x)
if len(list_1) == 0:
    x1 = 'N'
else:
    x1 = sum(list_1)
if len(list_2) == 0:
    x2 = 'N'
else:
    x2 = sum(list_2)
if len(list_3) == 0:
    x3 = 'N'
else:
    x3 = len(list_3)
if len(list_4) == 0:
    x4 = 'N'
else:
    x4 = round(sum(list_4)/len(list_4),1)
if len(list_5) == 0:
    x5 = 'N'
else:
    x5 = max(list_5)
print("{} {} {} {} {}".format(x1,x2,x3,x4,x5))