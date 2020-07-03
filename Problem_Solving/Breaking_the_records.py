arr = [10, 5 ,20 ,20 ,4 ,5 ,2 ,25 ,1]
h_score = arr[0]
max_count =0
l_score = arr[0]
min_count =0
for i in range(len(arr)):
    if arr[i]> h_score:
        h_score = arr[i]
        max_count+=1
    elif arr[i]< l_score:
        l_score = arr[i]
        min_count+=1

print(max_count,min_count)