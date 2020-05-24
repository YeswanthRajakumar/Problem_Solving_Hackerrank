import math
n =2
a = [73,67,38,33]
f_list =[]
for i in range(len(a)):
   
    if (a[i]+5) >= 40:
        x = a[i]/5
        b = (math.ceil(x))*5
        
        key = b-a[i] 

        if  key< 3:
           f_list.append(b)

        else:
           f_list.append(a[i])

    else:
        f_list.append(a[i])


print(f_list)