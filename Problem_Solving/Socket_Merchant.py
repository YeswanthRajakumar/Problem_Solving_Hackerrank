pairs = dict()
arr =[1,2,1,2,1,3,1,2,2]
pair_count =0

for i in range(len(arr)):
    pairs[arr[i]] = arr.count(arr[i])//2

print(sum(pairs.values()))
