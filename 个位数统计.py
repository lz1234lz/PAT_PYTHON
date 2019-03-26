l = [i for i in input()]
ls = list(set(l))
ls.sort()
for i in ls:
    print("{}:{}".format(i,l.count(i)))