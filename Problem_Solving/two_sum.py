a = [-2,1,2,4,7,14]
target = 13
index_i =-1
index_j =-1
for i in range(len(a)):
    for j  in range(len(a)):
        if i != j:
            if a[i] + a[j] == target:
                if index_i == -1 :
                    index_i = i
                    index_j =j

if index_i == -1:
    print("Index not found")
else:                
    print(index_i,index_j)