a,b,d = map(int,input().split())
c = a + b
l = []
def change(c,d):
    if c > d:
        m = c // d 
        n = c % d
        l.insert(0,str(n))
        change(m,d)
    else:
        l.insert(0,str(c))
change(c,d)
print(''.join(l),end='')