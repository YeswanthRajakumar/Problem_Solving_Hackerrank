a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
point_a = 0
point_b = 0

for i in range(len(a)):
    if a[i] > b[i]:
            point_a +=1

    if b[i] > a[i]:
            point_b +=1

    elif a[i]==b[i]:
            pass


point_list =[point_a,point_b]
print(point_list)