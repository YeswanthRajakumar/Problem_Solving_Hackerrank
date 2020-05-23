s= 7
t= 11


m_no_of_apples =3
n_no_of_oranges = 2

a_loca_apple_tree = 5 
b_loca_orange_tree = 15

apples =[-2,2,1]
oranges =[5,-6] 

apples_sum = [i+a_loca_apple_tree for i in apples]
oranges_sum =[i+b_loca_orange_tree for i in oranges]

# print('apples_sum : ',apples_sum)
# print('oranges_sum:',oranges_sum)

apples_in_house  = 0
oranges_in_house = 0


for i in apples_sum:
    if i in range(s,t):
        apples_in_house+=1

for i in oranges_sum:
    if i in range(s,t):
        oranges_in_house+=1


print(apples_in_house)

print(oranges_in_house)

