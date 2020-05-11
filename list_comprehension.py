''' 
NAIVE METHOD :

lists =[]

for letter in 'Hello':
	lists.append(letter)

print(lists)

'''


#LIST COMPREHENSIONS :

'''
SYNTAX :

 [ expression for item in list]



lists =[ i for i in range(1,10) if i%2==0 ]
print(lists)

'''

X = 1
Y = 1 
Z = 1
N = 2

'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
'''
final_list =[]

'''
for i in range(0,X+1):
	for j in range(0,Y+1): 
		for k in range(0,Z+1):
			if i+j+k !=N:
				final_list.append([i,j,k]) 

print(final_list)
'''


final_list =[ [i,j,k] for i in range(0,X+1) for j in range(0,Y+1) for k in range(0,Z+1) if i+j+k !=N]

print(final_list)

