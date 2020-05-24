x1 = 42
v1 = 3

x2 = 94
v2 = 2

key = False
for i in range(10000):
    print('position ---> ',x1,x2)
    if(x1 == x2):
        
        key = True
    x1 += v1
    x2 += v2

print(key)