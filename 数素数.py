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