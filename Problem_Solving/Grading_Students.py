import math
n =2
a = [73,67,38,33]
for i in range(len(a)):
    print('For grade : ',a[i])
    if a[i] >= 40:
        x = a[i]/5
        b = (math.ceil(x))*5
        
        key = b-a[i] 

        if  key< 3:
            print('Final grade  =',b)
        else:
            print('Final grade  =',a[i])
    else:
        print('Final grade  =',a[i])

