def isLeap(yeartype,year):
    if yeartype is "Julian":
        if year%4 == 0 :
            return True
        else:
            return False
    elif yeartype is "Georgian":
        if year%4 == 0:
            if year % 100 == 0: 
                if year %400 ==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

y = int(input("Year : "))
yeartype=""
mon = [31,28,31,30,31,30,31,31]
day = sum(mon)
dd = 0
mm = len(mon) +1
yyyy = y
if y <=1917 and y>=1700: 
     yeartype = 'Julian'
     leapyear = isLeap(yeartype,y)
     if leapyear:
        day += 1
     dd = 256 - day
     

else:
     yeartype = 'Georgian'
     leapyear = isLeap(yeartype,y)
     if leapyear:
        day += 1
     dd = 256 - day

print(f'{dd}.0{mm}.{yyyy}')