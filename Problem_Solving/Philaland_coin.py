t= int(input())
for i in range(0,t):
    n = int(input())
    count =0
    while 2**count <=n:
        count+=1
    print(count)
   