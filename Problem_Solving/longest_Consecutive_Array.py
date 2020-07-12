a =[1,2,3,4,100,200,300,400,500]
count =0
maxi = 1 
for i in range(len(a)-1):
    if a[i+1] == a[i]+1:
        count +=1 
    else:
        if count >= maxi:
            maxi = count
            count = 0

print(maxi)