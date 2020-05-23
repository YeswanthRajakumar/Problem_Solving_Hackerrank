n = int(input())
l=[]

for i in range(0,n):
    x = input().split(' ')
    command = x[0]
    if x[0] == 'insert':
        l.insert(int(x[1]),int(x[2]))

    if x[0] == 'print':
        print(l)

    if x[0] == 'remove':
        l.insert(int(x[2]))

    if x[0] == 'append':
        l.append(int(x[2]))

    if x[0] == 'sort':
        l.sort()

    if x[0] == 'pop':
        if (len(l) !=0 ):
            l.pop()

    if x[0] == 'reverse':
        l.reverse()

    