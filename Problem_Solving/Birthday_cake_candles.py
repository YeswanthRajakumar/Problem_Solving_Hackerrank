n = 4
arr =[3,2,1,3]
max_arg = max(arr)
count =0
for i in arr:
    if i == max_arg:
        count+=1

print(count)