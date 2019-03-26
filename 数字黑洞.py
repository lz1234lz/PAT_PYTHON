a = input()
while len(a) < 4:
    a = a + '0'
def chang_value(a):
    if len(set(a)) == 1:
        print('{} - {} = 0000'.format(''.join(a),''.join(a)))
        return 6174
    a.sort()
    a1 = a.copy()
    a.reverse()
    a2 = a.copy()
    ax = ''.join(a1)
    ay = ''.join(a2)
    result = int(ay) - int(ax)
    print("{} - {} = {}".format(ay,ax,result))
    return result
while True:
    a = chang_value(list(str(a)))
    if a == 6174:
        break