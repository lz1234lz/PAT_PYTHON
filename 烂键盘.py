l1 = [i.upper()for i in list(input())]
l2 = [i.upper()for i in list(input())]
l3 = set(l1)-set(l2)
l = []
for i in l3:
    l.append({
        'v':i,
        'i':l1.index(i)
    })
def sort_s(value):
    return value['i']
l.sort(key=sort_s)
for i in l:
    print(i,end='')