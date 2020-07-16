from collections import Counter 
# a = [4 ,2 ,3 ,4 ,4 ,9 ,98 ,98, 3 ,3 ,3 ,4 ,2 ,98 ,1 ,98 ,98 ,1 ,1, 4 ,98 ,2 ,98 ,3 ,9 ,9 ,3 ,1 ,4 ,1 ,98 ,9 ,9 ,2 ,9 ,4 ,2, 2 ,9 ,98 ,4 ,98 ,1 ,3 ,4 ,9 ,1 ,98 ,98 ,4 ,2 ,3 ,98 ,98, 1 ,99, 9 ,98 ,98, 3 ,98 ,98, 4 ,98, 2 ,98 ,4 ,2 ,1 ,1 ,9, 2 ,4]
a = [1,2,2,3,1,2]
a = Counter(a)
maxnum =0 
print(a)
for i in range(100):
    maxnum = max(maxnum,a[i] + a[i+1])
    print(f'a[i] :{a[i]} + a[i+1]{a[i+1]} ==> {a[i] + a[i+1]} ')
print(maxnum)