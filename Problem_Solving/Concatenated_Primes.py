def prime_or_not(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count > 2:
        return False
    else:
        return True

num = 20
lookups =[]
for i in range(2,num+1):
    # print( str(i) +':'+ str(prime_or_not(i)))
    if prime_or_not(i):
        lookups.append(i)

# print(lookups)
whole_list =[]

for i in range(len(lookups)):
    for j in range( i,len(lookups)):
        whole_list.append(int(str(lookups[i])+str(lookups[j])))
        whole_list.append(int(str(lookups[j])+str(lookups[i])))

whole_list = list(set(whole_list))
c  = 0
for i in range(len(whole_list)):
    if prime_or_not(whole_list[i]):
        c+=1

print(c)