n = 6
arr =[-4,3,-9,0,4,1]
p_count = 0
n_count = 0
z_count = 0
for i in arr:
    if i < 0:
        n_count+=1
    elif i == 0:
        z_count+=1
    elif i > 0:
        p_count+=1

print(p_count/n)
print(n_count/n)
print(z_count/n)