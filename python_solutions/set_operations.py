# n = int(input())
# s = set(map(int, input().split()))
# N = int(input())

# command =[]

# for i in range(0,N):
#     command = input(f'Enter command - {i+1}:').split(' ')
#     if command[0] =='pop':
#         s.pop()
#     elif command[0] =='remove':
#         s.remove(int(command[1]))

#     elif command[0] =='discard':

#          s.discard(int(command[1]))

# print(sum(s))


'''UNION'''

s1 ={ 1,2,3,4,5,6,7,8,9}

s2 ={10,1,2,3,11,21,55,6,8}

s3 = s1.union(s2)
# print(len(s3))



'''Intersection'''

s1 ={ 1,2,3,4,5,6,7,8,9}

s2 ={10,1,2,3,11,21,55,6,8}

s3 = s1.intersection(s2)
# print(len(s3))


'''Set .symmetric_difference() Operation '''


# s1 ={ 1,2,3,4,5,6,7,8,9}

# s2 ={10,1,2,3,11,21,55,6,8}

# s3 = s1.symmetric_difference(s2)
# print(len(s3))



# s1n = int(input())
# s1  = set(map(int,input().split(' ')))

# s2n = int(input())
# s2  = set(map(int,input().split(' ')))


# s3 = s1.symmetric_difference(s2)
# print(len(s3))



''' Sub Set '''

# T = int(input())
# sublist =[]
# for i in  range(0,T):
#     nA = int(input())
#     A = set(map(int,input().split(' ')))
#     nB = int(input())
#     B = set(map(int,input().split(' ')))
#     X = A.issubset(B)
#     sublist.append(X)

# for i in sublist:
#     print(i)


''' super Set '''

A = set(map(int,input().split(' ')))
n = int(input())
sup_list =[]
for i in range(n):
    n_set = set(map(int,input().split(' ')))
    X = A.issuperset(n_set)
    sup_list.append(X)

if False in sup_list:
    print(False)
else:
    print(True)








