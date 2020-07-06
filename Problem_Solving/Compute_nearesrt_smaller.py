
l= list(map(int,input().split(' ')))
a = list(str(l[0]))
flag = True
b= l[1]
minvalue = 0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        for k in range(0,len(a)):
            if i!=j and j!=k and k!=i:
                # print(a[i],a[j],a[k])
                value = int(str(a[i])+str(a[j])+str(a[k]))
                if value > b and flag:
                    minvalue = value
                    print(minvalue)
                    flag = False
                    



# print(minvalue)
                    

                