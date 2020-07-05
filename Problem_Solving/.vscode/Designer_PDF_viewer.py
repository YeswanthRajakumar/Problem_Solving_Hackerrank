heights = list(map(int,input().split()))
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = input()
result =[]
for i in word:
    result.append(heights[alpha.index(i)]) 


print(max(result) * len(result))