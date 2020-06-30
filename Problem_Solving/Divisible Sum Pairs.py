arr = list(map(int,input().split(' ')))
k = int(input())
counter=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if(i<j):
            if((arr[i]+ arr[j]) % k == 0):
                print(f'[{arr[i] , arr[j]}]')
                counter += 1

print(counter)    