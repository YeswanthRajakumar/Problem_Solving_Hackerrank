na = int(input('Length of A : '))
A = set(map(int,input('Elements in A :').split(' ')))

N = int(input('Other entries Lenght :'))

for i in range(0,N):
    command_list = input().split('Enter command and length :  ')
    other_set = set(map(int,input().split(' ')))
    if command_list[0]=='intersection_update':
        A.intersection_update(other_set)

    elif command_list[0]=='update':
        A.update(other_set)

    elif command_list[0]=='symmetric_difference_update':
        A.symmetric_difference_update(other_set)

    elif command_list[0]=='difference_update':
        A.difference_update(other_set)
       
print(sum(A))