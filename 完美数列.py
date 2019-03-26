count,p = map(int,input().split())
l = [int(i) for i in input().split()]
maxi = max(l)
mini = min(l)
num = 0
for i in l:
    if maxi <= i * p:
        num = num + 1
print(num,end='')