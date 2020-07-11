n = 5
charkra=[ [0 for i  in range(n)] for j  in range(n) ]

count = (n+1)//2
low = 0
high  = n-1
num = 1

for i in range(count):#0,1,2
    #TOP
    for j in range(low,high+1):#0,1,2,3,4
        charkra[i][j] = num
        num+=1
    #RIGHT
    for j in range(low+1,high+1):#1,2,3,4
        charkra[j][high] = num
        num+=1

    #BOTTOM
    for j in range(high-1,low-1,-1):
        charkra[high][j] = num
        num+=1
    #LEFT
    for j in range(high-1,low,-1):
        charkra[j][low] =num
        num+=1

    low+=1
    high -=1




for i in charkra:
    print(i)