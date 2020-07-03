n = 2
m = 9
arr =[
      [1, 0 ,1 ,1 ,0 ,1 ,1 ,1 ,1], 
      [0, 0, 0, 1, 0, 1, 0, 0, 1]
     ]

i =0
j =8

print(arr[i][j])
print(arr[i+1][j+1])
print(arr[i-1][j])



# for i in range(0,len(arr)):
#     for j in range(len(arr[0])):
#             if i+j !=0:
#                 if arr[i][j] == 1:
#                     print(i,j)