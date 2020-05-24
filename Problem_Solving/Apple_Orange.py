s= 7
t= 11

a = 5 
b = 15

apples =[-2,2,1]
oranges =[5,-6] 

apples_sum = [s<= i+a <=t for i in apples]
oranges_sum =[s<= i+b <=t for i in oranges]


print(sum(apples_sum))
print(sum(oranges_sum))


# apples_in_house  = 0
# oranges_in_house = 0


# for i in apples_sum:
#     if i in range(s,t):
#         apples_in_house+=1

# for i in oranges_sum:
#     if i in range(s,t):
#         oranges_in_house+=1


# print(apples_in_house)

# print(oranges_in_house)

