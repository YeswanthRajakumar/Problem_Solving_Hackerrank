arr =[1,3,5,7,9]
as_sort = sorted(arr)
des_sort = list(reversed(as_sort))
as_sum =0
des_sum =0

for i in range(0,len(arr)-1):
    as_sum +=as_sort[i]

for i in range(0,len(arr)-1):
    des_sum +=des_sort[i]


print(as_sum ,end=' ')
print(des_sum)

