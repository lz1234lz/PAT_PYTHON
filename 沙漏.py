a,b = input().split()
l = [b]
num = 1
index = 3
while True:
    if index*2 + num < int(a):
        l = [' '+i+' ' for i in l]
        l.insert(0,b*index)
        l.append(b*index)
        num = num + index*2
        index = index +2
    else:
        break
for i in l:
    print(i)
print(a-num)
