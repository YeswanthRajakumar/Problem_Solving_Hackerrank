A =  [0]
converted  =[]
for i in range(len(A)):
    converted.append(str(A[i]))

num_str = ''.join(converted)
num = int(num_str)
num +=1
str_a = str(num)
a = []
for  i in range(len(str_a)):
    a.append(int(str_a[i]))
print(a)