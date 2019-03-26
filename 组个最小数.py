l = input().split()
l = list(''.join([str(i)*int(l[i]) for i in range(10)]))
l.sort()
count = 0
for i in l:
    if i == '0':
        count = count + 1
    else:
        break
print("{}{}".format(l[count],''.join(l[:count]+l[count+1:])))