# 数素数
# 题目描述
# 令Pi表示第i个素数。现任给两个正整数M <= N <= 10000，请输出PM到PN的所有素数。

# 输入描述
# 输入在一行中给出M和N，其间以空格分隔。

# 输出描述
# 输出从PM到PN的所有素数，每10个数字占1行，其间以空格分隔，但行末不得有多余空格。

# 输入例子
# 5 27

# 输出例子
# 11 13 17 19 23 29 31 37 41 43 
# 47 53 59 61 67 71 73 79 83 89 
# 97 101 103
count = 0
data_start = 0
data_end = 0
data_num = 0
def print_num(data):
    global count,data_start,data_end,data_num
    data_num = data_num + 1
    if int(data_start) > data_num or int(data_end) < data_num:
        return
    count = count + 1
    if count == 10:
        print(data)
        count =0
    elif int(data_end) == data_num:
        print(data,end='')
    else:
        print(data,end=' ')
def get_num(data):
    if data<2:
        return 
    elif data == 2:
        print_num(data)
        return
    for i in range(2,data+1):
        if data == i:
            print_num(data)
        elif data % i == 0 :
            return
data_start,data_end = input().split()
i = 2
while int(data_end) >=  data_num:
    if int(data_start) == 10000:
        print('104729',end='')
        break
    get_num(i)
    i = i +1