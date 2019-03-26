kind,count = map(int,input().split())
l1 = input().split()
l2 = input().split()
l3 = []
num = 0
for i in range(kind):
    if int(l1[i]) != 0:
        l3.append(int(l2[i])/int(l1[i]))
    else:
        l3.append(0)
while True:
    v_index = l3.index(max(l3))
    if count - int(l1[v_index]) > 0:
        num = num + int(l2[v_index])
        count = count - int(l1[v_index])
    else:
        num = num + (count/int(l1[v_index])) * int(l2[v_index])
        print(round(num,2),end='')
        break
    l3 = l3[:v_index] + l3[v_index+1:]
    l1 = l1[:v_index] + l1[v_index+1:]
    l2 = l2[:v_index] + l2[v_index+1:]