count = int(input())
max_ = ['name','0000/00/00',0000,00,00]
min_ = ['name','0000/00/00',9999,99,99]
num = 0
d = 0
while num < count:
    name,date = input().split()
    year,month,day = map(int,date.split('/'))
    x = 2014 - year
    y = 9 - month
    
    if x <= 200 and x >=0:
        if x == 200 and y > 0:
            num = num + 1
            continue
        if y ==0 and 6-day>0:
            num = num + 1
            continue
        if year>max_[2]:
            max_ = [name,date,year,month,day]
        elif year==max_[2] and month>max_[3]:
            max_ = [name,date,year,month,day]
        elif month>max_[3] and day>max_[4]:
            month>max_[3]
        if year<min_[2]:
            min_ = [name,date,year,month,day]
        elif year==max_[2] and month<min_[3]:
            min_ = [name,date,year,month,day]
        elif month<min_[3] and day<min_[4]:
            month<min_[3]
        d = d + 1
    num = num + 1
print("{} {} {}".format(d,min_[0],max_[0]))