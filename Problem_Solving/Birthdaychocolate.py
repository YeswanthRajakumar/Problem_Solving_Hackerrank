s = [2,2,1,3,2]
m=2
d=4
count =0
for i in range(0,len(s)):
        if sum(s[i:m+i]) == d: 
            count +=1
print(count)