arr = list(map(int,input().split(' ')))
bird_count =[0,0,0,0,0]
a1 = arr.count(1)
a2 = arr.count(2)
a3 = arr.count(3)
a4 = arr.count(4)
a5 = arr.count(5)

bird_list = [a1,a2,a3,a4,a5]
max_b = max(bird_list) 
print(bird_list.index(max_b)+1)