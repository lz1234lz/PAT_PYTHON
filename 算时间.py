a,b = map(int,input().split())
x = b-a
if x % 100 != 0:
    x = x//100 + 1
else:
    x = x // 100
def get_two(v):
    if v < 10:
        v = '0' + v
    return v
hour = x // 3600
minute = (x % 3600) // 60
sencod = x - hour * 3600 - minute * 60
print("{}:{}:{}".format(get_two(hour),get_two(minute),get_two(sencod)))