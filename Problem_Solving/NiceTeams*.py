
rate = [1,2,3,4,5,6]
mindif = 4
check = []
count =0
for i in range(len(rate)):
    for j in range(len(rate)):
        if i != j:
           if rate[i]-rate[j] == mindif:

                # print(rate[j],rate[i])
                count+=1
    check.append(count)


print(len((set(check))))