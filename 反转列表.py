start,count,fan = input().split()
num = 0
l = {}
r = []
r2 = []
while num < int(count):
    a,b,c = input().split()
    l[a] =  {
        'v':b,
        'n':c,
        'c':a
    }
    num = num + 1
num = 0
while num < int(count):
    if start == '-1':
        break
    x = l[start]
    r.append(x)
    start = l[start]['n']
    num = num + 1
num = 0
while num < (len(r) // int(fan)) :
    x = r[num*int(fan):(num+1)*int(fan)]
    x.reverse()
    r2.append(x)
    num = num + 1
r2.append(r[(num)*int(fan):])
z = []
for i in r2:
    z = z + i
num = 0 
while num < (len(z) - 1):
    print("{} {} {}".format(z[num]['c'],z[num]['v'],z[num+1]['c']))
    num = num + 1
print("{} {} -1".format(z[num]['c'],z[num]['v']))