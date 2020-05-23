a = [
     [11, 2, 4],
     [4, 5 ,6],
     [10 ,8 ,-12]
    ]

# a[0][3]
# a[1][2]
# a[2][1]

d1 = 0
d2 = 0
length =len(a)

for i in range(length):
    # d1.append(a[i][i])
    d1 += a[i][i]
    # d2.append(a[i][length-(i+1)])
    d2 += a[i][length-(i+1)]


dsum = d1-d2
if dsum < 0:
    dsum*=-1

print(dsum)